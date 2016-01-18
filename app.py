from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

#route for home
@app.route('/')
def home():
	return "hello world"

#route for welcome
@app.route('/welcome')
def welcomw():
	return render_template ("welcome.html")

# route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)



#start the server with 'run()' method
if __name__ == '__main__':
	app.run(debug=True)