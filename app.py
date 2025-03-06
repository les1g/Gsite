from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'untitledgisel@gmail.com'  # Use your email
app.config['MAIL_PASSWORD'] = 'Gisel123'  # Use your email password (use app password if 2FA is enabled)
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')  # Home page

@app.route('/about')
def about():
    return render_template('about.html')  # About Me page

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')  # Portfolio page

@app.route('/resume')
def resume():
    return render_template('resume.html')  # Resume page

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message('Contact Form Submission',
                      recipients=['untitledgisel@gmail.com'])  # Replace with your email
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)
        return 'Message sent successfully!'
    return render_template('contact.html')  # Contact page

if __name__ == '__main__':
    app.run(debug=True)
