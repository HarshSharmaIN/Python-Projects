from flask import Flask, render_template, request,redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)
app.secret_key = 'xyzsdfg'

app.config['SQLALCHEMY_DATABASE_URI'] ="mysql://root:kapi@localhost/users"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'kapi'
app.config['MYSQL_DB'] = 'users'
mysql = MySQL(app)


class login(db.Model):
    user_id =  db.Column(db.Integer, primary_key = True)
    user_name =  db.Column(db.String(35), unique = True, nullable = False)
    user_email =  db.Column(db.String(200), nullable = False)
    user_password =  db.Column(db.String(50), nullable = False)
    date_created =  db.Column(db.DateTime, default = datetime.utcnow)


    # def __repr__(self) -> str:
    #     return f"{self.Sno} -  {self.ID}"

@app.route("/")
def hello_world():
    return render_template('cart.html')
    

@app.route("/signin", methods=['GET', 'POST'])
def Sign_in():
    msg = ''
    if(request.method=='POST' and 'inputEmail' in request.form and 'inputPassword' in request.form):
        '''SIgning in'''
        email = request.form.get("inputEmail")
        passw = request.form.get("inputPassword")

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM login WHERE user_email = %s AND user_password = %s', (email, passw,))
        # Fetch one record and return result
        account = cursor.fetchone()

        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['user_id']
            session['username'] = account['user_name']
            msg = 'Logged in Successfully'
            # Redirect to home page
            return render_template('home.html',msg=msg)
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('signin.html',msg=msg)

@app.route("/signup", methods = ['GET','POST'])
def Sign_up():
    if(request.method=='POST'):
        '''add entry to the database'''
        name = request.form.get("inputName")
        email = request.form.get("inputEmail")
        passw = request.form.get("inputPassword")

        entry = login(user_name = name, user_email = email, user_password = passw)
        db.session.add(entry)
        db.session.commit()
    return render_template('signUp.html')


@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect('http://127.0.0.1:5000/signin')

@app.route('/user')
def user():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('cart.html', username=session['user_name'])
    # User is not loggedin redirect to login page
    return redirect("http://127.0.0.1:5000/signin")


@app.route('/homepage')
def homepage():
    return render_template("cart.html")

@app.route('/racquets')
def racket():
    return render_template("rackets.html")

@app.route('/shoes')
def shoes():
    return render_template("shoes.html")

# @app.route('/shuttle')
# def homepage():
#     return render_template("shuttle.html")

if __name__ == '__main__':
    app.run(debug=True)