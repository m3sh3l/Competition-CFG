// open this web page
from flask import Flask, render_template, request

    import requests


app = Flask("MyApp")

@app.route("/contact-us")
def hello():
    return render_template("contact_us.html")

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxae7220a00ff84c7ca7fe2dc6f566a5ed.mailgun.org/messages",
        auth=("api", "a9b68955e996430e41e4303d25eb50cd-de7062c6-302dc37f"),
        data={"from": "Excited User <mailgun@sandboxae7220a00ff84c7ca7fe2dc6f566a5ed.mailgun.org>",
            "to": ["cathy7oranges@gmail.com"],
            "subject": "Helloooooooooooooooo",
            "text": "Testing some Mailgun awesomness!"})

app.run(debug=True)
