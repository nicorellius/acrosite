// utility.js for holding misc js scripts

// jquery ready function
//$(d$(document).ready(function() {});

// hide things by default
$('#loading-spinner').hide();

$(document).ready(function() {
    $( ".show-admin" ).click(function() {
        $("#admin-access").toggle( "slow" );
    });
});


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

function get_timestamp() {

    var date = new Date();
	var date_time = date.toLocaleString();
	var month = get_month();
	var date_time = date.getFullYear() + '-' + month + '-' + date.getDate() + ' ' + date.toTimeString();

    return date_time;
}

// loading spinner script
$('.spinner').click(function() {
	$('#loading-spinner').show();
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

$(document).ready(function () {
    var name = $.QueryString['name'];
    var theme = $.QueryString['theme'];
    //var ecrostic = $.QueryString['ecrostic'];

    console.log(get_timestamp() + ": " + 'name: ' + name + '; theme: ' + theme); // + '; ecrostic: ' + ecrostic);

    //$('#theme-selector [value=" + value + "]').prop('selected', true)
});

// http://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
(function($) {
    $.QueryString = (function(a) {
        if (a == "") return {};
        var b = {};
        for (var i = 0; i < a.length; ++i)
        {
            var p=a[i].split('=');
            if (p.length != 2) continue;
            b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
        }
        return b;
    })(window.location.search.substr(1).split('&'))
})(jQuery);

// http://stackoverflow.com/questions/901115/how-can-i-get-query-string-values-in-javascript
function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}