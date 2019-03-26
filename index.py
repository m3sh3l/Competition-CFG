from flask import Flask, render_template, request

app = Flask("MyApp")
# Load index.html
@app.route("/")
def hello():
    return render_template("index.html")

# Load Contact Us page
@app.route("/contact_us")
def contact_page():
    return render_template("contact_us.html")

# Post form when submit button is clicked
@app.route("/contact_us", methods=["POST"])
def contact_us():
    form_data = request.form
    print (form_data["email"])
    return "All OK"

# To Cathy: Modify contact_us function with the mailgun API.

# Run app if application is debugged
app.run(debug=True)
