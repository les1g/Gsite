from dotenv import load_dotenv
load_dotenv() # Load environment variables from .env file

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

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
        # Get form data
        name = request.form.get('first') # Changed from first_name
        email = request.form.get('email')
        message_body = request.form.get('message')

        # Simple validation
        if not all([name, email, message_body]): # Removed last_name
            flash('All form fields are required.', 'danger')
            return redirect(url_for('contact'))

        # Create and send email
        try:
            msg = Message(f"New message from {name}", # Changed from first_name last_name
                          recipients=[app.config['MAIL_USERNAME']])
            msg.body = f"From: {email}\n\n{message_body}"
            mail.send(msg)
            flash('Your message has been sent successfully!', 'success')
        except Exception as e:
            # Log the error for debugging
            print(e)
            flash('Sorry, there was an error sending your message. Please try again later.', 'danger')

        return redirect(url_for('contact'))
        
    return render_template('contact.html')  # Contact page

if __name__ == '__main__':
    app.run(debug=True)
