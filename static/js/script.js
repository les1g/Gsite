document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent default form submission

    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let message = document.getElementById('message').value;

    if (name && email && message) {
        alert('Message Sent! Thank you for reaching out.');
        document.getElementById('contactForm').reset(); // Reset form fields after submission
    } else {
        alert('Please fill in all fields.');
    }
});
