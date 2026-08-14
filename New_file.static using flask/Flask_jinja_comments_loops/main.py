from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    marks={
        "John":89,
        "Siddharth":90,
        "Roshni":99,
        "Nukul":100,
        "Harry":99,
        "Sahdev":12,
        "Manoj":23,
        "Rishi":65
        
    }
    return render_template("index.html",marks=marks)
app.run(debug=True)