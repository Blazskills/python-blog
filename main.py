from flask import Flask

app = Flask(__name__) #global context

@app.route("/yemi")
def index():
    retun "Hello Alaye"

if __name__="__main__":
    app.run()
