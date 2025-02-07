document.addEventListener("DOMContentLoaded", function() {
    const menuButton = document.querySelector(".hamburger-menu");
    const navLinks = document.querySelector(".nav-links");

    menuButton.addEventListener("click", function() {
        navLinks.classList.toggle("show-menu"); // Toggles menu visibility
    });

    // Optional: Close menu when clicking outside
    document.addEventListener("click", function(event) {
        if (!menuButton.contains(event.target) && !navLinks.contains(event.target)) {
            navLinks.classList.remove("show-menu");
        }
    });
});
