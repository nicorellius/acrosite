// ajax.js for holding ajax js scripts

// re-generate ecrostic script on button click
$(document).ready(function() {
    $(".redo").click(function(e) {

        e.preventDefault();

		$('#loading-spinner').show();
		
		var id = $(this).attr('id');

        var date_time = get_timestamp();

        var name = $.QueryString['name'];
        var theme = $.QueryString['theme'];
        var ecrostic = $.QueryString['ecrostic'];

        // pushState()
        //var stateObj = { acrostic: 'acrostic' };
        //history.pushState(stateObj, "page 2", '/generate/acrostic/');

        console.log(date_time + ": " + 'name: ' + name + '; theme: ' + theme + '; ecrostic: ' + ecrostic);

		if ($(this).attr('data-target') == 'acrostic_id') {
			$.ajax({
				type: 'post',
				url: '/generate/',
				data: {
                    name: name,
                    theme: theme
                },
				success: function(data, response) {
					console.log(date_time + ": " + "ajax call succeeded!");
                    //location.replace('/generate/acrostic/?name=' + name + '&theme=' + theme + '&ecrostic=' + ecrostic);
                    //console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
                    location.reload();
				},
				error: function(data, response) {
                    console.log(date_time + ": " + "ajax call failed!");
                    console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
				}
			});
		}
		
		else {
			console.log(date_time + ": " + 'user canceled delete operation...');
			$('#loading-spinner').hide();
			return;
		}
		
        
    });
    
    $(".new-word").click(function(e) {

        e.preventDefault();

		$('#loading-spinner').show();
		
		var id = $(this).attr('id');

        var date_time = get_timestamp();

        var name = $.QueryString['name'];
        var theme = $.QueryString['theme'];
        var ecrostic = $.QueryString['ecrostic'];

        // pushState()
        //var stateObj = { acrostic: 'acrostic' };
        //history.pushState(stateObj, "page 2", '/generate/acrostic/');

        console.log(date_time + ": " + 'name: ' + name + '; theme: ' + theme + '; ecrostic: ' + ecrostic);

		if ($(this).attr('data-target') == 'acrostic_id') {
			$.ajax({
				type: 'post',
				url: '/generate/',
				data: {
                    name: 'secret-code:new-word',
                    theme: theme
                },
				success: function(data, response) {
					console.log(date_time + ": " + "ajax call succeeded!");
                    //location.replace('/generate/acrostic/?name=' + name + '&theme=' + theme + '&ecrostic=' + ecrostic);
                    //console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
                    location.reload();
				},
				error: function(data, response) {
                    console.log(date_time + ": " + "ajax call failed!");
                    console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
				}
			});
		}
		
		else {
			console.log(date_time + ": " + 'user canceled delete operation...');
			$('#loading-spinner').hide();
			return;
		}
		
        
    });
    
    $(".new-theme").click(function(e) {

        e.preventDefault();

		$('#loading-spinner').show();
		
		var id = $(this).attr('id');

        var date_time = get_timestamp();

        var name = $.QueryString['name'];
        var theme = $.QueryString['theme'];
        var ecrostic = $.QueryString['ecrostic'];

        // pushState()
        //var stateObj = { acrostic: 'acrostic' };
        //history.pushState(stateObj, "page 2", '/generate/acrostic/');

        console.log(date_time + ": " + 'name: ' + name + '; theme: ' + theme + '; ecrostic: ' + ecrostic);

		if ($(this).attr('data-target') == 'acrostic_id') {
			$.ajax({
				type: 'post',
				url: '/generate/',
				data: {
                    name: 'secret-code:new-word',
                    theme: 'new-theme'
                },
				success: function(data, response) {
					console.log(date_time + ": " + "ajax call succeeded!");
                    //location.replace('/generate/acrostic/?name=' + name + '&theme=' + theme + '&ecrostic=' + ecrostic);
                    //console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
                    location.reload();
				},
				error: function(data, response) {
                    console.log(date_time + ": " + "ajax call failed!");
                    console.log(date_time + ": " + "ajax data: " + data);
                    console.log(date_time + ": " + "ajax response: " + response);
				}
			});
		}
		
		else {
			console.log(date_time + ": " + 'user canceled delete operation...');
			$('#loading-spinner').hide();
			return;
		}
		
        
    });
});

// rateit ajax script
 $('.rateit').bind('click', function(e) {

     e.preventDefault();

     // TODO - move this below to success if necessary
     //$('.rateit').attr('data-rateit-readonly', 'true');

     var date_time = get_timestamp();
     var ri = $(this);
     var value = ri.rateit('value');
     var acrostic_id = ri.data('acrostic_id');

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
             var $a = '#average';
             var $t = '#total';
             // TODO - figure out how to lock score after one vote
             $($a).html('');
             $($t).html('');
             $($a).append('('+ data['average'] + ')');
             $($t).append(data['total']);
         },
         error: function(data, response) {
             console.log(date_time + ": " + "ajax call failed!");
             //console.log(date_time + ": " + "ajax data: " + JSON.stringify(data));
             console.log(date_time + ": " + "ajax response: " + response);
         }
     });
 });