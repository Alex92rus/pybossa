/**
 * Created by alex on 11/8/16.
 */

(function(pybossaapi, $, undefined) {
    var url =  '/'

    pybossaapi.getTaskRuns = function (userId) {
        console.log(userId);
        return $.ajax({
            url: url + 'api/taskrun',
            data: 'all=1&user_id=' + userId,
            cache: true,
            dataType: 'json',
            contentType: 'application/json'
        }).done( function(response) {
            response = response.responseJSON;
        });
    }

} (window.pybossaapi = window.pybossaapi || {}, jQuery));