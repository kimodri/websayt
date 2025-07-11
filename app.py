from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def about():
    return render_template("about.html")

@app.route('/papers')
def papers():
    return render_template("papers.html")

if __name__ == '__main__':
    app.run(debug=True, port=5001)