from flask import Flask, redirect, render_template, request
import random

songs = []

app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        genre = request.form.get("genre")
        return redirect("/")
    
    else:
        return render_template("index.html")