'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MeteorologiaCtrl
 * @description
 * # MeteorologiaCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MeteorologiaCtrl', function ($scope,$mdDialog,ServerData,Meteorologia,$filter) {

    $scope.query = {q:'Asunción',units:'metric',lang:'es',APPID:'38212c68fe70ee4c21988681e3982a25'};

  $scope.getWeather = function () {
    Meteorologia.current.get($scope.query, function(data){
      data.dt = data.dt*1000;
      if (data.weather[0].description == 'nubes rotas'){
        data.weather[0].description = 'parcialmente nublado';
      }
      data.wind.speed = data.wind.speed*3.6;
      data.wind.speed = data.wind.speed.toFixed(1);
      data.main.temp = data.main.temp.toFixed(1);
      $scope.current = data;
    });

    Meteorologia.forecast.get($scope.query,function(data){
      data.list.shift();
      angular.forEach(data.list,function(item){
        if (item.weather[0].description == 'nubes rotas'){
          item.weather[0].description = 'parcialmente nublado';
        }
        item.dt = new Date(item.dt*1000);
        item.temp.min = item.temp.min.toFixed(1);
        item.temp.max = item.temp.max.toFixed(1);
      });
      $scope.forecast = data;
    });

  };
  $scope.getWeather();

    $scope.queryReg = {establecimiento: ServerData.establecimiento.id,ordering: 'id',page: 1};
    $scope.selectedReg = [];

    function successReg(registros) {
      $scope.registros = registros;
      console.log($scope.registros);
    }

    $scope.getReg = function () {
      $scope.promiseCat = Meteorologia.server.get($scope.queryCat,successReg).$promise;
      $scope.selectedReg = [];
    };

    $scope.getReg();


    $scope.deleteReg = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar_registro.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Meteorologia','$filter' ,function ($scope, $mdDialog, Meteorologia) {
          $scope.options = {
            pageSelect: true
          };
          $scope.logPagination = function (page, limit) {
            console.log('page: ', page);
            console.log('limit: ', limit);
          }

          $scope.query = {
            limit: 20,
            page: 1
          };
          $scope.lista = lista;
          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (lista.length >= 1){
                angular.forEach(lista, function(reg){
                  Meteorologia.server.delete({id:reg.id},reg,function(data){
                    console.log("Eliminado: " + data.fecha);
                  });
                });
              }
              $mdDialog.hide(lista);
            }else{
              $mdDialog.hide();
            }
          };

        }]
      })
        .then(function(lista) {
          if (lista !== true) {
            $scope.getReg();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.editReg = function(registroModificar) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_meteorologia.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','ServerData' ,function ($scope, $mdDialog, ServerData) {
          $scope.newRegistro = {};
          if (registroModificar) {
            $scope.newRegistro = registroModificar;
          }else{
            $scope.newRegistro.fecha = '';
            $scope.newRegistro.cantidad = 0;
            $scope.newRegistro.establecimiento = ServerData.establecimiento.id;
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (registroModificar){
                Meteorologia.server.update({id:$scope.newRegistro.id},$scope.newRegistro,function(data){
                  $scope.newRegistro = data;
                  $mdDialog.hide($scope.newRegistro);
                });

              }else {
                var nuevo = new Meteorologia.server($scope.newRegistro);

                nuevo.$save(function () {

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
          if (nuevo !== true) {
            var prueba = $filter('filter')($scope.registros.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.registros.results.unshift(nuevo);
              }
            }else{
              $scope.registros.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };


  });
