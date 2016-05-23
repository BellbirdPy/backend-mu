'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Evento
 * @description
 * # Evento
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Evento', function ($resource) {
    return $resource('/api/sanitacion/eventos/:id/',null);
  });
