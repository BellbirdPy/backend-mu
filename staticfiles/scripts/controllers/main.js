'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MainCtrl', function ($scope, ServerData, Establecimiento, $location,$rootScope) {
    $scope.establecimientos = [];
    $scope.obj = ServerData;
    $scope.establecimientos = Establecimiento.get(function(response){
    $scope.establecimientos = response.results;
   });

    $scope.seleccionar = function(e){
      $scope.obj.establecimiento = e;
      $rootScope.establecimiento = e;
      $location.path('/inventario/');
    };





  });
