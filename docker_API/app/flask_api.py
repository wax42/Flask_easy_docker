from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Flask"



@app.route("/testapic")
def testapic():
    return "testapic" 

@app.route("/speechtotext")
def speech():
    return "Speech to text"

@app.route("/sentiment")
def sentiment():
    return "Some beautiful sentiment"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
