'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.AnimalCaravana
 * @description
 * # AnimalCaravana
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('AnimalCaravana', function ($resource) {
    return $resource('/animal/list_caravana/:id/' ,null);
  });
