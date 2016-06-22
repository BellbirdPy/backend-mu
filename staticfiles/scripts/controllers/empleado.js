'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:EmpleadoCtrl
 * @description
 * # EmpleadoCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('EmpleadoCtrl', function ($scope,Empleado,Contratista,$mdDialog,$filter,ServerData,$http) {

    $scope.queryEmp = {establecimiento: ServerData.establecimiento.id,ordering: 'apellido',page: 1};
    $scope.selectedEmp = [];

    function successEmp(empleados) {
      $scope.empleados = empleados;
      console.log($scope.empleados);
    }

    $scope.getEmp = function () {
      $scope.promiseEmp = Empleado.get($scope.queryEmp,successEmp).$promise;
      $scope.selectedEmp = [];
    };

    $scope.getEmp();


    $scope.deleteEmp = function(lista) {
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar_empleado.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Empleado','$filter' ,function ($scope, $mdDialog, Empleado) {
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
                angular.forEach(lista, function(cat){
                  Empleado.delete({id:cat.id},cat,function(data){
                    console.log("Eliminado: " + data.nombre);
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
            $scope.getEmp();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.editEmp = function(empleadoModificar) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_empleado.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Raza','ServerData','$http' ,function ($scope, $mdDialog, Raza, ServerData,$http) {
          $scope.newEmpleado = {};
          if (empleadoModificar) {
            $scope.newEmpleado = empleadoModificar;
            $scope.newEmpleado.fecha_nacimiento = new Date(empleadoModificar.fecha_nacimiento);
            $scope.newEmpleado.ingreso_empresa = new Date(empleadoModificar.ingreso_empresa);
          }else{
            $scope.newEmpleado.establecimiento = ServerData.establecimiento.id;
          }


          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (empleadoModificar){
                Empleado.update({id:$scope.newEmpleado.id},$scope.newEmpleado,function(data){
                  $scope.newEmpleado = data;
                  $mdDialog.hide($scope.newEmpleado);
                });

              }else {
                var nuevo = new Empleado($scope.newEmpleado);

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
            var prueba = $filter('filter')($scope.empleados.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.empleados.results.unshift(nuevo);
              }
            }else{
              $scope.empleados.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };


    //CONTRATISTA
    $scope.queryCon = {establecimiento: ServerData.establecimiento.id,ordering: 'id',page: 1};
    $scope.selectedCon = [];

    function successCon(contratistas) {
      $scope.contratistas = contratistas;
      console.log($scope.contratistas);
    }

    $scope.getCon = function () {
      $scope.promiseCon = Contratista.get($scope.queryCon,successCon).$promise;
      $scope.selectedCon = [];
    };

    $scope.getCon();


    $scope.deleteCon = function(lista) {
      console.log(lista);
      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_eliminar_contratista.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Contratista','$filter' ,function ($scope, $mdDialog, Contratista) {
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
                angular.forEach(lista, function(cat){
                  Contratista.delete({id:cat.id},cat,function(data){
                    console.log("Eliminado: " + data.nombre);
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
            $scope.getCon();
          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };

    $scope.editCon = function(contratistaModificar) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_contratista.html',
        targetEvent: null,
        controller: ['$scope','$mdDialog','Contratista','ServerData' ,function ($scope, $mdDialog, Contratista, ServerData) {
          $scope.newContratista = {};
          if (contratistaModificar) {
            $scope.newContratista = contratistaModificar;
            $scope.newContratista.fecha_nacimiento = new Date(contratistaModificar.fecha_nacimiento);
          }else{
            $scope.newContratista.establecimiento = ServerData.establecimiento.id;
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };

          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (contratistaModificar){
                Contratista.update({id:$scope.newContratista.id},$scope.newContratista,function(data){
                  $scope.newContratista = data;
                  $mdDialog.hide($scope.newContratista);
                });

              }else {
                var nuevo = new Contratista($scope.newContratista);

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
            var prueba = $filter('filter')($scope.contratistas.results, function (d) {return d.id.toString() === nuevo.id.toString();})[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.contratistas.results.unshift(nuevo);
              }
            }else{
              $scope.contratistas.results.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };



  });
