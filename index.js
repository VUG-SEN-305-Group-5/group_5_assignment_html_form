const form = document.getElementById("biodataForm");
const successBox = document.getElementById("successBox");

function showError(input, message) {
    input.classList.add("invalid");
    const errorText = input.parentElement.querySelector(".error");
    errorText.textContent = message;
}

function clearError(input) {
    input.classList.remove("invalid");
    const errorText = input.parentElement.querySelector(".error");
    errorText.textContent = "";
}

function validateForm() {
    let isValid = true;

    const fullName = document.getElementById("fullName");
    const matricNo = document.getElementById("matricNo");
    const email = document.getElementById("email");
    const phone = document.getElementById("phone");
    const dob = document.getElementById("dob");
    const department = document.getElementById("department");
    const level = document.getElementById("level");
    const stateOfOrigin = document.getElementById("stateOfOrigin");
    const genderGroup = document.getElementById("genderGroup");

    // full name - at least two names
    if (fullName.value.trim() === "") {
        showError(fullName, "Full name is required");
        isValid = false;
    } else if (fullName.value.trim().split(" ").length < 2) {
        showError(fullName, "Enter at least your surname and first name");
        isValid = false;
    } else {
        clearError(fullName);
    }

    const matricPattern = /^[A-Z]{3}\/[A-Z]{3}\/\d{2}\/\d{4,6}$/i;
    if (matricNo.value.trim() === "") {
        showError(matricNo, "Matric number is required");
        isValid = false;
    } else if (!matricPattern.test(matricNo.value.trim())) {
        showError(matricNo, "Use the format VUG/SEN/24/11362");
        isValid = false;
    } else {
        clearError(matricNo);
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email.value.trim() === "") {
        showError(email, "Email is required");
        isValid = false;
    } else if (!emailPattern.test(email.value.trim())) {
        showError(email, "Enter a valid email address");
        isValid = false;
    } else {
        clearError(email);
    }

    const phonePattern = /^0\d{10}$/;
    if (phone.value.trim() === "") {
        showError(phone, "Phone number is required");
        isValid = false;
    } else if (!phonePattern.test(phone.value.trim())) {
        showError(phone, "Phone number must be 11 digits starting with 0");
        isValid = false;
    } else {
        clearError(phone);
    }

    if (dob.value === "") {
        showError(dob, "Date of birth is required");
        isValid = false;
    } else {
        const birthYear = new Date(dob.value).getFullYear();
        const currentYear = new Date().getFullYear();
        if (currentYear - birthYear < 15) {
            showError(dob, "You must be at least 15 years old");
            isValid = false;
        } else {
            clearError(dob);
        }
    }

    const genderSelected = document.querySelector('input[name="gender"]:checked');
    const genderError = genderGroup.parentElement.querySelector(".error");
    if (!genderSelected) {
        genderError.textContent = "Please select your gender";
        isValid = false;
    } else {
        genderError.textContent = "";
    }

    if (department.value === "") {
        showError(department, "Please select your department");
        isValid = false;
    } else {
        clearError(department);
    }

    if (level.value === "") {
        showError(level, "Please select your level");
        isValid = false;
    } else {
        clearError(level);
    }

    if (stateOfOrigin.value.trim() === "") {
        showError(stateOfOrigin, "State of origin is required");
        isValid = false;
    } else {
        clearError(stateOfOrigin);
    }

    return isValid;
}

form.addEventListener("submit", function (event) {
    event.preventDefault();

    successBox.classList.add("hidden");

    if (!validateForm()) {
        return;
    }

    const student = {
        fullName: document.getElementById("fullName").value.trim(),
        matricNo: document.getElementById("matricNo").value.trim().toUpperCase(),
        email: document.getElementById("email").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        dob: document.getElementById("dob").value,
        gender: document.querySelector('input[name="gender"]:checked').value,
        department: document.getElementById("department").value,
        level: document.getElementById("level").value,
        stateOfOrigin: document.getElementById("stateOfOrigin").value.trim(),
        address: document.getElementById("address").value.trim() || "N/A"
    };

    console.log(student);

    successBox.innerHTML = `
        <h3>Form submitted successfully!</h3>
        <p><strong>Name:</strong> ${student.fullName}</p>
        <p><strong>Matric No:</strong> ${student.matricNo}</p>
        <p><strong>Email:</strong> ${student.email}</p>
        <p><strong>Phone:</strong> ${student.phone}</p>
        <p><strong>Date of Birth:</strong> ${student.dob}</p>
        <p><strong>Gender:</strong> ${student.gender}</p>
        <p><strong>Department:</strong> ${student.department}</p>
        <p><strong>Level:</strong> ${student.level}</p>
        <p><strong>State of Origin:</strong> ${student.stateOfOrigin}</p>
        <p><strong>Address:</strong> ${student.address}</p>
    `;
    successBox.classList.remove("hidden");

    form.reset();
});


// clear everything when reset is clicked
form.addEventListener("reset", function () {
    form.querySelectorAll(".invalid").forEach(function (field) {
        field.classList.remove("invalid");
    });
    form.querySelectorAll(".error").forEach(function (err) {
        err.textContent = "";
    });
    successBox.classList.add("hidden");
});