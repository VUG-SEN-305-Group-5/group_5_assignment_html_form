// Fill the state dropdown
var states = ["Abia","Adamawa","Akwa Ibom","Anambra","Bauchi","Bayelsa","Benue","Borno",
  "Cross River","Delta","Ebonyi","Edo","Ekiti","Enugu","FCT","Gombe","Imo","Jigawa",
  "Kaduna","Kano","Katsina","Kebbi","Kogi","Kwara","Lagos","Nasarawa","Niger","Ogun",
  "Ondo","Osun","Oyo","Plateau","Rivers","Sokoto","Taraba","Yobe","Zamfara"];

var stateSelect = document.getElementById("state");
states.forEach(function (s) {
  var opt = document.createElement("option");
  opt.textContent = s;
  stateSelect.appendChild(opt);
});

var form = document.getElementById("studentForm");
var message = document.getElementById("message");

form.addEventListener("submit", function (e) {
  e.preventDefault(); // stop page reload
  var data = new FormData(form);
  message.innerHTML = "<b>Form submitted:</b><br>" +
    "Name: " + data.get("fullname") + "<br>" +
    "Matric: " + data.get("matric") + "<br>" +
    "Email: " + data.get("email") + "<br>" +
    "Phone: " + data.get("phone") + "<br>" +
    "DOB: " + data.get("dob") + "<br>" +
    "Gender: " + data.get("gender") + "<br>" +
    "Department: " + data.get("department") + "<br>" +
    "Level: " + data.get("level") + "<br>" +
    "State: " + data.get("state") + "<br>" +
    "Address: " + data.get("address");
});

form.addEventListener("reset", function () {
  message.innerHTML = "";
});
