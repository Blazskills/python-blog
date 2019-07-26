from flask import Flask, render_template, request

app = Flask(__name__)

usernames = ["Yemi","Laide","Ope","Wale","Funmi","Bayo"]

database = []


@app.route('/server')
def yemi():
    return 'Testing server'

@app.route('/refer/<username>')
def refer(username):
    if username in usernames:
        return "welcome"
    else:
        return "invalid referer id"
@app.route('/signnup/<username>/<password>/<email>')
def signup(username,password,email):
    database.append(username)
    database.append(password)
    database.append(email)
    return "Registration successful"

@app.route('/resultt')
def resultt():
    return database

@app.route('/login/<email>')
def login(email):
    if email in database:
        return "Welcome "+email
    else:
        return "Not registered"

@app.route("/view")
def view():
    return "<h1>Hello world</h1>" "<p>what's going on out there? I'd really like to know if it's hot or cold?</p>" "<p>Ans-Man it's so hot out here I'd suggest you go back to where you are coming from </p>" "<p> Unfortunately man I've been locked out of my Planet, Got  no place to go. mind recommending a place</p>" "<p> Okay man check the link for this planet, i think they've got some place</p>"

@app.route("/journal")
def home():
    return render_template('home.html')

@app.route("/scores/<int:scores>")
def scores_t(scores):
    return render_template("scores.html", marks=scores)


@app.route('/signup')
def register():
    return render_template('./form.html')

@app.route('/processor',methods=['POST'])
def processor():
    fname = request.form['fname']
    username = request.form['username']
    password = request.form['password'] 
    
database_name=[]
@app.route('/registeration',methods=['GET','POST'])
def collection():
    if request.method =='POST':
        fname = request.form['fname']
        age = request.form['age']
        address = request.form['address']
        Phonenumber = request.form['Phonenumber']
        database_name.append(fname)
        database_name.append(age)
        database_name.append(address)
        database_name.append(Phonenumber)
        return "Registration successful"

    return render_template('./form_age.html')


@app.route('/result')
def result():
    return render_template('/result.html',database_name=database_name)        

@app.route('/images')
def images():
    return render_template("images.html")

    

if __name__=='__main__':
    app.run(port=8000,debug=True)