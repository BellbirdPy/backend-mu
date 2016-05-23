'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:SanitacionCtrl
 * @description
 * # SanitacionCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('SanitacionCtrl', function ($scope,Evento,EventoEstablecimiento,$mdDialog,$filter,ServerData) {
    Evento.query(function(response){
      $scope.eventos = response;
      angular.element(('#calendar')).fullCalendar( 'addEventSource', $scope.eventos );
    });

    EventoEstablecimiento.query({'establecimiento':ServerData.establecimiento.id},function(response){
      $scope.eventos_establecimiento = response;
      console.log($scope.eventos_establecimiento);
      angular.element(('#calendar')).fullCalendar( 'addEventSource', $scope.eventos_establecimiento );
    });

    $scope.showAlert = function(ev) {
      // Appending dialog to document.body to cover sidenav in docs app
      // Modal dialogs should fully cover application
      // to prevent interaction outside of dialog
      $mdDialog.show(
        $mdDialog.alert()
          .parent(angular.element(document.querySelector('#popupContainer')))
          .clickOutsideToClose(true)
          .title('Sanitación')
          .textContent(ev.title )
          .ariaLabel('Alert Dialog')
          .ok('OK!')
          .targetEvent(null)
      );
    };

    angular.element(('#calendar')).fullCalendar(
      {
        eventClick: function(calEvent, jsEvent, view) {
          if (calEvent.veterinario){

          var prueba = $filter('filter')($scope.eventos_establecimiento, { id: calEvent.id }, true)[0];

          $scope.agregarEvento(prueba);
          }
        },
        dayClick: function (date, jsEvent, view) {
          var eventoNuevo = {start:date,end:date,veterinario:'',establecimiento:ServerData.establecimiento.id,nombre:''};

          $scope.agregarEvento(eventoNuevo);

        }
      }
    );





    $scope.agregarEvento = function(evento) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_evento.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','EventoEstablecimiento','$filter','ServerData' ,function ($scope, $mdDialog, EventoEstablecimiento,$filter,ServerData) {

          $scope.newEvento = {};
          if (evento) {
            if (evento.id) {
              $scope.newEvento = evento;
              $scope.newEvento.start = new Date(evento.start);
              $scope.newEvento.end = new Date(evento.end);
            } else {
              $scope.newEvento = evento;
              $scope.newEvento.start = new Date(evento.start);
              $scope.newEvento.end = new Date(evento.end);
            }
          }
          $scope.deleteEvento = function(evento) {
            var confirm = $mdDialog.confirm().title('Estas seguro de que quieres eliminar?')
              .textContent(evento.title)
              .ariaLabel('Eliminar Vacunación')
              .targetEvent(null)
              .ok('Sí, estoy seguro')
              .cancel('Cancelar');
            $mdDialog.show(confirm).then(function() {
              EventoEstablecimiento.delete({id:evento.id},evento,function(data){
                angular.element(('#calendar')).fullCalendar( 'removeEvents', [evento.id] );
              });

            }, function() {
              console.log('Cancelaste');
            });
          };




          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (evento.id){
                console.log($scope.newEvento);
                EventoEstablecimiento.update({id:$scope.newEvento.id},$scope.newEvento,function(data){
                  $scope.newEvento = data;
                  $mdDialog.hide($scope.newEvento);
                });
              }else {
                $scope.newEvento.establecimiento = ServerData.establecimiento.id;
                var nuevo = new EventoEstablecimiento($scope.newEvento);

                nuevo.$save(function (data) {
                  angular.element(('#calendar')).fullCalendar( 'addEventSource', [data] );
                }, function (error) {
                  console.log(error);
                });
                $mdDialog.hide(nuevo);
              }
            }
          };

        }]
      })
        .then(function(nuevo) {
          if (nuevo){
          if (nuevo !== true) {
            var prueba = $filter('filter')($scope.eventos_establecimiento, { id: nuevo.id }, true)[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
                angular.element(('#calendar')).fullCalendar( 'removeEvents', [nuevo.id] );
                angular.element(('#calendar')).fullCalendar( 'addEventSource', [nuevo] );
              }else{
                $scope.eventos_establecimiento.unshift(nuevo);
              }
            }else{
              $scope.eventos_establecimiento.unshift(nuevo);
            }

          }
          }

        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

  });
