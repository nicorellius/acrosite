/*
file		: 	validate_forms.js
date		:  	2014-1101
description	:   functions to validate forms in web pages.
*/

function validate_form(form) {
	
	var fields = [];
	
	for (i = 0; i < field.length(); i++) {
		field =  validate_field(form.fields[i].value);
	}
	

	if (field == "") {
		return true;
	}
	
	else {
		$("#loading-spinner").hide();
		alert("You must enter required fields in the form. Thanks!");
		return false;
	}
}

function validate_generate_acrostic_form(form) {
	
	var name = validate_name(form.name.value);

	if (name == "") {
		return true;
	}
	
	else {
		$("#loading-spinner").hide();
		alert("You must enter required fields in the form. Thanks!");
		return false;
	}
}