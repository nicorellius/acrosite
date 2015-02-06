// ajax.js for holding ajax js scripts
$(document).ready(function() {
    $(".redo").click(function(e) {

        e.preventDefault();

		$('#loading-spinner').show();
		
		var id = $(this).attr('id');

        var date = new Date();
		var date_time = date.toLocaleString();
		var month = get_month();
		var date_time = date.getFullYear() + '-' + month + '-' + date.getDate() + ' ' + date.toTimeString();

        var name = $.QueryString['name'];
        var theme = $.QueryString['theme'];
        var ecrostic = $.QueryString['ecrostic'];

        console.log(date_time + ": " + 'name: ' + name + '; theme: ' + theme + '; ecrostic: ' + ecrostic);

		if ($(this).attr('data-target') == 'acrostic_id') {
			$.ajax({
				type: 'post',
				url: '/generate/',
				data: {
                    name: name,
                    theme: theme
                },
				success: function(response) {
					console.log(date_time + ": " + "ajax call succeeded!");
                    //location.replace('/generate/acrostic/?name=' + name + '&theme=' + theme + '&ecrostic=' + ecrostic);
                    location.reload();
				},
				error: function(response) {
					console.log(date_time + ": " + "ajax call failed!");
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