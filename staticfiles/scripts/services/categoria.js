'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Categoria
 * @description
 * # Categoria
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Categoria', function ($resource) {
    return $resource('http://localhost:8000/api/categoria/:id/',null);
  });
