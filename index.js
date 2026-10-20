document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let name = document.getElementById("name").value;

    if (name.trim() === "") {
        alert("Please enter your name");
    } else {
        alert("Form submitted successfully!");
    }
});