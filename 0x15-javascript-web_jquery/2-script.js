/*
 a JavaScript script that updates the text color of
 the <header> element to red (#FF0000) when the user
 clicks on the tag DIV#red_header
 */

function changeColor () {
  $('DIV#red_header').css('color', '#FF0000');
}

$('DIV#red_header').on('click', changeColor);
