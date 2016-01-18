from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(__name__)

#need this for sessions to work right, 
#def don't keep it here for the long term
app.secret_key = "super secret"

#route for home
@app.route('/')
def home():
	return "hello world"

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
        	return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return redirect(url_for('welcome'))



#start the server with 'run()' method
if __name__ == '__main__':
	app.run(debug=True)