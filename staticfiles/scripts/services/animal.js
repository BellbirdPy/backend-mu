'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Animal
 * @description
 * # Animal
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Animal', function ($resource) {
    return $resource('http://localhost:8000/api/animal/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
