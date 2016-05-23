'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Establecimiento
 * @description
 * # Establecimiento
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Establecimiento', function ($resource) {
    return $resource('/api/establecimiento/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
