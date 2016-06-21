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
      establecimiento : {
        "id": 1,
        "nombre": "Ganadera M - J - G",
        "owner": 1,
        "miembros": [
          25
        ],
        "lotes": [
          1,
          2,
          4,
          21,
          28
        ],
        "potreros": [
          1,
          3,
          4,
          5,
          6,
          8,
          9,
          11
        ]
      }
    };
  });
