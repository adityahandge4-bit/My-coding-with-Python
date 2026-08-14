from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={
    "Harry":98,
    "Ganesh":45,
    "Srijesh":12,
    "Aditya":99,
    "Kavita":100
    }
   

    return jsonify(marks)
app.run(debug=True)