from flask import Flask, url_for, render_template
import time
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/wait')
def wait():
    time.sleep(10)
    return "OK"

if __name__ == "__main__":
    app.run(port=80, threaded=True)
