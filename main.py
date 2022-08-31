from flask import Flask,render_template
app = Flask (__name__)

@app.route("/")
def hello():
    return render_template('home/index.html')
app.run(debug=True)