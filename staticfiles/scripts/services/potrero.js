'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Potrero
 * @description
 * # Potrero
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Potrero', function ($resource) {
    return $resource('/api/potrero/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
