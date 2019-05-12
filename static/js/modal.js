
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

var modals = document.getElementById('arend');

// Get the button that opens the modal
var btns = document.getElementById("myArend");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[1];

// When the user clicks on the button, open the modal 
btns.onclick = function() {
  modals.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modals.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modals) {
    modals.style.display = "none";
  }
};
var modalsp = document.getElementById('person');

// Get the button that opens the modal
var btnp = document.getElementById("person_btns");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[2];

// When the user clicks on the button, open the modal
btnp.onclick = function() {
  modalsp.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modalsp.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalsp) {
    modalsp.style.display = "none";
  }
};

var modalsoptom = document.getElementById('optom');

// Get the button that opens the modal
var btnoptom = document.getElementById("btn_optom");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[3];

// When the user clicks on the button, open the modal 
btnoptom.onclick = function() {
  modalsoptom.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modalsoptom.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalsoptom) {
    modalsoptom.style.display = "none";
  }
};
var modalekskursion = document.getElementById('ekskursion');

// Get the button that opens the modal
var btneks = document.getElementById("btn_eks");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[4];

// When the user clicks on the button, open the modal 
btneks.onclick = function() {
  modalekskursion.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modalekskursion.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modalekskursion) {
    modalekskursion.style.display = "none";
  }
};


