from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello_world():
    name="Harry"
    token=234567
    if "name" in request.args.keys():
        name=request.args["name"]
    if "token" in request.args.keys():
        token=request.args["tokens"]

    # name=request.args.get("name")# or you can also make use as name=request.args["name"]
    # token=request.args.get("tokens")# or you can also amke use as token=request.args["tokens"]   

    return render_template("index.html", name=name, tokens=token)
app.run(debug=True)