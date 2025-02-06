document.addEventListener("DOMContentLoaded", function () {
    const menuButton = document.querySelector(".hamburger-menu");
    const navLinks = document.querySelector(".nav-links");

    menuButton.addEventListener("click", function () {
        navLinks.classList.toggle("show-menu"); // Toggle class to show/hide menu
    });
});
