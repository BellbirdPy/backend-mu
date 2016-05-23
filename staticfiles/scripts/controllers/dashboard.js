'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:DashboardCtrl
 * @description
 * # DashboardCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('DashboardCtrl', function ($scope,Evento,EventoEstablecimiento,$mdDialog,$filter,ServerData) {
    Evento.query(function(response){
      $scope.eventos = response;
      angular.element(('#calendar')).fullCalendar( 'addEventSource', $scope.eventos );
    });

    EventoEstablecimiento.query({'establecimiento':ServerData.establecimiento.id},function(response){
      $scope.eventos_establecimiento = response;
      console.log($scope.eventos_establecimiento);
      angular.element(('#calendar')).fullCalendar( 'addEventSource', $scope.eventos_establecimiento );
    });

    angular.element(('#calendar')).fullCalendar({});


  });
