from Config import app, render_template, request, redirect, url_for, seceret_key
from Models import db,Users
from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user
from Models import db,Users
import re

app.secret_key = seceret_key # For cookies and other personal info.


login_manager = LoginManager()
login_manager.init_app(app)

# Callback to reload the user object     
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


# Sign In route
@app.route('/signin', methods=['GET', 'POST'])
def signIn():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            return redirect(url_for('home',user = user))

        else:
            return render_template('SignIn.html',message = 'Invalid Credentials.')

    else:
        return render_template('SignIn.html')


# Logout route.
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'),logout_msg = 'Logged out successfully.')


@app.route('/signup', methods=['GET', 'POST'])
def signUp():

    if request.method == 'POST':

        message = addUser()

        if message[1] == None:
            if 'email' in message[0] : 
                return render_template('SignUp.html',invalidEmail = message[0])
            else: 
                return render_template('SignUp.html',userExists = message[0])
        else:
            return redirect(url_for('home',user = message[1]))

    return render_template('SignUp.html')


def addUser():
    # validate email.
    email = request.form['email']
    error = validateEmail(email)
    if error:
        # Invalid email address
        return error,None
    
    password = request.form['password']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']

    trainer = request.form['type']
    if trainer == 'True':
         trainer = True
    else:
         trainer = False

    # Check if the username already exists in the database.
    username = request.form['username']
    existing_user = Users.query.filter_by(username = username).first()


    if existing_user:
            # Username already exists.
            # Select new one.
            message = "Username already exists."
            return message,None
    else:
        # Create a new user and add it to the database
        new_user = Users(username=username, password=password,email = email,name = name,age = age,gender = gender,trainer = trainer)
        db.session.add(new_user)
        db.session.commit()
        return None,new_user
    

def validateEmail(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
      
    if re.match(email_pattern,email):

        if Users.query.filter_by(email=email).first():
            return 'email already exists.'
        else:
            return
    else:
        # Invalid email address
        return "Invalid email."
    
