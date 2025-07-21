from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def squarenumber():
    if request.method=="POST":
        if request.form.get('num')==None:
            return render_template("squarenum.html")
        elif request.form.get('num')=="":
            return f"<h3>Invalid number</h3>"
        else:
            number = request.form.get("num")
            square = int(number) * int(number)
            return render_template("result.html",num=number,square=square)
    return render_template("squarenum.html")
        
if __name__ == "__main__":
    app.run(debug=True)