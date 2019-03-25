from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/contact_us", methods=["POST"])
def contact_us():
    form_data = request.form
    print (form_data["email"])
    return "All OK"

app.run(debug=True)
