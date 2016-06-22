'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Empleado
 * @description
 * # Empleado
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Empleado', function ($resource) {
    return $resource('/api/empleado/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
