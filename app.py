import numbers

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/generate-triangle', methods=['POST'])
def generate_triangle():
    if request.method == "POST":
        inputVal = request.json.get('input')

        if inputVal is None:
            return jsonify({'message': 'Input required.'})

        length = len(inputVal)

        arr = []

        for i, digit in enumerate(inputVal):
            if i < length:
                line = digit + '0' * i
                arr.append(line)

        for i in range(length - len(arr)):
            line = '0' * (i + length)
            arr.append(line)

        return jsonify(arr)


@app.route('/generate-odd-number', methods=['POST'])
def generate_odd_number():
    if request.method == "POST":
        inputVal = request.json.get('input')

        if inputVal is None:
            return jsonify({'message': 'Input required.'})

        inputVal = int(inputVal)

        arr = []

        for i in range(0, inputVal):
            if i % 2 != 0:
                arr.append(i)

        return jsonify(arr)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


@app.route('/generate-prisma-number', methods=['POST'])
def generate_prisma_number():
    if request.method == "POST":
        inputVal = request.json.get('input')

        if inputVal is None:
            return jsonify({'message': 'Input required.'})

        inputVal = int(inputVal)
        arr = []

        for i in range(2, inputVal + 1):
            if is_prime(i):
                arr.append(i)

        return arr


if __name__ == '__main__':
    app.run(debug=True)
