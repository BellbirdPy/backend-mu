'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:EstablecimientoCtrl
 * @description
 * # EstablecimientoCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('EstablecimientoCtrl', function ($scope,$location,Potrero,Categoria,Raza,Lote, ServerData,$mdDialog, AnimalCaravana) {

    $scope.go = function ( path ) {
      $location.path( path );
    };

    $scope.configuraciones = [
      {nombre:'Potreros',url:'/potrero'},
      {nombre:'Lotes',url:'/inventario'},
      {nombre:'Categorias personalizadas',url:'/categoria'},
      {nombre:'Razas perzonalizadas',url:'/raza'}

    ];


    $scope.cargaAnimales = function() {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_carga_animales.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Raza','Categoria','ServerData','$filter','Animal','AnimalCaravana','Potrero','$rootScope' ,function ($scope, $mdDialog, Raza,Categoria, ServerData,$filter,Animal,AnimalCaravana,Potrero,$rootScope) {

          var query = {establecimiento: ServerData.establecimiento.id,ordering: 'id',page: 1,limit:100};
          Categoria.get(query,function(response){
            $scope.categorias = response;
          });
          Raza.get(query,function(response){
            $scope.razas = response;
          });
          Lote.get(query,function(response){
            $scope.lotes = response;
          });
          Potrero.get(query,function(response){
            $scope.potreros = response;
          });
          AnimalCaravana.get({id:ServerData.establecimiento.id},function(response){
            $scope.caravanas = response.animales;
          });

          $scope.crearExcel = function (){
            $scope.$parent.crearExcel();
          };

          $scope.options = {
            pageSelect: true
          };
          $scope.logPagination = function (page, limit) {
            console.log('page: ', page);
            console.log('limit: ', limit);
          }
          $scope.query = {
            limit: 20,
            page: 1
          };

          var X = XLSX;
          $scope.paso = 1;
          $scope.error =[];
          $scope.cargado = false;

          function comprobarHeader(sheet){
            var headerComprobacion = ["N° de Caravana", "Código de Raza", "Código de Categoría", "Carimbo", "N° de Caravana de la Madre", "Código de Lote", "Estado sanitario", "Peso especifico"];
            var header = get_header_row(sheet);
            var result = true;
            if (headerComprobacion.length == header.length) {
              angular.forEach(header, function (item) {
                if (headerComprobacion.indexOf(item) == -1) {
                  result = false;
                }
              });
            }else{
              result = false;
            }

            return result;
          };

          var to_json = function (workbook) {
            var result = {};
            var sheet = workbook.Sheets[workbook.SheetNames[0]];
            $scope.error = [];
            $scope.cargado = false;
            if (comprobarHeader(sheet)) {
              var roa = X.utils.sheet_to_row_object_array(sheet);
              if (roa.length > 0) {
                result = roa;
                $scope.subirArchivo(result);
                $scope.cargado = true;
                $scope.model = {};
                document.getElementById("file").value = "";
                document.getElementById("file").onchange();
              }
            }else{
              $scope.error.push('Error en el formato del archivo excel. Por favor siga todos los pasos.');
              console.log($scope.error);
              $scope.cargado = false;
              document.getElementById("file").value = "";
              document.getElementById("file").onchange();
            }

          };

          function get_header_row(sheet) {
            var headers = [];
            var range = XLSX.utils.decode_range(sheet['!ref']);
            var C, R = range.s.r; /* start in the first row */
            /* walk every column in the range */
            for(C = range.s.c; C <= range.e.c; ++C) {
              var cell = sheet[XLSX.utils.encode_cell({c:C, r:R})] /* find the cell in the first row */

              var hdr = "UNKNOWN " + C; // <-- replace with your desired default
              if(cell && cell.t) hdr = XLSX.utils.format_cell(cell);

              headers.push(hdr);
            }
            return headers;
          }

          $scope.guardarAnimales = function(){
            console.log({animales:$scope.archivo});
            Animal.create({animales:$scope.archivo},function(data){
              console.log(data);
              if (data.length){
                $scope.hide();
              }

            });
          }

          $scope.generarPlantilla = function (){
            var wb = new Workbook(['Animales']);
            var wsani = sheet_from_array_of_arrays([['N° de Caravana','Código de Raza',	'Código de Categoría','Carimbo',	'N° de Caravana de la Madre',	'Código de Lote','Estado sanitario']])
            var wscols = [
              {wch:15},
              {wch:15},
              {wch:18},
              {wch:10},
              {wch:25},
              {wch:15}
            ];
            wsani['!cols'] = wscols;

            wb.Sheets['Animales'] = wsani;
            var wbout = XLSX.write(wb, {bookType:'xlsx', bookSST:true, type: 'binary'});

            function s2ab(s) {
              var buf = new ArrayBuffer(s.length);
              var view = new Uint8Array(buf);
              for (var i=0; i!=s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
              return buf;
            }
            saveAs(new Blob([s2ab(wbout)],{type:"application/octet-stream"}), "animales.xlsx")

          };

          function datenum(v, date1904) {
            if(date1904) v+=1462;
            var epoch = Date.parse(v);
            return (epoch - new Date(Date.UTC(1899, 11, 30))) / (24 * 60 * 60 * 1000);
          }

          function capitalizeFirstLetter(string) {
            return string.charAt(0).toUpperCase() + string.slice(1);
          }

          function array_from_json(data){
            var aux = 0;
            var lista = [];
            var borrarId = false;
            angular.forEach(data, function(item){
              delete item.establecimiento;
              delete item.animales;
              delete item.is_hembra;
              delete item.potrero;
              if (borrarId){
                delete item.id;
              }
              if (aux==0){
                var header = $rootScope.Utils.keys(item);
                angular.forEach(header, function(titulo){
                  if (titulo == 'potrero_nombre'){
                    header[$.inArray(titulo, header)] = 'Potrero';
                  }else if (titulo == 'peso_promedio') {
                    header[$.inArray(titulo, header)] = 'Peso promedio';
                  }else{
                    header[$.inArray(titulo, header)] = capitalizeFirstLetter(titulo);
                  }
                });
                var estaDentro = $.inArray('Codigo', header);
                if (estaDentro < 0){
                  header[0] = 'Código';
                  borrarId =false;
                }else{
                  delete item.id;
                  header = $rootScope.Utils.keys(item);
                  angular.forEach(header, function(titulo){
                    header[$.inArray(titulo, header)] = capitalizeFirstLetter(titulo);
                  });
                  borrarId = true;
                  estaDentro = $.inArray('Codigo', header);
                  header[estaDentro] = 'Código';
                }

                console.log(header);
                lista.push(header);
                var arr = $.map(item, function(el) { return el });
                lista.push(arr);
              }else{
                var arr = $.map(item, function(el) { return el });
                lista.push(arr);
              }
              aux += 1;
            });
            return lista;
          }

          function sheet_from_array_of_arrays(data, opts) {
            var ws = {};
            var range = {s: {c:10000000, r:10000000}, e: {c:0, r:0 }};
            for(var R = 0; R != data.length; ++R) {
              for(var C = 0; C != data[R].length; ++C) {
                if(range.s.r > R) range.s.r = R;
                if(range.s.c > C) range.s.c = C;
                if(range.e.r < R) range.e.r = R;
                if(range.e.c < C) range.e.c = C;
                var cell = {v: data[R][C] };
                if(cell.v == null) continue;
                var cell_ref = XLSX.utils.encode_cell({c:C,r:R});

                if(typeof cell.v === 'number') cell.t = 'n';
                else if(typeof cell.v === 'boolean') cell.t = 'b';
                else if(cell.v instanceof Date) {
                  cell.t = 'n'; cell.z = XLSX.SSF._table[14];
                  cell.v = datenum(cell.v);
                }
                else cell.t = 's';

                ws[cell_ref] = cell;
              }
            }
            if(range.s.c < 10000000) ws['!ref'] = XLSX.utils.encode_range(range);
            return ws;
          }

          function Workbook(sheetNames) {
            if(!(this instanceof Workbook)) return new Workbook();
            this.SheetNames = sheetNames;
            this.Sheets = {};
          }

          $scope.setFiles = function(element) {
            $scope.$apply(function($scope) {
              console.log('files:', element.files);
              // Turn the FileList object into an Array
              $scope.files = [];
              for (var i = 0; i < element.files.length; i++) {
                $scope.files.push(element.files[i]);
              }
              if ($scope.files.length > 0) {
                $scope.handleFile()
              }
            });
          };

          $scope.handleFile = function() {
            var files = $scope.files;
            var i, f;
            for (i = 0, f = files[i]; i != files.length; ++i) {
              var reader = new FileReader();
              var name = f.name;
              reader.onload = function (e) {
                var data = e.target.result;

                var workbook = X.read(data, {type: 'binary'});
                console.log(workbook);
                to_json(workbook);

                /* DO SOMETHING WITH workbook HERE */

              };
              reader.readAsBinaryString(f);
            }
          };

          $scope.subirArchivo = function(result) {
            $scope.archivo = result;


            var rename = function (obj, oldName, newName) {
              // Do nothing if the names are the same
              if (oldName == newName) {
                return obj;
              }
              // Check for the old property name to avoid a ReferenceError in strict mode.
              if (obj.hasOwnProperty(oldName)) {
                obj[newName] = obj[oldName];
                delete obj[oldName];
              }
              return obj;
            };
            angular.forEach($scope.archivo, function (animal) {
              animal.estado = 'V';
              animal.establecimiento = ServerData.establecimiento.id;
              animal = rename(animal, 'N° de Caravana', 'caravana');
              animal = rename(animal, 'Código de Raza', 'raza');
              animal = rename(animal, 'Código de Categoría', 'categoria');
              animal = rename(animal, 'Carimbo', 'carimbo');
              animal = rename(animal, 'N° de Caravana de la Madre', 'caravana_madre');
              animal = rename(animal, 'Código de Lote', 'lote');
              animal = rename(animal, 'Estado sanitario', 'estado_sanitario');
              animal = rename(animal, 'Peso especifico', 'peso_especifico');
              if ( isNaN(animal.carimbo)){
                animal.carimbo = 'Error';
                animal.error = true;
                $scope.error.push('El carimbo debe ser numerico (0-9). Caravana Nº: ' + animal.caravana.toString());
              }else{
                if (animal.carimbo >= 0 && animal.carimbo <10 ){
                }else{
                  animal.carimbo = 'Error';
                  animal.error = true;
                  $scope.error.push('El carimbo debe estar en el rango de (0-9). Caravana Nº: ' + animal.caravana.toString());
                }
              }
              if ( isNaN(animal.peso_especifico)){
                animal.peso_especifico = 'Error';
                animal.error = true;
                $scope.error.push('El peso debe ser numerico. Caravana Nº: ' + animal.caravana.toString());
              }else {
                if (animal.peso_especifico > 0) {
                } else {
                  animal.peso_especifico = 'Error';
                  animal.error = true;
                  $scope.error.push('El peso debe ser positivo. Caravana Nº: ' + animal.caravana.toString());
                }
              }
              animal.estado = 'V';
              animal.establecimiento = ServerData.establecimiento.id;
              if (animal.estado_sanitario.toString() === 'E') {
                animal.estado_sanitario_display = 'En fecha';
              } else if (animal.estado_sanitario.toString() === 'N') {
                animal.estado_sanitario_display = 'No esta en fecha';
              } else if (animal.estado_sanitario.toString() === 'D') {
                animal.estado_sanitario_display = 'Desconocido';
              } else {
                animal.estado_sanitario = '';
                animal.estado_sanitario_display = 'Error';
                animal.error = true;
                $scope.error.push('El estado sanitario no es valido. Por favor use estas opciones: "E" o "N" o "D". Caravana Nº: ' + animal.caravana.toString());
              }
              var raza_nombre = $filter('filter')($scope.razas.results, function (d) {return d.id.toString() === animal.raza.toString();})[0];
              if (raza_nombre){
                animal.raza_nombre = raza_nombre.nombre;
              }else{
                animal.error = true;
                animal.raza_nombre = 'Error';
                $scope.error.push('El codigo de raza no es valido. Caravana Nº: ' + animal.caravana.toString());
              }
              var categoria = $filter('filter')($scope.categorias.results, function (d) {return d.codigo.toString() === animal.categoria.toString();})[0];
              if (categoria){
                animal.categoria_nombre = categoria.nombre;
                animal.categoria = categoria.id;
              }else{
                animal.error = true;
                animal.categoria_nombre = 'Error';
                $scope.error.push('El codigo de categoria no es valido. Caravana Nº: ' + animal.caravana.toString());
              }
              var lote_nombre = $filter('filter')($scope.lotes.results, function (d) {return d.id.toString() === animal.lote.toString();})[0];
              if (lote_nombre != null){
                animal.lote_nombre = lote_nombre.nombre;
              }else{
                animal.lote_nombre = 'Error';
                animal.error = true;
                $scope.error.push('El codigo de lote no es valido. Caravana Nº: ' + animal.caravana.toString());
              }
            });

            angular.forEach($scope.archivo, function (animal) {
              if ($filter('filter')($scope.archivo, function (d) {return d.caravana.toString() === animal.caravana.toString();}).length > 1 ||$filter('filter')($scope.caravanas, function (d) {return d.toString() === animal.caravana.toString();}).length > 0) {
                animal.error = true;
                var mensaje = 'Existen caravanas iguales. Caravana Nº: ' + animal.caravana.toString();
                if ($filter('filter')($scope.error, function (d) {return d === mensaje;}).length == 0 ){
                  $scope.error.push(mensaje);
                }

              }
            });
            console.log($scope.error);
          };

          $scope.crearExcel = function (){
            console.log('crearExcel')
            var wb = new Workbook(['Potreros','Lotes','Categorias','Razas']);
            var wscat = sheet_from_array_of_arrays(array_from_json($scope.categorias.results));
            var wslot = sheet_from_array_of_arrays(array_from_json($scope.lotes.results));
            var wsraz = sheet_from_array_of_arrays(array_from_json($scope.razas.results));
            var wspot = sheet_from_array_of_arrays(array_from_json($scope.potreros.results));



            var wscols = [
              {wch:20},
              {wch:20},
              {wch:20},
              {wch:20}
            ];
            wspot['!cols'] = wscols;
            wscat['!cols'] = wscols;
            wsraz['!cols'] = wscols;
            wslot['!cols'] = wscols;
            /* add worksheet to workbook */
            wb.Sheets['Potreros'] = wspot;
            wb.Sheets['Lotes'] = wslot;
            wb.Sheets['Categorias'] = wscat;
            wb.Sheets['Razas'] = wsraz;
            wb.Sheets['Potreros']
            var wbout = XLSX.write(wb, {bookType:'xlsx', bookSST:true, type: 'binary'});

            function s2ab(s) {
              var buf = new ArrayBuffer(s.length);
              var view = new Uint8Array(buf);
              for (var i=0; i!=s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
              return buf;
            }
            saveAs(new Blob([s2ab(wbout)],{type:"application/octet-stream"}), "configuracion.xlsx")
          };

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
          };

        }]
      })
        .then(function(nuevo) {
          console.log(nuevo);
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };
  });
