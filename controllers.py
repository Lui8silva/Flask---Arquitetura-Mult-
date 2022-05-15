from flask import render_template

class Index():
  def index():
    return render_template('index.html')

class CalcController():
  def mult(num1, num2):
    return f'Mult = {int(num1) * int(num2)}'