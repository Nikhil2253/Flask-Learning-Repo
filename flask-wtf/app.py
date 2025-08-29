from flask import Flask, render_template, request, redirect, url_for, flash
from form import RegistrationForm

app= Flask(__name__)
app.secret_key="sasuke-uchiha"

@app.route("/", methods=["GET","POST"])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        username=form.name.data
        email=form.email.data
        flash(f"Welcome, {username} registered succesfully","success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")
