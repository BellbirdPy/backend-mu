'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:CategoriaCtrl
 * @description
 * # CategoriaCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('CategoriaCtrl', function ($scope,Categoria,$mdDialog,$filter,ServerData) {

    $scope.queryCat = {establecimiento: ServerData.establecimiento.id,ordering: 'id',page: 1};
    $scope.selectedCat = [];

    function successCat(categorias) {
      $scope.categorias = categorias;
      console.log($scope.categorias);
    }

    $scope.getCat = function () {
      $scope.promiseCat = Categoria.get($scope.queryCat,successCat).$promise;
      $scope.selectedCat = [];
    };

    $scope.getCat();


    $scope.deleteCat = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar_categoria.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Categoria','$filter' ,function ($scope, $mdDialog, Categoria) {
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
                angular.forEach(lista, function(cat){
                  Categoria.delete({id:cat.id},cat,function(data){
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
            $scope.getCat();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.editCat = function(categoriaModificar) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_categoria.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Raza','ServerData' ,function ($scope, $mdDialog, Raza, ServerData) {
          $scope.newCategoria = {};
          if (categoriaModificar) {
            $scope.newCategoria = categoriaModificar;
          }else{
            $scope.newCategoria.codigo = "";
            $scope.newCategoria.nombre = "";
            $scope.newCategoria.is_hembra = false;
            $scope.newCategoria.establecimiento = ServerData.establecimiento.id;
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (categoriaModificar){
                Categoria.update({id:$scope.newCategoria.id},$scope.newCategoria,function(data){
                  $scope.newCategoria = data;
                  $mdDialog.hide($scope.newCategoria);
                });

              }else {
                var nuevo = new Categoria($scope.newCategoria);

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
            var prueba = $filter('filter')($scope.categorias.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.categorias.results.unshift(nuevo);
              }
            }else{
              $scope.categorias.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

  });
