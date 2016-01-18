from flask import Flask, render_template, redirect, url_for, request, session, flash
from functools import wraps

app = Flask(__name__)

#need this for sessions to work right, 
#def don't keep it here for the long term
app.secret_key = "super secret"


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
	return render_template ("index.html")

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
        	flash('good job, you logged in')
        	return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('you logged out')
	return redirect(url_for('welcome'))



#start the server with 'run()' method
if __name__ == '__main__':
	app.run(debug=True)