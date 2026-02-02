
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello and welcome to my web app!"

@app.route("/contact")
def contact():
    return "Please reach out to us at nnour@imudsolutions."

@app.route("/about")
def about():
    return "We are over 1000 members and fastest growing platform. \n"    "Our community is expanding at an unprecedented rate, and we are proud to announce that we have officially surpassed 1,000 active members"

if __name__ == "__main__":
    app.run(debug=True)
