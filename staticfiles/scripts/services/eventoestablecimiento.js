'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.EventoEstablecimiento
 * @description
 * # EventoEstablecimiento
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('EventoEstablecimiento', function ($resource) {
    return $resource('http://localhost:8000/api/sanitacion/eventos_establecimiento/:id/',null,{
      'update': { method:'PUT' },
      'delete': {method:'DELETE'}
    });
  });
