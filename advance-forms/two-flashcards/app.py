from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "sasuke-uchiha"  # required for flash messages

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        username = request.form.get("username")
        feedback = request.form.get("feedback")

        if not username:
            flash("⚠️ Your Name can’t be empty", "error")
            return redirect(url_for("form"))
        if not feedback:
            flash("⚠️ Feedback cannot be empty", "error")
            return redirect(url_for("form"))

        flash(f"✅ Thanks {username}, your feedback was saved!", "success")
        return redirect(url_for("thankyou", username=username, feedback=feedback))

    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    username = request.args.get("username")
    feedback = request.args.get("feedback")
    return render_template("thankyou.html", username=username, feedback=feedback)

