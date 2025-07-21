from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    message = "hello everyone"
    return render_template("index.html",message=message)


# @app.route("/") #static
# def home():
#     return f"Hello, everyone"

# @app.route("/<username>") #dynamic routing for strings
# def home(username):
#     return f"Hello, everyone {username}"

# @app.route("/")#default route
# def default():
#     return f"This is default route"

# @app.route("/<path:username>") #dynamic routing for https 
# def home(username):
#     return f"Hello, everyone {username}"

# @app.route("/about") #static
# def about():
#     return "This is about page"

if __name__ =="__main__":
    app.run(debug=True) #debug=True for development
