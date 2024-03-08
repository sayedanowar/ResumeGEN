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

function PrintResume() {
    const resume = document.body.innerHTML;
    const resumeContents = document.getElementById('resume').innerHTML;
    document.body.innerHTML = resumeContents;
    window.print();
    document.body.innerHTML = resume;
}

const eyeIconClasses = ['uil-eye', 'uil-eye-slash'];
const passwordField = document.getElementById('id_password');
const showPasswordButton = document.getElementById('showPsswd');
const eyeIcon = showPasswordButton.querySelector('.eye_icons');
function showPassword(e) {
    if (
        passwordField.type === 'password'
        && (e.type !== 'keydown' || e.code === 'Enter')
    ) {
        passwordField.type = 'text';
        eyeIcon.classList.remove(eyeIconClasses[0]);
        eyeIcon.classList.add(eyeIconClasses[1]);
    }
}
function hidePassword(e) {
    if (
        passwordField.type !== 'password'
        && (e.type !== 'keyup' || e.code == 'Enter')
    ) {
        passwordField.type = 'password';
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


const passwordLen = document.getElementById('id_password');
passwordLen.addEventListener('input', function () {
    if (passwordLen.value.length <= 7) {
        passwordLen.style.color = '#FF6969';
    } else {
        passwordLen.style.color = '#FFFFFF';
    }
});