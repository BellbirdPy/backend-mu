'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:MasterCtrl
 * @description
 * # MasterCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('MasterCtrl', function ($scope, $location, ServerData, Establecimiento,Menu,$rootScope) {
    var menu = Menu;
    var vm = this;
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
