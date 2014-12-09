// ajax.js for holding ajax js scripts
$(document).ready(function() {
    $(".redo").click(function() {

		$('#loading-spinner').show();
		
		var id = $(this).attr('id');
		var date = new Date();
		var date_time = date.toLocaleString();
		
		var month = get_month();
		var date_time = date.getFullYear() + '-' + month + '-' + date.getDate() + ' ' + date.toTimeString();
		
		if ($(this).attr('data-target') == 'acrostic_id') {
			$.ajax({
				type: 'post',
				url: '/admin/generator/acrostic/delete/' + id + '/',
				data: id,
				success: function(response) {
					//alert('Document deleted successfully');
					console.log(date_time + ": " + response);
					location.reload();
				},
				error: function(response) {
					console.log(date_time + ": " + "ajax call failed!");
				},
			});
		}
		
		else {
			console.log(date_time + ": " + 'user canceled delete operation...');
			$('#loading-spinner').hide();
			return;
		}
		
        
    });
});