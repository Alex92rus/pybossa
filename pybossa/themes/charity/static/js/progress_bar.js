// To remove start
$(function() {
	$('#rightsidebar').stop().animate({'margin-right':'-200px'},1000);

    function toggleDivs() {
        var $inner = $("#rightsidebar");
        if ($inner.css("margin-right") == "-200px") {
            $inner.animate({'margin-right': '-30'});
            $(".nav-btn").html('<i class="fa fa-caret-square-o-left fa-fw fa-4x"></i>')
        }
        else {
            $inner.animate({'margin-right': "-200px"});
            $(".nav-btn").html('<i class="fa fa-caret-square-o-right fa-fw fa-4x"></i>')
        }
    }

    $(".nav-btn").bind("click", function(){
        console.log('log')
        toggleDivs();
    });

});
// To remove end
var progressBar = {
    tokenValue: 5
};