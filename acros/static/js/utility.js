// utility.js for holding misc js scripts

// jquery ready function
//$(document).ready(function() {});

$('#loading-spinner').hide();

// get month function
function get_month() {
	
	var date = new Date();
	
	month = date.getMonth();
	month = month + 1;
	
	if (month < 10) {
		month = '0' + month;
	}
	
	return month;
}

$('#gen-acrostic-btn').click(function() {
	$('#loading-spinner').show();
	alert("no backend hooked up yet...");
	$('#loading-spinner').hide();
});

// loading spinner script
$('.spinner').click(function() {
	$('#loading-spinner').show();
});

$(document).ajaxComplete(function() {
    $('#loading').hide();
});

// back to top widget
$(document).ready(function() {
    
    $('.back-to-top').hide();
    
    var offset = 220;
    var duration = 500;
    var $root = $('html, body');
    
    $(window).scroll(function() {
        
		if ($(this).scrollTop() > offset) {
            $('.back-to-top').fadeIn(duration);
        }
        
        else {
            $('.back-to-top').fadeOut(duration);
        }
    });
    
    $('.back-to-top').click(function(event) {
        
		event.preventDefault();
        $($root).animate({ scrollTop: 0 }, duration);
        return false;
    })
    
    $('.back-to-top').click(function() {
        
		var href = $.attr(this, 'href');
        
		$root.animate({
            scrollTop: $(href).offset.top
        }, 500, function () {
            window.location.hash = href;
        });
        
		return false;
    })
});

// tooltip widget
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});

// bootstrap select plugin
$(document).ready(function () {
    $('.bootstrap-select').selectpicker();
});