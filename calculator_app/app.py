from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    number1 = request.form['number1']
    number2 = request.form['number2']
    result = float(number1) + float(number2)
    return render_template('result.html', operation="addition", number1=number1, number2=number2, result=result)

@app.route('/subtract', methods=['POST'])
def subtract():
    number1 = request.form['number1']
    number2 = request.form['number2']
    result = float(number1) - float(number2)
    return render_template('result.html', operation="subtraction", number1=number1, number2=number2, result=result)

@app.route('/multiply', methods=['POST'])
def multiply():
    number1 = request.form['number1']
    number2 = request.form['number2']
    result = float(number1) * float(number2)
    return render_template('result.html', operation="multiplication", number1=number1, number2=number2, result=result)

@app.route('/divide', methods=['POST'])
def divide():
    number1 = request.form['number1']
    number2 = request.form['number2']
    if float(number2) == 0:
        return "Error: Cannot divide by zero."
    result = float(number1) / float(number2)
    return render_template('result.html', operation="division", number1=number1, number2=number2, result=result)

if __name__ == '__main__':
    app.run(debug=True)
