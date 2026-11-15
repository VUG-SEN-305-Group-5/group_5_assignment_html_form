const form = document.getElementById("biodataForm");
const successBox = document.getElementById("successBox");
const departmentSelect = document.getElementById("department");

// Display validation errors
function showError(input, message) {
    input.classList.add("invalid");
    input.parentElement.querySelector(".error").textContent = message;
}

function clearError(input) {
    input.classList.remove("invalid");
    input.parentElement.querySelector(".error").textContent = "";
}

// Load departments from the backend
async function loadDepartments() {
    try {
        const response = await fetch("/api/departments");
        const result = await response.json();

        if (!response.ok || result.status === "error") {
            throw new Error(result.message || "Could not load departments");
        }

        const departments = Array.isArray(result.data)
            ? result.data
            : Array.isArray(result)
                ? result
                : [];

        departmentSelect.innerHTML =
            '<option value="">-- Select department --</option>';

        departments.forEach(department => {
            const option = document.createElement("option");

            option.value = department.department_id;
            option.textContent = department.department_name;

            departmentSelect.appendChild(option);
        });

        if (departments.length === 0) {
            departmentSelect.innerHTML =
                '<option value="">No departments available</option>';
        }

    } catch (error) {
        console.error("Department loading error:", error);
        departmentSelect.innerHTML =
            '<option value="">Departments unavailable</option>';
    }
}

// Validate registration form
function validateForm() {
    let isValid = true;

    const fields = [
        "firstName",
        "lastName",
        "otherName",
        "matricNo",
        "email",
        "phone",
        "dob",
        "department",
        "level",
        "stateOfOrigin",
        "address",
        "username",
        "password",
        "confirmPassword"
    ];

    fields.forEach(id => {
        const input = document.getElementById(id);
        if (input) clearError(input);
    });

    const firstName = document.getElementById("firstName");
    const lastName = document.getElementById("lastName");
    const matricNo = document.getElementById("matricNo");
    const email = document.getElementById("email");
    const phone = document.getElementById("phone");
    const dob = document.getElementById("dob");
    const department = document.getElementById("department");
    const level = document.getElementById("level");
    const stateOfOrigin = document.getElementById("stateOfOrigin");
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirmPassword");

    // First name
    if (!firstName.value.trim()) {
        showError(firstName, "First name is required");
        isValid = false;
    }

    // Last name
    if (!lastName.value.trim()) {
        showError(lastName, "Last name is required");
        isValid = false;
    }

    // Matric number
    const matricPattern = /^[A-Z]{3}\/[A-Z]{3}\/\d{2}\/\d{4,6}$/i;

    if (!matricNo.value.trim()) {
        showError(matricNo, "Matric number is required");
        isValid = false;
    } else if (!matricPattern.test(matricNo.value.trim())) {
        showError(matricNo, "Use the format VUG/SEN/24/11362");
        isValid = false;
    }

    // Email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!email.value.trim()) {
        showError(email, "Email is required");
        isValid = false;
    } else if (!emailPattern.test(email.value.trim())) {
        showError(email, "Enter a valid email address");
        isValid = false;
    }

    // Phone number
    const phonePattern = /^0\d{10}$/;

    if (!phone.value.trim()) {
        showError(phone, "Phone number is required");
        isValid = false;
    } else if (!phonePattern.test(phone.value.trim())) {
        showError(phone, "Enter an 11-digit number starting with 0");
        isValid = false;
    }

    // Date of birth
    if (!dob.value) {
        showError(dob, "Date of birth is required");
        isValid = false;
    } else {
        const birthDate = new Date(dob.value + "T00:00:00");
        const today = new Date();

        if (Number.isNaN(birthDate.getTime()) || birthDate >= today) {
            showError(dob, "Enter a valid date of birth");
            isValid = false;
        }
    }

    // Gender
    const gender = document.querySelector('input[name="gender"]:checked');
    const genderError = document.getElementById("genderGroup")
        .parentElement.querySelector(".error");

    if (!gender) {
        genderError.textContent = "Please select your gender";
        isValid = false;
    } else {
        genderError.textContent = "";
    }

    // Department
    if (!department.value) {
        showError(department, "Please select a department");
        isValid = false;
    }

    // Level
    if (!level.value) {
        showError(level, "Please select your level");
        isValid = false;
    }

    // State of origin
    if (!stateOfOrigin.value.trim()) {
        showError(stateOfOrigin, "State of origin is required");
        isValid = false;
    }

    // Username
    if (!username.value.trim()) {
        showError(username, "Username is required");
        isValid = false;
    } else if (username.value.trim().length < 3) {
        showError(username, "Username must have at least 3 characters");
        isValid = false;
    }

    // Password
    if (!password.value) {
        showError(password, "Password is required");
        isValid = false;
    } else if (password.value.length < 8) {
        showError(password, "Password must be at least 8 characters");
        isValid = false;
    }

    // Confirm password
    if (!confirmPassword.value) {
        showError(confirmPassword, "Please confirm your password");
        isValid = false;
    } else if (password.value !== confirmPassword.value) {
        showError(confirmPassword, "Passwords do not match");
        isValid = false;
    }

    return isValid;
}

// Submit registration form
form.addEventListener("submit", async function (event) {
    event.preventDefault();

    successBox.classList.add("hidden");

    if (!validateForm()) {
        return;
    }

    const gender = document.querySelector('input[name="gender"]:checked');

    const student = {
        first_name: document.getElementById("firstName").value.trim(),
        last_name: document.getElementById("lastName").value.trim(),
        other_name: document.getElementById("otherName").value.trim(),
        matric_no: document.getElementById("matricNo").value.trim().toUpperCase(),
        email: document.getElementById("email").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        date_of_birth: document.getElementById("dob").value,
        gender: gender.value,
        department_id: Number(departmentSelect.value),
        level: Number(document.getElementById("level").value),
        state_of_origin: document.getElementById("stateOfOrigin").value.trim(),
        address: document.getElementById("address").value.trim(),
        username: document.getElementById("username").value.trim(),
        password: document.getElementById("password").value,
        confirm_password: document.getElementById("confirmPassword").value
    };

    const submitButton = form.querySelector(".btn-submit");
    submitButton.disabled = true;
    submitButton.textContent = "Registering...";

    try {
        const response = await fetch("/api/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(student)
        });

        const result = await response.json();

        if (!response.ok || result.status !== "success") {
            throw new Error(result.message || "Registration failed");
        }

        const heading = document.createElement("h3");
        heading.textContent = "Registration successful!";

        const message = document.createElement("p");
        message.textContent = result.message || "Your account has been created successfully.";

        successBox.replaceChildren(heading, message);
        successBox.classList.remove("hidden");

        form.reset();

    } catch (error) {
        successBox.textContent = error.message;
        successBox.classList.remove("hidden");
    } finally {
        submitButton.disabled = false;
        submitButton.textContent = "Register";
    }
});

// Reset form errors
form.addEventListener("reset", function () {
    form.querySelectorAll(".invalid").forEach(field => {
        field.classList.remove("invalid");
    });

    form.querySelectorAll(".error").forEach(error => {
        error.textContent = "";
    });

    successBox.classList.add("hidden");
});

// Load departments when the page opens
loadDepartments();