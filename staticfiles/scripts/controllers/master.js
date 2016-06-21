'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MasterCtrl
 * @description
 * # MasterCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MasterCtrl', function ($scope, $location, ServerData, Establecimiento,Menu,$rootScope,$timeout,$mdSidenav) {
    var menu = Menu;
    var vm = this;
    $scope.toggleLeft = buildDelayedToggler('left');
    function debounce(func, wait, context) {
      var timer;
      return function debounced() {
        var context = $scope,
          args = Array.prototype.slice.call(arguments);
        $timeout.cancel(timer);
        timer = $timeout(function() {
          timer = undefined;
          func.apply(context, args);
        }, wait || 10);
      };
    }
    /**
     * Build handler to open/close a SideNav; when animation finishes
     * report completion in console
     */
    function buildDelayedToggler(navID) {
      return debounce(function() {
        // Component lookup should always be available since we are not using `ng-if`
        $mdSidenav(navID)
          .toggle()
          .then(function () {
            $log.debug("toggle " + navID + " is done");
          });
      }, 200);
    }

    $scope.establecimientos = [];
    $scope.obj = ServerData;

    Establecimiento.get(function (data) {
      $scope.establecimientos = data.results;
    });

    $scope.seleccionar = function(e){
      $scope.obj.establecimiento = e;
      $rootScope.establecimiento = e;
      $location.path('/inventario/');
    };


    //functions for menu-link and menu-toggle
    vm.isOpen = isOpen;
    vm.toggleOpen = toggleOpen;
    vm.autoFocusContent = false;
    vm.menu = menu;

    vm.status = {
      isFirstOpen: true,
      isFirstDisabled: false
    };
    function isOpen(section) {
      return menu.isSectionSelected(section);
    }
    function toggleOpen(section) {
      menu.toggleSelectSection(section);
    }
    $scope.vm = vm;
  });
