/*
file		: 	validate_fields.js
date		:  	2014-1101
description	:   functions to validate fields in web site forms.
*/


// split input utility function
function split_input(input, delimeter) {
	
	var str = input;
	var array = str.split(delimeter);
	
	return array;
}

// validate name field, simple presence validation
function validate_field(field) {
	
	// note that the '||' below is not that good here... consider changing.
	if (field == "") {
		return "Please fill out all fields in form.\n";
	}
	
	return "";
}

// validate name field, simple presence validation
// TODO: we need to come up with sensible word validation
function validate_name(field) {
	
	if (field == "") {
		return "Please enter a word.\n";
	}
	
	return "";
}