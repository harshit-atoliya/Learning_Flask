from flask import Flask , Response, redirect, session, url_for, request

app= Flask(__name__)
app.secret_key="superkey"

@app.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        if username=="admin" and password=="123":
            session['user']=username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials",mimetype="text/plain")
    return """
            <h2>Login page</h2>
            <form method="POST">
            Username:<input type="name" name="username" placeholder="Enter your name"><br>
            Password:<input type="password" name="password" placeholder="Enter your password"><br>
            <input type="submit" value="Login">
            </form>
"""
@app.route("/welcome")
def welcome():
    if 'user' in session:
        return f"""
        <h2>Welcom, {session['user']}</h2>
        <a href={url_for('logout')}>logout</a>
    """
    return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for('login'))    
