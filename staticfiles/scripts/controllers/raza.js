'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:RazaCtrl
 * @description
 * # RazaCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('RazaCtrl', function ($scope,Raza,$mdDialog,$filter,ServerData) {

    $scope.queryRazas = {establecimiento: ServerData.establecimiento.id,ordering: 'id',page: 1};
    $scope.selectedRazas = [];

  function successRazas(razas) {
    $scope.razas = razas;
    console.log($scope.razas);
  }

  $scope.getRazas = function () {
    $scope.promiseRazas = Raza.get($scope.queryRazas,successRazas).$promise;
    $scope.selectedRazas = [];
  };

  $scope.getRazas();


    $scope.deleteRaza = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar_raza.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Raza','$filter' ,function ($scope, $mdDialog, Raza) {
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
                angular.forEach(lista, function(raza){
                  Raza.delete({id:raza.id},raza,function(data){
                    console.log("Eliminado: " + data.nombre);
                  });
                });
              }
              $mdDialog.hide(lista);
            }else{
              $mdDialog.hide();
            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            $scope.getRazas();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.editRaza = function(razaModificar) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_raza.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Raza','ServerData' ,function ($scope, $mdDialog, Raza, ServerData) {
          $scope.newRaza = {};
          if (razaModificar) {
            $scope.newRaza = razaModificar;
          }else{
            $scope.newRaza.nombre = "";
            $scope.newRaza.descripcion = "";
            $scope.newRaza.establecimiento = ServerData.establecimiento.id;
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (razaModificar){
                Raza.update({id:$scope.newRaza.id},$scope.newRaza,function(data){
                  $scope.newRaza = data;
                  $mdDialog.hide($scope.newRaza);
                });

              }else {
                var nuevo = new Raza($scope.newRaza);

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
            var prueba = $filter('filter')($scope.razas.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.razas.results.unshift(nuevo);
              }
            }else{
              $scope.razas.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

  });
