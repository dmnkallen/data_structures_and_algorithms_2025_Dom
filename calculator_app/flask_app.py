from flask import Flask, render_template, request

app = Flask(__name__)  # create the instance of the flask class

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])  # associating the POST method with this route
def calculate():

    # using the request method from flask to request the values that were sent to the server through the POST method
    value1 = request.form['value1']
    value2 = request.form['value2']
    operation = str(request.form['operation'])

    # convert the input to floating points
    value1 = float(value1)
    value2 = float(value2)

    # do the calculation
    if operation == 'add':
        result = value1 + value2
    elif operation == 'subtract':
        result = value1 - value2
    elif operation == 'divide':
        result = value1 / value2
    elif operation == 'multiply':
        result = value1 * value2
    else:
        return render_template('index.html',
                               printed_result='Operation must be one of "add", "subtract", "divide", or "multiply".')

    return render_template('index.html', printed_result=str(result))

if __name__ == "__main__":
    app.run(debug=True)