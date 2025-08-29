from flask import Flask, render_template, request, redirect, url_for, flash

app=Flask(__name__);
app.secret_key="sasuke-uchiha";

@app.route("/")
def home():
    return "Home Page";

@app.route("/feedback", methods=["POST","GET"])
def feedback():
    if request.method == "POST": 
        username= request.form.get("username")
        feedback= request.form.get("feedback")

        return render_template("thankyou.html", username=username, feedback=feedback)
    
    return render_template("feedback.html")
