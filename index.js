// index.js - Interactive Validation and Form Handling

document.addEventListener('DOMContentLoaded', () => {
  const form = document.querySelector('form');

  if (!form) return;

  form.addEventListener('submit', (event) => {
    let isValid = true;

    // Validate Full Name
    const fullname = document.getElementById('fullname');
    if (fullname && fullname.value.trim() === '') {
      showError(fullname, 'Full name is required.');
      isValid = false;
    } else if (fullname) {
      clearError(fullname);
    }

    // Validate Matric Number
    const matric = document.getElementById('matric');
    if (matric && matric.value.trim() === '') {
      showError(matric, 'Matric number is required.');
      isValid = false;
    } else if (matric) {
      clearError(matric);
    }

    // Validate Email Format
    const email = document.getElementById('email');
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (email && !emailRegex.test(email.value.trim())) {
      showError(email, 'Please enter a valid email address.');
      isValid = false;
    } else if (email) {
      clearError(email);
    }

    // Validate Phone Number
    const phone = document.getElementById('phone');
    if (phone && phone.value.trim().length < 10) {
      showError(phone, 'Please enter a valid phone number.');
      isValid = false;
    } else if (phone) {
      clearError(phone);
    }

    // Validate Department Dropdown Selection
    const department = document.getElementById('department');
    if (department && department.value === '') {
      showError(department, 'Please select a department.');
      isValid = false;
    } else if (department) {
      clearError(department);
    }

    // Validate Level Dropdown Selection
    const level = document.getElementById('level');
    if (level && level.value === '') {
      showError(level, 'Please select your current level.');
      isValid = false;
    } else if (level) {
      clearError(level);
    }

    if (!isValid) {
      event.preventDefault();
    } else {
      alert('Registration form submitted successfully!');
    }
  });

  // Helper Functions for Validation Styling
  function showError(inputElement, message) {
    const parentGroup = inputElement.closest('.form-group');
    if (parentGroup) {
      parentGroup.classList.add('invalid');
      let errorDiv = parentGroup.querySelector('.error-message');
      if (!errorDiv) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        parentGroup.appendChild(errorDiv);
      }
      errorDiv.textContent = message;
    }
  }

  function clearError(inputElement) {
    const parentGroup = inputElement.closest('.form-group');
    if (parentGroup) {
      parentGroup.classList.remove('invalid');
      const errorDiv = parentGroup.querySelector('.error-message');
      if (errorDiv) {
        errorDiv.textContent = '';
      }
    }
  }
});
