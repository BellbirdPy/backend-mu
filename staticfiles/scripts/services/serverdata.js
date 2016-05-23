'use strict';

/**
 * @ngdoc service
 * @name frontendmuApp.ServerData
 * @description
 * # ServerData
 * Service in the frontendmuApp.
 */
angular.module('frontendmuApp')
  .service('ServerData', function () {
    // AngularJS will instantiate a singleton by calling "new" on this function
    return {
      establecimiento : ''
    };
  });
