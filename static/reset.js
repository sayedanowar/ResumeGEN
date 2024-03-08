const eyeIconClasses = ['uil-eye', 'uil-eye-slash'];
const passwordField1 = document.getElementById('id_new_password1');
const passwordField2 = document.getElementById('id_new_password2');
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

const passwordLen1 = document.getElementById('id_new_password1');
passwordLen1.addEventListener('input', function () {
    if (passwordLen1.value.length <= 7) {
        passwordLen1.style.color = '#FF6969';
    } else {
        passwordLen1.style.color = '#FFFFFF';
    }
});

const passwordLen2 = document.getElementById('id_new_password2');
passwordLen2.addEventListener('input', function () {
    if (passwordLen2.value.length <= 7) {
        passwordLen2.style.color = '#FF6969';
    } else {
        passwordLen2.style.color = '#FFFFFF';
    }
});