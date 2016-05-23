'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:InventarioCtrl
 * @description
 * # InventarioCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('InventarioCtrl', function ($scope,$filter,$mdDialog,Animal,Lote, ServerData,Categoria,Raza) {
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
  $scope.queryAnimales = {establecimiento: ServerData.establecimiento.id,estado:'V',ordering: 'caravana',page: 1};
  $scope.selectedAnimales = [];

  function successAnimales(animales) {
    $scope.animales = animales;
  }

  $scope.getAnimales = function () {
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
                var listaId = []
                angular.forEach(lista, function(animalSeleccionado){
                  listaId.push(animalSeleccionado.id);
                  animalSeleccionado.estado = 'M';
                  animalSeleccionado.lote = null;
                  Animal.update({id:animalSeleccionado.id},animalSeleccionado,function(data){
                  });
                });
                var nuevo = new Mortandad($scope.form);
                nuevo.establecimiento = ServerData.establecimiento.id;
                nuevo.animales = [];
                nuevo.$save(function (result) {
                  result.animales = listaId;
                  Mortandad.update({id:result.id},result,function(data){
                    console.log(data);
                  });
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
  $scope.queryLotes = {establecimiento: ServerData.establecimiento.id,ordering: 'nombre',page: 1};
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
        controller: ['$scope','$mdDialog','Potrero','ServerData' ,function ($scope, $mdDialog, Potrero,ServerData) {
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

  });
