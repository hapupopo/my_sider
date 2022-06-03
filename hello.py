from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return \
        '<h1 style="text-align: center">Hello, World!</h1>' \
        '<p> This is a new paragraph.</p>' \
        '<img width=300 src="https://media2.giphy.com/media/ho0xXatV7b3Fo1ZRXN/giphy.gif?cid=ecf05e47qnkzqepcqxccgw4d2xe8av3yqjyquk3f7bzqady8&rid=giphy.gif&ct=g"></img>'


@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    app.run(debug=True)