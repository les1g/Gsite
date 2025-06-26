from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', 'your-app-password')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME', 'your-email@gmail.com')

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

@app.route('/contact')
def contact():
    return render_template('contact.html')  # Contact page

if __name__ == '__main__':
    app.run(debug=True)
