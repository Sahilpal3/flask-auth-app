
#Routes

#login
@app.route("/login",methods=["POST"])
def login():
    #Collect info
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        #login the user
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return render_template("index.html")
    
#register
@app.route("/register",methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template("index.html",error="User already here!")
    else:
        new_user = User(username = username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect(url_for('dashboard'))

#dashboard
@app.route("/dashboard")
def dashboard():
    if "username" in session:
        return render_template("dashboard.html")
    return redirect(url_for("home"))

#logout

