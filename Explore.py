from Config import app, render_template, request

@app.route('/explore')
def explore():
    return render_template('Explore.html')