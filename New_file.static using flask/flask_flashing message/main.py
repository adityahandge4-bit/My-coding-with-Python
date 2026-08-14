from flask import Flask,flash,render_template,redirect  # import Flask class, flash function, and render_template helper

app = Flask(__name__)  # create Flask application instance using current module name
app.secret_key="Ai&cs@engg#$&@"  # set secret key for session management and flashing messages

@app.route("/")  # define route for the home page
def hello_world():
  return render_template("index.html")  # render index.html template for home page

@app.route("/logout")  # define route for logout action
def logout():
  flash("You have been logout!","success")  # flash a success message to show after logout
  return render_template("logout.html")  # render index.html template after logout
app.run(debug=True)  # run the Flask development server in debug mode

