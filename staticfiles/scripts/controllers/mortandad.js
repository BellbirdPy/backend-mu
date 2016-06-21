'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MortandadCtrl
 * @description
 * # MortandadCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MortandadCtrl', function ($scope,$mdDialog,$filter,ServerData,Mortandad) {


    $scope.queryMortandad = {establecimiento: ServerData.establecimiento.id,ordering: 'lote__nombre',page: 1};
    $scope.selectedMortandad = [];

    function successMortandad(mortandades) {
      $scope.mortandades = mortandades;
    }

    $scope.getMortandad = function () {
      $scope.promiseMortandad = Mortandad.get($scope.queryMortandad,successMortandad).$promise;
      console.log($scope.promiseMortandad);
      $scope.selectedMortandad = [];
    };

    $scope.getMortandad();


    $scope.deleteMortandad = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar_mortandad.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Mortandad','$filter' ,function ($scope, $mdDialog, Mortandad,$filter) {
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
                angular.forEach(lista, function(mortandad){
                  Mortandad.delete({id:mortandad.id},mortandad,function(data){
                    console.log("eliminado: " + data.fecha);
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
            $scope.getMortandad();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

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
          if (nuevo !== true) {
            var prueba = $filter('filter')($scope.mortandades.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.mortandades.results.unshift(nuevo);
              }
            }else{
              $scope.mortandades.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.viewMortandad = function(mortandad) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_view_mortandad.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog' ,function ($scope, $mdDialog) {
          $scope.mortandad = mortandad;
          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            $scope.cancel();
          };

        }]
      })
        .then(function(mortandad) {
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };




  });
