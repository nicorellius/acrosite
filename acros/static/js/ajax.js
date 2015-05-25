// ajax.js for holding ajax js scripts

setCookie('lockvote', 'false');

alert(getCookie('lockvote'));
var lock = document.getElementById('lock-vote');

if (getCookie('lockvote') == 'true') {
    $('rateit').rateit('readonly', true);
    lock.disabled = true;
}

// re-generate ecrostic script on button click
$(document).ready(function() {

    $(".redo").click(function(e) {

        e.preventDefault();

        var $ls = $('#loading-spinner');
		$ls.show();
		
		var id = $(this).attr('id');

        var date_time = get_timestamp();

        var name = $.QueryString['name'];
        var theme = $.QueryString['theme'];
        var ecrostic = $.QueryString['ecrostic'];

        console.log(date_time + ": " + 'name: ' + name + '; theme: ' + theme + '; ecrostic: ' + ecrostic);

		if ($(this).attr('data-target') == 'acrostic_id') {

            // TODO - sort this out. this works only because I'm pushing an URL without the ecrostic
            // TODO - need to figure out how to get that damn ecrostic into this script.
            // var acros = $('#get-acrostic').text();
            // pushState()
            var stateObj = {acrostic: 'acrostic'};
            history.pushState(stateObj, '', '?name=' + name + '&theme=' + theme);

			$.ajax({
				type: 'post',
				url: '/generate/?xhr',
				data: {
                    name: name,
                    theme: theme
                },
				success: function(data, response) {
					console.log(date_time + ": " + "ajax call succeeded!");
                    //console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
                    location.reload();
                    //window.history.pushState(
                    //    "object or string",
                    //    "Title",
                    //    "/generate/acrostic/?name=" + name + "&theme=" + theme + "&ecrostic=" + ecrostic
                    //);
                    var lock = document.getElementById('lock-vote');
                    lock.disabled = false;
                    setCookie('lockvote', 'false');
				},
				error: function(data, response) {
                    console.log(date_time + ": " + "ajax call failed!");
                    console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
				}
			});
		}
		
		else {
			console.log(date_time + ": " + "user canceled delete operation...");
			$ls.hide();
		}
    });
});

// Add event listener
// When button clicked, set `click` cookie to true
// and disable button
//button.addEventListener('click', function() {
//    setCookie('lockvote', 'true');
//    button.disabled = true;
//}, false);

// rateit ajax script
$(document).ready(function() {

    $(lock).bind('click', function(e) {

        e.preventDefault();

        var $ri = $('.rateit');
        var date_time = get_timestamp();
        var value = $ri.rateit('value');
        var acrostic_id = $ri.data('acrostic_id');

        $.ajax({
            url: '/acrostic/rate/?xhr',
            data: {
                acrostic_id: acrostic_id,
                value: value
            },
            type: 'post',
            success: function(data, response) {
                console.log(date_time + ": " + "ajax call succeeded!");
                console.log(date_time + ": " + "ajax data: " + JSON.stringify(data));
                console.log(date_time + ": " + "ajax response: " + response);
                $ri.rateit('readonly', true);
                $(lock).unbind('mouseenter mouseleave').off('click').attr('disabled', false);
                setCookie('lockvote', 'true');
                var $avg = $('#average');
                var $tot = $('#total');
                $avg.html('');
                $tot.html('');
                $avg.append('('+ data['average'] + ')');
                $tot.append(data['total']);
            },
            error: function(data, response) {
                console.log(date_time + ": " + "ajax call failed!");
                //console.log(date_time + ": " + "ajax data: " + JSON.stringify(data));
                console.log(date_time + ": " + "ajax response: " + response);
            }
        });
    });
});
