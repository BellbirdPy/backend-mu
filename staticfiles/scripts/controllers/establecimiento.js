'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:EstablecimientoCtrl
 * @description
 * # EstablecimientoCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('EstablecimientoCtrl', function ($scope,$location) {
    $scope.go = function ( path ) {
      $location.path( path );
    };
  });
