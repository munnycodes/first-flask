from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello World... <h1> HELLO WORLD!<h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}, you're going to have a wonderful day!"

if __name__ == "__main__":
    app.debug = True
    app.run()