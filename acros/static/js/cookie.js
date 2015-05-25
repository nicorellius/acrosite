// cookie.js for holding cookie set and get functions

function setCookie(name, value, days, path) {

    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = '; expires=' + date.toTimeString();
    }

    else {
        expires = '';
    }

    if (!path) {
        path = window.location.pathname;
    }

    document.cookie = name + '=' + value + expires + '; path=' + path;
}

function getCookie(cname) {

    var name = cname + '=';
    var ca = document.cookie.split(';');

    for (var i=0; i<ca.length; i++) {

        var c = ca[i];

        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }

        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }

    //alert(c);
    return '';
}