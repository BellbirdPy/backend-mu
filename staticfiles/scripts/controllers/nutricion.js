'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:NutricionCtrl
 * @description
 * # NutricionCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('NutricionCtrl', function ($scope,$mdDialog,Nutricion,$filter,ServerData,Lote) {

    $scope.queryLotes = {establecimiento: ServerData.establecimiento.id,ordering: 'nombre',page: 1};

      function successLotes(lotes) {
        $scope.lotes = lotes;
      }

  $scope.getLotes = function () {
    $scope.promiseLotes = Lote.get($scope.queryLotes,successLotes).$promise;
  };

  $scope.getLotes();

    $scope.queryDietas = {establecimiento: ServerData.establecimiento.id,ordering: 'fecha_inicio',page: 1};
    $scope.selectedDietas = [];

  function successDietas(dietas) {
    $scope.dietas = dietas;
  }

  $scope.getDietas = function () {
  if ($scope.queryDietas.lotes){
    if ($scope.queryDietas.lotes.toString() === 'todos'){
        delete $scope.queryDietas["lotes"];
    }
    }

    $scope.promiseDietas = Nutricion.get($scope.queryDietas,successDietas).$promise;
    $scope.selectedDietas = [];
  };

  $scope.getDietas();

    $scope.deleteDieta = function(ev) {
      // Appending dialog to document.body to cover sidenav in docs app
      console.log(ev);
      var confirm = $mdDialog.confirm()
        .title('Estas seguro de que quieres eliminar?')
        .content('Tipo: '+ev.tipo_nutricion + '<br>' +
        'Tipo de alimento: ' + ev.tipo_comida + '<br>' +
        'Periodo: ' + $filter('date')(new Date(ev.fecha_inicio), "dd/MM/yyyy")   + ' - '+ $filter('date')(new Date(ev.fecha_fin), "dd/MM/yyyy") + '<br>' )
        .ariaLabel('Delete potrero')
        .targetEvent(null)
        .ok('Sí, estoy seguro')
        .cancel('Cancelar');
      $mdDialog.show(confirm).then(function() {
        Nutricion.delete({id:ev.id},ev,function(data){
          console.log(data);
          $scope.dietas.results.splice($scope.dietas.results.indexOf(ev),1);
          $scope.selectedDietas = [];
        });
      }, function() {
        $scope.status = 'Se eliminó correctamente.';

      });
    };


    $scope.editDieta = function(nutricion_modificar) {

      $mdDialog.show({
        templateUrl: '/staticfiles/views/dialogs/dialogo_nutricion.html',
        targetEvent: nutricion_modificar,
        controller: ['$scope','$mdDialog','Nutricion','Lote','ServerData' ,function ($scope, $mdDialog, Nutricion,Lote,ServerData) {
          var _MS_PER_DAY = 1000 * 60 * 60 * 24;

// a and b are javascript Date objects
          function dateDiffInDays(a, b) {
            // Discard the time and time-zone information.
            var utc1 = Date.UTC(a.getFullYear(), a.getMonth(), a.getDate());
            var utc2 = Date.UTC(b.getFullYear(), b.getMonth(), b.getDate());

            return Math.floor((utc2 - utc1) / _MS_PER_DAY);
          }
          $scope.form = {};

          $scope.calculo_kilos = function(cantidad){
            var result = dateDiffInDays($scope.newNutricion.fecha_inicio,$scope.newNutricion.fecha_fin);
            console.log(result);
            if (cantidad == $scope.form.gramos){
              $scope.form.kilos = cantidad * result /1000;
            }else{
              $scope.form.gramos = cantidad / result *1000;
            }
          };

          $scope.lotes = [];
          Lote.get({establecimiento:ServerData.establecimiento.id},function(response) {
            $scope.lotes = response.results;
          });



          $scope.alimentos = ['Sal mineral','Balanceado','Pastura','Núcleo','Otros'];

          $scope.newNutricion = {};
          if (nutricion_modificar) {
            $scope.newNutricion = nutricion_modificar;
            $scope.newNutricion.fecha_inicio = new Date(nutricion_modificar.fecha_inicio);
            $scope.newNutricion.fecha_fin = new Date(nutricion_modificar.fecha_fin);
            console.log($scope.alimentos.indexOf($scope.newNutricion.tipo_comida));
            if ($scope.alimentos.indexOf($scope.newNutricion.tipo_comida) == -1 ){
              $scope.form.tipo_comida = $scope.newNutricion.tipo_comida;
              $scope.newNutricion.tipo_comida = 'Otros';
            }
            $scope.form.kilos = $scope.newNutricion.kilos;
            $scope.calculo_kilos($scope.newNutricion.kilos);
          }

          $scope.hide = function () {
            $mdDialog.hide();
          };

          $scope.cancel = function () {
            $mdDialog.cancel();
          };



          $scope.answer = function (answer) {
            if (answer === 'guardar'){
              if (nutricion_modificar){
                if ($scope.newNutricion.tipo_comida == 'Otros'){
                  $scope.newNutricion.tipo_comida = $scope.form.tipo_comida;
                }
                $scope.newNutricion.kilos = $scope.form.kilos;

                Nutricion.update({id:$scope.newNutricion.id},$scope.newNutricion,function(data){
                  $scope.newNutricion = data;
                  $mdDialog.hide($scope.newNutricion);
                });

              }else {
                var nuevo = new Nutricion($scope.newNutricion);
                if (nuevo.tipo_comida == 'Otros'){
                  nuevo.tipo_comida = $scope.form.tipo_comida;
                }
                nuevo.kilos = $scope.form.kilos;
                console.log(nuevo);
                nuevo.establecimiento = ServerData.establecimiento.id;

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
            var prueba = $filter('filter')($scope.dietas, { id: nuevo.id }, true)[0];
            if (prueba){
              if (prueba.id === nuevo.id) {
                angular.extend(prueba, nuevo);
              }else{
                $scope.dietas.unshift(nuevo);
              }
            }else{
              $scope.dietas.unshift(nuevo);
            }

          }
        }, function() {
          $scope.alert = 'You cancelled the dialog.';
        });
    };
  });
