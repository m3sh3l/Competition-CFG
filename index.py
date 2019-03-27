# Import requests
import requests

# Import Flask
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
    send_simple_message()
    return "all ok"


def send_simple_message():
    form_data = request.form
    return requests.post(
    "https://api.mailgun.net/v3/sandboxae7220a00ff84c7ca7fe2dc6f566a5ed.mailgun.org/messages",
    auth=("api", "a9b68955e996430e41e4303d25eb50cd-de7062c6-302dc37f"),
    data={"from": "Excited User <mailgun@sandboxae7220a00ff84c7ca7fe2dc6f566a5ed.mailgun.org>",
          "to": form_data["email"],
          "subject": "Helloooooooooooooooo",
          "text": "Testing some Mailgun awesomness!"})

# Run app if application is debugged
app.run(debug=True)
