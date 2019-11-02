let app = angular.module("InputTextApp", [])

app.controller("InputTextController", ['$scope', '$http', function InputTextController($scope, $http) {

    $scope.input_text  = ""
    $scope.history     = []
    $scope.count       = 0

    $scope.submit = text => {
        return $http.post('submit', JSON.stringify({text: text}))
        .then(response => {
            let history = response.data.history
            $scope.count = history[history.length-1].count
            $scope.history = history
        })
    }

    // get history from server on page initialise
    (() => {
        $http.get('history')
            .then(response => {
                $scope.history = response.data.history
            })
    })()

}])