'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:LogoutCtrl
 * @description
 * # LogoutCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('LogoutCtrl', function ($scope, $location, DjangoAuth,ServerData) {
    DjangoAuth.logout();
  });
