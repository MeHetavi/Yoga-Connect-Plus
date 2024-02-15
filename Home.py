from Config import app,render_template
import templates

@app.route('/home')
def renderHomePage():
    return render_template('Home.html')
