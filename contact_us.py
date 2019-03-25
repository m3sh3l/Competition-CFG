##open this web page
from flask import Flask, render_template, request
import requests


app = Flask("MyApp")

@app.route("/contact-us, methods=[POST]")
def sign_ups():
    form_data = request.form
    print form_dats["email"]
    return "All OK"

app.run(debug=True)
