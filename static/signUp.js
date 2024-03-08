const toggleButton = document.getElementById('js-navbar-toggle');
const menu = document.getElementById('js-menu');
toggleButton.addEventListener('click', () => {
    menu.classList.toggle('nav_active');
});

const navLinks = document.querySelectorAll('.nav_links');
navLinks.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.forEach(link => link.classList.remove('active'));
        link.classList.add('active');
    });
});

const eyeIconClasses = ['uil-eye', 'uil-eye-slash'];
const passwordField1 = document.getElementById('id_password1');
const passwordField2 = document.getElementById('id_password2');
const showPasswordButton = document.getElementById('showPsswd');
const eyeIcon = showPasswordButton.querySelector('.eye_icons');
function showPassword(e) {
    if (
        passwordField1.type === 'password' &&
        passwordField2.type === 'password' &&
        (e.type !== 'keydown' || e.code === 'Enter')
    ) {
        passwordField1.type = 'text';
        passwordField2.type = 'text';
        eyeIcon.classList.remove(eyeIconClasses[0]);
        eyeIcon.classList.add(eyeIconClasses[1]);
    }
}
function hidePassword(e) {
    if (
        passwordField1.type !== 'password' &&
        passwordField2.type !== 'password' &&
        (e.type !== 'keyup' || e.code == 'Enter')
    ) {
        passwordField1.type = 'password';
        passwordField2.type = 'password';
        eyeIcon.classList.remove(eyeIconClasses[1]);
        eyeIcon.classList.add(eyeIconClasses[0]);
    }
}
showPasswordButton.addEventListener('mousedown', showPassword);
document.addEventListener('mouseup', hidePassword);
showPasswordButton.addEventListener('touchstart', showPassword);
document.addEventListener('touchend', hidePassword);
showPasswordButton.addEventListener('keydown', showPassword);
document.addEventListener('keyup', hidePassword);

const emailField = document.getElementById("id_email");
function validateEmail() {
    if (!emailField.value.match(/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/)) {
        emailField.style.color = '#FF6969';
        return false;
    }
    emailField.style.color = '#FFFFFF'
    return true;
}

const passwordLen1 = document.getElementById('id_password1');
passwordLen1.addEventListener('input', function () {
    if (passwordLen1.value.length <= 7) {
        passwordLen1.style.color = '#FF6969';
    } else {
        passwordLen1.style.color = '#FFFFFF';
    }
});

const passwordLen2 = document.getElementById('id_password2');
passwordLen2.addEventListener('input', function () {
    if (passwordLen2.value.length <= 7) {
        passwordLen2.style.color = '#FF6969';
    } else {
        passwordLen2.style.color = '#FFFFFF';
    }
});