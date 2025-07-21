from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)
@app.route('/index')
def index():
    message = "this is index page"
    return render_template("index.html",message = message)

@app.route("/home")
def home():
    message = "this is home page"
    return render_template("home.html",message=message)

@app.route("/data/<username>")
def data(username):
    if username =="index":
        return redirect(url_for('index'))
    elif username == "home":
        return redirect(url_for('home'))
    else:
        return f" {username} invalid username"
    

@app.route("/if")
def if_example():
    message = "if_example"
    return render_template("if_example.html",message=message)



@app.route("/for")
def for_example():
    course = ["python","java","c++","flask","django"]
    return render_template("for_example.html",course=course)



if __name__ == "__main__":
    app.run(debug=True)