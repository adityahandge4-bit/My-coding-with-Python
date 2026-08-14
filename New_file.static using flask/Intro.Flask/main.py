from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html") # If you want to make the template to be read and must be highlighted in the website you must have to import render_tempalate
app.run(debug=True) # This is for making your website to run