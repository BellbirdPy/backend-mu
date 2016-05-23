'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Lote
 * @description
 * # Lote
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Lote', function ($resource) {
    return $resource('/api/lote/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
