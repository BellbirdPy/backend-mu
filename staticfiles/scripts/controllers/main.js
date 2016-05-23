'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MainCtrl', function ($scope, ServerData, Establecimiento, $location) {
    $scope.establecimientos = [];
    $scope.obj = ServerData;
    Establecimiento.query(function (data) {
      $scope.establecimientos = data;
    });

    $scope.seleccionar = function(e){
      $scope.obj.establecimiento = e;
      $location.path('/inventario/');
    };



  });
