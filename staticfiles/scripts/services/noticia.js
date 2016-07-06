'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Noticia
 * @description
 * # Noticia
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Noticia', function ($resource) {
    return $resource('/api/noticia/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
