$('#textarea1').val('New Text');
$('#textarea1').trigger('autoresize');


$('.timepicker').pickatime({
    default: 'now', // Set default time: 'now', '1:30AM', '16:30'
    format: "HH:ii:SS",
    fromnow: 0,       // set default time to * milliseconds from now (using with default = 'now')
    twelvehour: false, // Use AM/PM or 24-hour format
    donetext: 'OK', // text for done-button
    cleartext: 'Clear', // text for clear-button
    canceltext: 'Cancel', // Text for cancel-button
    autoclose: false, // automatic close timepicker
    ampmclickable: true, // make AM PM clickable
    aftershow: function(){} //Function for after opening timepicker
});

$('.datepicker').pickadate({
	format: 'dd/mm/yyyy',  
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
	});

	$(document).ready(function() {
	$('select').material_select();
});