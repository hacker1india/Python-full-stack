from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])

def index():
    if request.method=='POST':
        if request.form.get('names') and request.form.get('feedback') == None:
            return render_template("index.html")
        elif request.form.get('names') and request.form.get('feedback') == "":
            return f"<h3>Invalid number</h3>"
        else:
            names = request.form.get('names')
            feedback = request.form.get('feedback')
            return render_template("submit.html",names=names,feedback=feedback)
        
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)