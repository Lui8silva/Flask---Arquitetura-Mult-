from flask import Flask
from controllers import Index, CalcController

app = Flask('app')

@app.route('/')
def index():
    return Index.index()

@app.route('/mult/<num1>/<num2>')
def mult(num1, num2):
  return CalcController.mult(num1, num2)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)