'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MainCtrl', function ($scope, ServerData, Establecimiento, $location,$rootScope, Noticia,$sce,$mdDialog) {
    $scope.establecimientos = [];
    $scope.obj = ServerData;
    $scope.noticias = [];
    Establecimiento.get(function(response){
    $scope.establecimientos = response.results;
   });



    $scope.seleccionar = function(e){
      $scope.obj.establecimiento = e;
      $rootScope.establecimiento = e;
      $location.path('/inventario/');
    };

    Noticia.get({},function(data){
      angular.forEach(data.results,function (item){
        item.texto = $sce.trustAsHtml(item.texto);
      });
      $scope.noticias = data.results;

    });

    $scope.verNoticia = function(noticia) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_noticia.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog' ,function ($scope, $mdDialog) {

          $scope.noticia = noticia;
          $scope.cancel = function () {
            $mdDialog.cancel();
          };

        }]
      });
    };




  });
