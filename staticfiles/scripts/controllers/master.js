'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MasterCtrl
 * @description
 * # MasterCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MasterCtrl', function ($scope, $location, ServerData, Establecimiento) {
    $scope.establecimientos = [];
    $scope.obj = ServerData;
    Establecimiento.get(function (data) {
      $scope.establecimientos = data.results;
    });

    $scope.seleccionar = function(e){
      $scope.obj.establecimiento = e;
      $location.path('/inventario/');
    };
  });
