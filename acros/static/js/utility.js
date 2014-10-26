// utility.js for holding misc js scripts

// jquery ready function
//$(document).ready(function() {});

function get_month() {
	
	var date = new Date();
	
	month = date.getMonth();
	month = month + 1;
	
	if (month < 10) {
		month = '0' + month;
	}
	
	return month;
}

// loading spinner script
$('a.spinner, button.spinner').click(function() {
	$('#loading').show();
});

$(document).ajaxComplete(function() {
    $('#loading').hide();
});

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
    
    $('a').click(function() {
        
		var href = $.attr(this, 'href');
        
		$root.animate({
            scrollTop: $(href).offset.top
        }, 500, function () {
            window.location.hash = href;
        });
        
		return false;
    })
});

$(document).ready(function() {
	
	$("#menu-button").click(function () {
		$("#main-nav").toggle(1000);
	});
});

$(document).ready(function () {
	
	var $window = $(window), $nav = $('nav');
	
	$window.on('resize', function () {
		
		if ($window.width() > 767) {
		    
			$nav.show();
			$("#main-nav").removeAttr('style');
        }
    });
});

$(document).ready(function() {
    
	$(".rslides").responsiveSlides({
        pager: true,
        speed: 1000,
        timeout: 5000,
        namespace: "centered-btns",
    });
});

//$(document).ready(function() {
//	$('#delete-document').click(function() {
//		alert("Are you sure you want to delete this document?");
//	});
//});

//function delete_alert(message, cb) {
//    alert(message); // log to the console of recent Browsers
//    cb();
//}
//
//$(document).ready(function() {
//	$('#').click(function() {
//		delete_alert("You are about to delete this document. Select 'No' on the next page if you wish to cancel.", function() {
//			$('#loading').show();
//		});
//	});
//});


$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});



// responsive slider docs
//auto: true,             // Boolean: Animate automatically, true or false
//speed: 500,             // Integer: Speed of the transition, in milliseconds
//timeout: 4000,          // Integer: Time between slide transitions, in milliseconds
//pager: false,           // Boolean: Show pager, true or false
//nav: false,             // Boolean: Show navigation, true or false
//random: false,          // Boolean: Randomize the order of the slides, true or false
//pause: false,           // Boolean: Pause on hover, true or false
//pauseControls: true,    // Boolean: Pause when hovering controls, true or false
//prevText: "Previous",   // String: Text for the "previous" button
//nextText: "Next",       // String: Text for the "next" button
//maxwidth: "",           // Integer: Max-width of the slideshow, in pixels
//navContainer: "",       // Selector: Where controls should be appended to, default is after the 'ul'
//manualControls: "",     // Selector: Declare custom pager navigation
//namespace: "rslides",   // String: Change the default namespace used
//before: function(){},   // Function: Before callback
//after: function(){}     // Function: After callback

// active tab script
//var url = window.location;
// Will only work if string in href matches with location
//$('ul.nav a[href="'+ url +'"]').parent().addClass('active');

// Will also work for relative and absolute hrefs
//$('ul.nav a').filter(function() {
    //return this.href == url;
//}).parent().addClass('active');