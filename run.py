from Config import app, render_template, request
import Gate,Explore

@app.route('/')
def home():
    user = request.args.get('user')
    return render_template('Home.html',user = user)

app.run(debug=True)