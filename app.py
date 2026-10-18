from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "test the ci pipeline"
@app.route("/gate")
def gate():
    return("Exit the world!")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
