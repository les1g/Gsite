from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # This will load an HTML page

@app.route('/about')
def about():
    return render_template('about.html')  # Will render about page

if __name__ == "__main__":
    app.run(debug=True)