from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3


app = Flask(__name__)

#need this for sessions to work right, 
#def don't keep it here for the long term
app.secret_key = "super secret"
app.database = "sample.db"


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
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
    #use g to store temp value, flask standard
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    #listcomp in python- generates a list with the rows the dicts that the cur.fetchall spit out
    posts = [dict(title = row[0], description=row[1]) for row in cur.fetchall()]
    g.db.close()
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

def connect_db():
    return sqlite3.connect(app.database)



#start the server with 'run()' method
if __name__ == '__main__':
	app.run(debug=True)