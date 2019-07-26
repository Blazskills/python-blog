from flask import Flask, render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
import sqlite3
from datetime import datetime
app = Flask(__name__)
app.secret_key = "kjhdsfkjhkjdsfhj"

sqlite3.connect('tmp/database.db')

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///tmp/database.db'
login_manager = LoginManager()


db = SQLAlchemy(app)
login_manager.init_app(app)
login_manager.login_view ='login'
@login_manager.user_loader
def user_loader(user_id):
    return Users.query.filter_by(id=user_id).first()


class Users(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    images = db.Column(db.String(255))
    brief = db.Column(db.String(255))
    content = db.Column(db.Text)
    date_posted = db.Column(db.String(255),default=datetime.now())



@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['name']
        username = request.form['username']
        password = request.form['password']
        new_users = Users(name=fname,username=username,
                            password=password)
        db.session.add(new_users)
        db.session.commit()
        return "sign up complete"
    return render_template("./signup/signup.html")




@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
        username = request.form['username']
        password = request.form['password']
        user = Users.query.filter_by(username=username).first()
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('dashboard'))
            else:
                return 'invalid password'
        else:
            return "invalid username"
                
    return render_template('./login.html')


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('./dashboard.html')

@app.route('/viewinfo')
def viewinfo():
    all_users = Users.query.all()
    return render_template('./view.html',all_users=all_users)

@app.route('/blog/index')
def blog():
    return render_template('blog.html')

@app.route('/create',methods=['GET','POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        images = request.form['images']
        brief = request.form['brief']
        content = request.form['content']
        new_content = BlogPost(title=title,author=author,
                            images=images,brief=brief,content=content)
        db.session.add(new_content)
        db.session.commit()
        return "Article Created"
    return render_template('/create.html')

@app.route('/viewarticle')
def viewarticle():
    all_contents = BlogPost.query.all()
    return render_template('./blog.html',all_contents=all_contents)



@app.route('/moneycont')
def money():
    moncontents = BlogPost.query.filter_by(contents='contents').all()
    return render_template('./content.html',moncontents=moncontents)


@app.route('/kidnapcont/<id>')
def cont(id):
    post = BlogPost.query.filter_by(id=id).first()
    return render_template("cont.html",post=post)

@app.route('/summer')
def register():
    return render_template('./summernote.html')



@app.route('/logout')
def logout():
    logout_user()
    return 'logout succeful'


if __name__=='__main__':
    app.run(port=7000,debug=True)
