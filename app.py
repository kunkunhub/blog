from flask import Flask
import time
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/wait')
def wait():
    time.sleep(10)
    return "OK"

if __name__ == "__main__":
    app.run(port=80, processes=True)
