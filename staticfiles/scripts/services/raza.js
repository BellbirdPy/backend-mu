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
    return $resource('/api/raza/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
