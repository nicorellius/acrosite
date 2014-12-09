// using jQuery, fetch csrf cookie token
function getCookie(name) {
    
    var cookieValue = null;
    
    if (document.cookie && document.cookie != '') {
        
        var cookies = document.cookie.split(';');
        
        for (var i = 0; i < cookies.length; i++) {
            
            var cookie = jQuery.trim(cookies[i]);
            
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    
    return cookieValue;
}

function csrf_safe_method(method) {
    
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    
    crossDomain: false,
    beforeSend: function(xhr, settings) {
        
        if (!csrf_safe_method(settings.type)) {
            
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

