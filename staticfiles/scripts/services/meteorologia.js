'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.Meteorologia
 * @description
 * # Meteorologia
 * Factory in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .factory('Meteorologia', function ($resource) {
    return {
      server:$resource('/api/meteorologia/:id/',null),
      forecast:$resource('http://api.openweathermap.org/data/2.5/forecast/daily',null),
      current:$resource('http://api.openweathermap.org/data/2.5/weather',null)
    }
  });
