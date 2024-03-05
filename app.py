#app.py no ipynb

#set connection 
#flask might not run on localhost

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")

def hello():
    return "<h1>Hello World!!!</h1>" #make it bold

#set the host+port
if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) #0.0.0.0. all adresses
 