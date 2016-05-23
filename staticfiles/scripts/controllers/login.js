'use strict';

/**
 * @ngdoc function
 * @name frontendmuApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the frontendmuApp
 */
angular.module('frontendmuApp')
  .controller('LoginCtrl', function ($scope, $location, DjangoAuth, Validate) {
    if (DjangoAuth.authenticated){
      $location.path("/");
    }
    $scope.model = {'username':'','password':''};
    $scope.complete = false;
    $scope.login = function(formData){
      $scope.errors = [];
      Validate.form_validation(formData,$scope.errors);
      if(!formData.$invalid){
        DjangoAuth.login($scope.model.username, $scope.model.password)
          .then(function(data){
            // success case
            $location.path("/");
          },function(data){
            // error case
            $scope.errors = data;
          });
      }
    }
  });
