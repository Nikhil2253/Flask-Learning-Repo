from flask import Flask, render_template, request

app = Flask(__name__)

# ✅ Dictionary of valid DBS characters with their "notable thing" as password
valid_users = {
    "goku": "ultra instinct",
    "vegeta": "ultra ego",
    "granolah": "sniper",
    "jiren": "limit breaker",
    "broly": "legendary ssj",
    "frieza": "black frieza",
    "beerus": "hakai",
    "whis": "angel staff",
    "moro": "magic absorption"
}

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/submit", methods=["POST"])
def login_submit():
    username = request.form.get("username").lower().strip()
    password = request.form.get("password").lower().strip()
    
    if username in valid_users and valid_users[username] == password:
        return render_template("welcome.html", name=username.capitalize())
    else:
        return "<h2 style='color:red;'>Invalid Credentials — Try Again!</h2>"
