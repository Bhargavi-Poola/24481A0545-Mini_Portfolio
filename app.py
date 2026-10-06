from flask import Flask,render_template 
from flask import request,redirect,url_for
app=Flask(__name__)
@app.route('/')
def welcome():
    return "<center> Welcome to FlaskApp </center>"

@app.route('/greet/<name>')
def greet(name):
    return f'<center> Good Morning {name} </center>'

@app.route('/user',methods=['GET','POST'])
def myProfile():
         data=None
         if request.method == 'POST':
              data=request.form
         return render_template('base.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)