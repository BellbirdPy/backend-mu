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
    return $resource('/api/animal/:id/' ,null,{
      'update': { method:'PUT' },
      'create': { method:'POST',isArray:true},
      'delete': {method:'DELETE'}
    });
  });
