from flask import *
from mongoengine import *
import mlab
# import location


app = Flask(__name__)
# app.config['SECRET_KEY'] = "daiso"

mlab.connect()

class User(Document):
    username = StringField()
    password = StringField()

@app.route('/')
def index():

    loggedin = session.get('loggedin', False)
    return render_template('index.html', loggedin=loggedin)
#
# thao = User(username= 'lam', password ='lamlam')
# thao.save()

@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        form = request.form
        username = form['username']
        password = form['password']
        if username == User.objects(username = username):
            return "user existed"
        else:
            new_user = User(username = username, password = password)
            new_user.save()
            return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        form =  request.form
        username = form['username']
        password = form['password']
        user = User.objects(username = username).first()
        if user is None:
            return"User khong ton tai"
        elif user.password != password :
            return "Sai mat khau"
        else:
            session['loggedin'] =True
            return redirect(url_for('index'))
#
# @app.route('/logout')
# def logout():
#     session['logout'] =False
#     return redirect(url_for('login'))



if __name__ == '__main__':
  app.run(debug=True)
