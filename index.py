from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/contact-us")
def hello():
    return render_template("contact_us.html")

app.run(debug=True)
