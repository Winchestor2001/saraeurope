let burger_btn = document.querySelector('.burger_btn');
let menu = document.querySelector('nav ul');

burger_btn.onclick = () => {
    menu.classList.toggle('active')
};