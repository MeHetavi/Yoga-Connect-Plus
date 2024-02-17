from flask_login import UserMixin, login_user, LoginManager,login_required, logout_user,current_user
from Config import app,request,redirect,render_template,url_for,flash
from Models import db,Users
import re

@app.route('/signup', methods=['GET', 'POST'])
def signUp():

    if request.method == 'POST':

        message = addUser()

        if message[1] == None:
            return render_template('SignUp.html',message = list(message)[0])
        else:
            return redirect(url_for('home',user = list(message)[1]))

    return render_template('SignUp.html')


def addUser():

    username = request.form['username']

    email = request.form['email']
    if not validateEmail(email):
        # Invalid email address
        return "Invalid email.",None
    
    password = request.form['password']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']

    trainer = request.form['type']
    if trainer == 'True':
         trainer = True
    else:
         trainer = False

    # Check if the username already exists in the database
    existing_user = Users.query.filter_by(username = username)

    message = None

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
        return message,new_user
    

def validateEmail(email):
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
      
    if re.match(email_pattern,email):
        return True
    else:
        # Invalid email address
        return False
    
