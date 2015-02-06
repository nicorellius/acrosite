// ajax.js for holding ajax js scripts

// re-generate ecrostic script on button click
$(document).ready(function() {
    $(".redo").click(function(e) {

        e.preventDefault();

		$('#loading-spinner').show();
		
		var id = $(this).attr('id');

        //var date = new Date();
		//var date_time = date.toLocaleString();
		//var month = get_month();
		//var date_time = date.getFullYear() + '-' + month + '-' + date.getDate() + ' ' + date.toTimeString();

        var date_time = get_timestamp();

        // pushState()
        var stateObj = { foo: "bar" };
        history.pushState(stateObj, "page 2", "bar.html");


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
                    console.log(response);
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

//<div id="products">
//   <div style="float:right; width:350px; border:1px solid #ccc; padding:1em;">
//     <strong>Server response:</strong>
//     <ul id="response">
//
//     </ul>
//     </div>
//     <ul>
//         <li><h4>Product X (id: 312)</h4>
//         RateIt: <div data-productid="312" class="rateit"></div>
//         </li>
//         <li><h4>Product Y (id: 423)</h4>
//         RateIt: <div data-productid="423" class="rateit"></div></li>
//         <li><h4>Product Z (id: 653)</h4>
//         RateIt: <div data-productid="653" class="rateit"></div>
//         </li>
//     </ul>
//
// </div>

// rateit ajax script
// we bind only to the rateit controls
 $('.rateit').bind('click', function(e) {

     e.preventDefault();

     var date_time = get_timestamp();
     var ri = $(this);
     var value = ri.rateit('value');
     var acrostic_id = ri.data('acrostic_id');

     $.ajax({
         url: '/acrostic/rate/', // TODO - need to write view and urls for capturing star data
         data: {
             acrostic_id: acrostic_id,
             value: value
         },
         type: 'post',
         success: function(data, response) {
             console.log(date_time + ": " + "ajax call succeeded!");
             console.log(data);
             console.log(response);
         },
         error: function(data, response) {
             console.log(date_time + ": " + "ajax call failed!");
             console.log(data);
             console.log(response);
         }
     });
 });