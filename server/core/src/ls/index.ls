angular.module \core, <[]>
  ..directive \loading, -> do
    restrict: \E
    template-url: '/s/core/loading.html'
    link: (scope, e, attrs, ctrl) ->
  ..controller \main, <[$scope $http]> ++ ($scope, $http) ->
    $scope.loading = true
    $http.get "/json/#{parse-int(1 + Math.random! * 1173)}/" .success (data) ->
      $scope.data = data
      $scope.loading = false
