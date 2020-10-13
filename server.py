from flask import Flask, render_template, redirect, session, request 
app = Flask(__name__)
app.secret_key = 'counter key'

@app.route('/')
def root(): 
    return redirect('/counter')

@app.route('/counter')
def index():
    if 'counter' in session:
        session['counter'] += 1
    else:
         session['counter'] = 0
    return render_template("counter.html")

@app.route('/counter/add-n-button',methods = ['POST'])
def add_n_button():
    session['n'] = request.form['n']
    return redirect('/counter')

@app.route('/counter/plus-two')
def plus_two():
    session['counter'] += 1
    return redirect('/counter')

@app.route('/counter/plus/<n>')
def plus_n(n):
    session['counter'] += int(n) - 1
    return redirect('/counter')

@app.route('/counter/reset')
def reset_counter():
    if('n' in session):
        session.pop('n')
    if('counter' in session):
        session.pop('counter')
    return redirect('/counter')

if __name__ == "__main__":
    app.run(debug=True)