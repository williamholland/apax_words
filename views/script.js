function copyTextArea() {
  /* Get the text field */

  var copyText = document.getElementById("wordListTextArea");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");

  return false;
} 
