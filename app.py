from flask import Flask, render_template

app = Flask(__name__)

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
