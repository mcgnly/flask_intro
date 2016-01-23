from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
from flask.ext.sqlalchemy import SQLAlchemy
# import sqlite3

app = Flask(__name__)

#need this for sessions to work right, 
#def don't keep it here for the long term
app.secret_key = "super secret"

#this was for using straight up sqlight
#app.database = "sample.db"

#change to sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

#create the sqlalchemy object
db = SQLAlchemy(app)

#only now can we import the model, bc only now the db object exists
from models import * #by * we mean BlogPost, but whatever

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs): #wtf is this shit?
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

#route for home
@app.route('/')
@login_required
def home():
    # #use g to store temp value, flask standard
    # g.db = connect_db()
    # cur = g.db.execute('select * from posts')
    # #listcomp in python- generates a list with the rows the dicts that the cur.fetchall spit out
    # posts = [dict(title = row[0], description=row[1]) for row in cur.fetchall()]
    # g.db.close()

    #now, using squalchemy- fancy cause it's one line:
    posts = db.session.query(BlogPost).all()
    return render_template ("index.html", posts = posts)

#route for welcome
@app.route('/welcome')
def welcome():
	return render_template ("welcome.html")

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
        	session['logged_in'] = True
        	flash('you were just logged in')
        	return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('you logged out')
	return redirect(url_for('welcome'))


#this was for straight sqlight, don't need it for sqlalchemy
# def connect_db():
#     return sqlite3.connect(app.database)



#start the server with 'run()' method
if __name__ == '__main__':
	app.run(debug=True)