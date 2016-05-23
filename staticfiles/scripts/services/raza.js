'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Raza
 * @description
 * # Raza
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Raza', function ($resource) {
    return $resource('http://localhost:8000/api/raza/:id/',null);
  });
