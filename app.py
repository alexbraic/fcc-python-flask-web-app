from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  welcome = 'Oh, hi!'

  return welcome

app.run(host='0.0.0.0',debug=True)