from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "Vegeta" and password == "Kakarot":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials. Try again", mimetype="text/plain")

    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Mythical Login</title>
  <style>
    body {
      margin: 0;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #1a1a40, #0f0f20);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #fff;
    }

    .login-container {
      background: rgba(20, 20, 60, 0.9);
      padding: 40px 50px;
      border-radius: 20px;
      box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.2);
      text-align: center;
      max-width: 350px;
      width: 100%;
      position: relative;
    }

    .login-container::before {
      content: "";
      position: absolute;
      top: -3px;
      left: -3px;
      right: -3px;
      bottom: -3px;
      border-radius: 20px;
      background: linear-gradient(45deg, #ff00cc, #3333ff, #00ffff);
      z-index: -1;
      filter: blur(10px);
      animation: glowing 6s linear infinite;
    }

    @keyframes glowing {
      0% { filter: blur(10px) hue-rotate(0deg); }
      100% { filter: blur(10px) hue-rotate(360deg); }
    }

    h2 {
      margin-bottom: 20px;
      font-size: 26px;
      letter-spacing: 2px;
      text-shadow: 0 0 10px #ff00cc, 0 0 20px #3333ff;
    }

    .input-field {
      width: 100%;
      padding: 12px;
      margin: 12px 0;
      border-radius: 10px;
      border: none;
      outline: none;
      background: rgba(255,255,255,0.1);
      color: #fff;
      font-size: 15px;
      transition: 0.3s;
    }

    .input-field:focus {
      background: rgba(255,255,255,0.2);
      box-shadow: 0px 0px 10px #00ffff;
    }

    .btn {
      width: 100%;
      padding: 12px;
      margin-top: 20px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      font-size: 16px;
      font-weight: bold;
      background: linear-gradient(135deg, #ff00cc, #3333ff);
      color: #fff;
      transition: 0.3s;
    }

    .btn:hover {
      background: linear-gradient(135deg, #3333ff, #ff00cc);
      box-shadow: 0px 0px 20px #ff00cc, 0px 0px 20px #3333ff;
    }

  </style>
</head>
<body>
  <div class="login-container">
    <h2>✨ Mythical Login ✨</h2>
    <form method="POST">
      <input type="text" name="username" placeholder="Enter Username" class="input-field" required>
      <input type="password" name="password" placeholder="Enter Password" class="input-field" required>
      <button type="submit" class="btn">Login</button>
    </form>
  </div>
</body>
</html>
'''

#welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome</title>
  <style>
    body {{
      margin: 0;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      background: linear-gradient(135deg, #1a1a40, #0f0f20);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      color: #fff;
    }}

    .container {{
      background: rgba(20, 20, 60, 0.9);
      padding: 40px 50px;
      border-radius: 20px;
      box-shadow: 0px 0px 30px rgba(255, 255, 255, 0.2);
      text-align: center;
      max-width: 400px;
      width: 100%;
      position: relative;
    }}

    .container::before {{
      content: "";
      position: absolute;
      top: -3px;
      left: -3px;
      right: -3px;
      bottom: -3px;
      border-radius: 20px;
      background: linear-gradient(45deg, #ff00cc, #3333ff, #00ffff);
      z-index: -1;
      filter: blur(10px);
      animation: glowing 6s linear infinite;
    }}

    @keyframes glowing {{
      0% {{ filter: blur(10px) hue-rotate(0deg); }}
      100% {{ filter: blur(10px) hue-rotate(360deg); }}
    }}

    h1 {{
      font-size: 28px;
      margin-bottom: 20px;
      text-shadow: 0 0 15px #ff00cc, 0 0 20px #3333ff;
    }}

    p {{
      font-size: 18px;
      margin-bottom: 25px;
      text-shadow: 0px 0px 8px #00ffff;
    }}

    .btn {{
      padding: 12px 25px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      font-size: 16px;
      font-weight: bold;
      background: linear-gradient(135deg, #ff00cc, #3333ff);
      color: #fff;
      transition: 0.3s;
    }}

    .btn:hover {{
      background: linear-gradient(135deg, #3333ff, #ff00cc);
      box-shadow: 0px 0px 20px #ff00cc, 0px 0px 20px #3333ff;
    }}
  </style>
</head>
<body>
  <div class="container">
    <h1>🌌 Welcome, {session['user']}! 🎉</h1>
    <p>You have entered the mythical realm.</p>
    <form method="POST" action="/logout">
      <button type="submit" class="btn">Logout</button>
    </form>
  </div>
</body>
</html>
'''
    return redirect(url_for("login"))

#logout page
@app.route("/logout", methods=["POST"])
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))
