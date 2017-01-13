/**
 * Created by alex on 11/8/16.
 */
(function(pybossaapi, $, undefined) {
    var url =  '/'

    pybossaapi.getTaskRuns = function (userId, limit) {
        console.log(userId);
        userIdParam = 'user_id=' + userId;
        allParam = 'all=1';
        limitParam = 'limit=' + limit;
        requestData = allParam + '&' + userIdParam + '&' + limitParam;
        console.log(requestData);
        return $.ajax({
            url: url + 'api/taskrun',
            data: requestData,
            cache: true,
            dataType: 'json',
            contentType: 'application/json'
        }).done( function(response) {
            response = response.responseJSON;
        });
    }

} (window.pybossaapi = window.pybossaapi || {}, jQuery));