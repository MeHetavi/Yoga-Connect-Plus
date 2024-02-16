from Config import app, render_template, url_for,request
import psycopg2

def db_conn():
    conn=psycopg2.connect(database="student",host="localhost",user="postgres",password="tirth",port="5432")
    return conn

@app.route("/")
def home():
    return render_template("Home.html")

@app.route('/login', methods=['GET', 'POST'])
def Login():
    conn=db_conn()
    cur=conn.cursor()
    if request.method=='POST':
        username=request.form["username"]
        email=request.form["email"]
        password=request.form["password"]
        gender=request.form["gender"]
        age=request.form["age"]
        type=request.form["type"]

        cur.execute('''INSERT INTO LOGIN VALUES(%s,%s,%s,%s,%s,%s)''',(username,email,password,gender,age,type))


@app.route('/signup', methods=['GET', 'POST'])
def signUp():
    conn=db_conn()
    cur=conn.cursor()
    if request.method=='POST':
        username=request.form["username"]
        password=request.form["password"]
        cur.execute('''Select password from login where username=(%s)''',(username))
        data=cur.fetchall()
        cur.close()
        conn.close()
        for i in data:
            if i[0]==password:
                break

        return render_template("Home.html")  
    
@app.route('/explore')
def expl():
    return render_template('Explore.html')
if __name__=="__main__":
    app.run(debug=True)