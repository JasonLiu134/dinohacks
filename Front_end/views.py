from flask import Blueprint, render_template

file_name = Blueprint("file_name", __name__)

@file_name.route("/")
def home():
    return render_template("index.html")