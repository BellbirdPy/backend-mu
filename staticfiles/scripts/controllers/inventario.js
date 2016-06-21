'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:InventarioCtrl
 * @description
 * # InventarioCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('InventarioCtrl', function ($scope,$filter,$mdDialog,$mdMedia,Animal,Lote, ServerData,Categoria,Raza,Mortandad,Establecimiento) {
    var obj = ServerData;
    $scope.estados_sanitarios = [{c:'E',display:'En fecha'},{c:'N',display:'No esta en fecha'},{c:'D',display:'En fecha'}]

    $scope.categorias = Categoria.get(function(response){
      $scope.categorias = response;
    });
    $scope.razas = Raza.get(function(response){
      $scope.razas = response;
    });

    $scope.options = {
      boundaryLinks: false,
      pageSelect: true
    };


    //-----------------------------------ANIMALES---------------------------------------------------
    $scope.queryAnimales = {establecimiento: ServerData.establecimiento.id,limit:20, estado:'V',ordering: 'lote__nombre',page: 1};
    $scope.selectedAnimales = [];

    function successAnimales(animales) {
      $scope.animales = animales;
    }

    $scope.getAnimales = function () {
      console.log($scope.queryAnimales);
      $scope.promiseAnimales = Animal.get($scope.queryAnimales,successAnimales).$promise;
      $scope.selectedAnimales = [];
    };

    $scope.getAnimales();

    $scope.editAnimal = function(animalSeleccionado) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_animal.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Animal','Categoria','Raza','Lote' ,function ($scope, $mdDialog, Animal, Categoria,Raza, Lote) {
          $scope.categorias =[];
          $scope.razas = [];
          $scope.lotes = [];

          $scope.lotes = Lote.get({establecimiento:obj.establecimiento.id},function(response){
            $scope.lotes = response.results;
          });

          $scope.categorias = Categoria.get(function(response){
            $scope.categorias = response.results;
          });

          $scope.razas = Raza.get(function(response){
            $scope.razas = response.results;
          });

          $scope.newAnimal = {};

          if (animalSeleccionado) {
            $scope.newAnimal = animalSeleccionado;
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (animalSeleccionado){
                Animal.update({id:$scope.newAnimal.id},$scope.newAnimal,function(data){
                  $scope.newAnimal = data;
                  $mdDialog.hide($scope.newAnimal);
                });
              }else {
                $scope.newAnimal.estado = "V";
                $scope.newAnimal.establecimiento = obj.establecimiento.id;
                var nuevo = new Animal($scope.newAnimal);

                nuevo.$save(function () {

                }, function (error) {
                  console.log(error);
                });
                $mdDialog.hide(nuevo);
              }
            }
          };

        }]
      })
        .then(function(nuevo) {
          if (nuevo !== true) {
            var prueba = $filter('filter')($scope.animales.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.animales.results.unshift(nuevo);
              }
            }else{
              $scope.animales.results.unshift(nuevo);
            }

          }
          $scope.getLotes();
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.deleteAnimal = function(animalSeleccionado) {
      // Appending dialog to document.body to cover sidenav in docs app]

      var confirm = $mdDialog.confirm().title('Estas seguro de que quieres eliminar?')
        .textContent(animalSeleccionado.categoria_nombre + '- Caravana: '+animalSeleccionado.caravana + ' - Raza: ' + animalSeleccionado.raza_nombre + ' - Carimbo: ' + animalSeleccionado.carimbo)
        .ariaLabel('Eliminar Animal')
        .targetEvent(null)
        .ok('Sí, estoy seguro')
        .cancel('Cancelar');
      $mdDialog.show(confirm).then(function() {
        Animal.delete({id:animalSeleccionado.id},animalSeleccionado,function(data){
          $scope.getLotes();
          var prueba = $filter('filter')($scope.animales.results, function (d) {return d.id.toString() === animalSeleccionado.id.toString();})[0];
          $scope.animales.results.shift(prueba);
        });
      }, function() {
        console.log('Cancelaste');
      });
    };

    $scope.deleteListaAnimal = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Animal','$filter' ,function ($scope, $mdDialog, Animal,$filter) {
          $scope.lista = lista;
          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (lista.length >= 1){
                angular.forEach(lista, function(animalSeleccionado){
                  Animal.delete({id:animalSeleccionado.id},animalSeleccionado,function(data){
                    console.log("eliminado: " + data.caravana);
                    $mdDialog.hide(lista);
                  });
                });
              }
            }else{
              $mdDialog.hide(lista);
            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            $scope.getAnimales();
            $scope.getLotes();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.mudarAnimales = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_mudar.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Lote','Animal','$filter' ,function ($scope, $mdDialog, Lote, Animal, $filter) {
          $scope.lotes =[];
          $scope.lotes = Lote.get({establecimiento:obj.establecimiento.id},function(response){
            $scope.lotes = response.results;
          });

          $scope.form = {};


          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (lista.length >= 1){
                angular.forEach(lista, function(animalSeleccionado){
                  animalSeleccionado.lote = $scope.form.lote;
                  Animal.update({id:animalSeleccionado.id},animalSeleccionado,function(data){
                    console.log(data);
                  });
                  var lote_nombre = $filter('filter')($scope.lotes, function (d) {return d.id.toString() === $scope.form.lote.toString();})[0];
                  animalSeleccionado.lote_nombre = lote_nombre.nombre;
                });
                $mdDialog.hide(lista);
              }
            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            $scope.getLotes();
            angular.forEach(lista,function(nuevo){
              var prueba = $filter('filter')($scope.animales.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
              if (prueba){
                if (prueba.id === nuevo.id) {
                  angular.extend(prueba, nuevo);
                }
              }
            });


          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.recategorizar = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_recategorizar.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Categoria','Animal','$filter' ,function ($scope, $mdDialog, Categoria, Animal,$filter) {
          $scope.categorias =[];

          $scope.categorias = Categoria.get(function(response){
            $scope.categorias = response.results;
          });

          $scope.form = {};


          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (lista.length >= 1){
                angular.forEach(lista, function(animalSeleccionado){

                  animalSeleccionado.categoria = $scope.form.categoria;
                  Animal.update({id:animalSeleccionado.id},animalSeleccionado,function(data){
                    console.log(data);
                  });
                  var id = $scope.form.categoria;
                  var categoria_nombre = $filter('filter')($scope.categorias,function (d) {return d.id.toString() === id.toString();})[0];
                  animalSeleccionado.categoria_nombre = categoria_nombre.nombre;
                });
                $mdDialog.hide(lista);
              }
            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            angular.forEach(lista,function(nuevo){
              var prueba = $filter('filter')($scope.animales.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
              if (prueba){
                if (prueba.id === nuevo.id) {
                  angular.extend(prueba, nuevo);
                }
              }
            });

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.agruparEnLote = function(lista) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_lote.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Potrero','ServerData' ,function ($scope, $mdDialog, Potrero,ServerData) {
          $scope.potreros =[];

          $scope.potreros = Potrero.get({establecimiento:ServerData.establecimiento.id,lote:''},function(response){
            $scope.potreros = response.results;
          });

          $scope.newLote = {};
          $scope.newLote.potrero = "";
          $scope.newLote.cantidad = 0;
          $scope.newLote.peso_promedio = 0;
          $scope.newLote.establecimiento = ServerData.establecimiento.id;
          $scope.newLote.animales = [];

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              var nuevo = new Lote($scope.newLote);

              nuevo.$save(function (result) {
                if (lista.length >= 1){
                  angular.forEach(lista, function(animalSeleccionado){
                    animalSeleccionado.lote = nuevo.id;
                    Animal.update({id:animalSeleccionado.id},animalSeleccionado,function(data){
                      console.log(data);
                    });
                    animalSeleccionado.lote_nombre = nuevo.nombre;
                  });
                  $mdDialog.hide(lista);
                }

              }, function (error) {
                console.log(error);
              });
              $mdDialog.hide(lista);

            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            $scope.getLotes();
            angular.forEach(lista,function(nuevo){
              var prueba = $filter('filter')($scope.animales.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
              if (prueba){
                if (prueba.id === nuevo.id) {
                  angular.extend(prueba, nuevo);
                }
              }
            });

          }

        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.mortandad = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_mortandad.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Animal','Mortandad','ServerData' ,function ($scope, $mdDialog, Animal, Mortandad,ServerData) {

          $scope.newMortandad = {};

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (lista.length >= 1){
                var listaId = []
                angular.forEach(lista, function(animalSeleccionado){
                  listaId.push(animalSeleccionado.id);
                });
                var nuevo = new Mortandad($scope.form);
                nuevo.establecimiento = ServerData.establecimiento.id;
                nuevo.animales = listaId;
                nuevo.$save(function (result) {
                  console.log(result);
                }, function (error) {
                  console.log(error);
                });

                $mdDialog.hide(lista);
              }
            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            $scope.getAnimales();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    //-----------------------------------LOTES---------------------------------------------------
    $scope.queryLotes = {establecimiento: ServerData.establecimiento.id,ordering: 'id',page: 1};
    $scope.selectedLotes = [];

    function successLotes(lotes) {
      $scope.lotes = lotes;
    }

    $scope.getLotes = function () {
      $scope.promiseLotes = Lote.get($scope.queryLotes,successLotes).$promise;
      $scope.selectedLotes = [];
    };

    $scope.getLotes();

    $scope.deleteLote = function(lote) {
      // Appending dialog to document.body to cover sidenav in docs app
      var confirm = $mdDialog.confirm()
        .title('Estas seguro de que quieres eliminar?')
        .content('Lote: '+lote.nombre + ' - ' +
        'Potrero: ' + lote.potrero_nombre + ' - ' +
        'Cantidad de animales: ' + lote.animales.length )
        .ariaLabel('Lucky day')
        .targetEvent(null)
        .ok('Sí, estoy seguro')
        .cancel('Cancelar');
      $mdDialog.show(confirm).then(function() {
        Lote.delete({id:lote.id},lote,function(data){
          console.log(data);
          console.log(ServerData);
          ServerData.establecimiento = Establecimiento.get({id:ServerData.establecimiento.id});
          console.log(ServerData);
        });
        $scope.lotes.results.splice($scope.lotes.results.indexOf(lote),1);
        $scope.selectedLotes = []
      }, function() {
        $scope.status = 'Se eliminó correctamente.';

      });
    };

    $scope.editLote = function(loteSeleccionado) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_lote.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Potrero','ServerData','Establecimiento' ,function ($scope, $mdDialog, Potrero,ServerData,Establecimiento) {
          $scope.potreros =[];

          $scope.potreros = Potrero.get({establecimiento:ServerData.establecimiento.id,lote:""},function(response){
            $scope.potreros = response.results;
          });

          $scope.newLote = {};
          if (loteSeleccionado) {
            $scope.newLote = loteSeleccionado;
          }else{
            $scope.newLote.potrero = "";
            $scope.newLote.cantidad = 0;
            $scope.newLote.peso_promedio = 0;
            $scope.newLote.establecimiento = obj.establecimiento.id;
            $scope.newLote.animales = [];
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (loteSeleccionado){
                Lote.update({id:$scope.newLote.id},$scope.newLote,function(data){
                  $scope.newLote = data;
                  $mdDialog.hide($scope.newLote);
                });

              }else {
                var nuevo = new Lote($scope.newLote);

                nuevo.$save(function () {
                  console.log(ServerData);
                  ServerData.establecimiento = Establecimiento.get({id:ServerData.establecimiento.id});
                  console.log(ServerData);

                }, function (error) {
                  console.log(error);
                });
                $mdDialog.hide(nuevo);
              }
            }
          };

        }]
      })
        .then(function(nuevo) {
          if (nuevo !== true) {
            var prueba = $filter('filter')($scope.lotes.results,function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.lotes.results.unshift(nuevo);
              }
            }else{
              $scope.lotes.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };


    //------------------------------------MORTANDAD Y ABIGEO---------------

    $scope.editMortandad = function(mortandad) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_mortandad.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Animal','Mortandad' ,function ($scope, $mdDialog, Animal, Mortandad) {
          $scope.hola = 'hola';
          $scope.form = {};
          if (mortandad) {
            $scope.form = mortandad;
            $scope.form.fecha = new Date(mortandad.fecha);
            console.log($scope.form);
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (mortandad){

                Mortandad.update({id:$scope.form.id},$scope.form,function(data){
                  $scope.form = data;
                  $mdDialog.hide($scope.form);
                });
              }
            }
          };

        }]
      })
        .then(function(nuevo) {
          console.log(nuevo);
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };



    //------------------------------------MANEJO DE ARCHIVOS---------------
    var X = XLSX;
    $scope.archivo = {};
    $scope.cargarArchivo = function(result) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_archivo.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Animal','ServerData' ,function ($scope, $mdDialog, Animal,ServerData) {


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
          $scope.archivo = result;
          var categorias = {'1':'Toro','2':'Vaca','3':'Desmamante','4':'Ternero'};
          var razas = {'1':'Brahman','2':'Angus','3':'Brangus','4':'Nelore'};

          var rename = function (obj,oldName, newName) {
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
          angular.forEach($scope.archivo, function(animal){
            animal = rename(animal,'N° de Caravana','caravana');
            animal = rename(animal,'Código de Raza','raza');
            animal = rename(animal,'Código de Categoría','categoria');
            animal = rename(animal,'Carimbo','carimbo');
            animal = rename(animal,'N° de Caravana de la Madre','caravana_madre');
            animal = rename(animal,'Código de Lote','lote');
            animal = rename(animal,'Estado sanitario','estado_sanitario');
            animal.estado = 'V';
            animal.establecimiento = ServerData.establecimiento.id;
            if (animal.estado_sanitario.toString() === 'En fecha'){
              animal.estado_sanitario = 'E';
              animal.estado_sanitario_display = 'En fecha';
            }else if (animal.estado_sanitario.toString() === 'No esta en fecha'){
              animal.estado_sanitario = 'N';
              animal.estado_sanitario_display = 'No esta en fecha';
            }else if (animal.estado_sanitario.toString() === 'Desconocido'){
              animal.estado_sanitario = 'D';
              animal.estado_sanitario_display = 'Desconocido';
            }else {
              animal.estado_sanitario = 'E';
              animal.estado_sanitario_display = 'En fecha';
            }
            animal.raza_nombre = razas[animal.raza];
            animal.categoria_nombre = categorias[animal.categoria];



          });


          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              angular.forEach($scope.archivo, function(animal){
                var nuevo = new Animal(animal);
                console.log(nuevo);

                nuevo.$save(function () {

                }, function (error) {
                  console.log(error);
                });


              });
              $mdDialog.hide();

            }
          };

        }]
      })
        .then(function() {
          $scope.getAnimales();
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    var to_json = function (workbook) {
      var result = {};
      var roa = X.utils.sheet_to_row_object_array(workbook.Sheets[workbook.SheetNames[0]]);
      if(roa.length > 0){
        result = roa;
      }
      $scope.cargarArchivo(result);
      $scope.model = {};
    }

    $scope.handleFile = function(e) {
      console.log(e);

      var files = [e.file];
      var i,f;
      for (i = 0, f = files[i]; i != files.length; ++i) {
        var reader = new FileReader();
        var name = f.name;
        reader.onload = function(e) {
          var data = e.target.result;

          var workbook = X.read(data, {type: 'binary'});
          console.log('ok');
          to_json(workbook);

          /* DO SOMETHING WITH workbook HERE */

        };
        reader.readAsBinaryString(f);
      }
    }



  });
