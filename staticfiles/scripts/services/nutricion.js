'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Nutricion
 * @description
 * # Nutricion
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Nutricion', function ($resource) {
    return $resource('/api/nutricion/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
