import numpy as np
from waitress import serve
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS


def getDerivative(polynomial):
    """
    Parses the given string (polynomial) and calculates it's derivative using linear transformations.

    Args:
        polynomial (string): A string representation of a polynomial.

    Returns:
        derivative (string): A string representation of the derivative of the given polynomial.
    """
    # Create coefficients matrix and the linear transformation matrix
    if polynomial.isdigit():
        return "0"
    size = 10000
    coeff = np.zeros(shape=(size, 1))
    shift = np.zeros(shape=(size, size))
    for i in range(size-1):
        shift[i][i+1] = i + 1
    # String preprocessing
    if polynomial[0] == "x":
        polynomial = "+1" + polynomial
    elif polynomial[0] == '-' or polynomial[0] == '+':
        polynomial
    else:
        polynomial = "+" + polynomial
    # Caclulate all coefficients and added them to their corresponding place in the coefficients matrix
    index = 0
    coeffTotal = 0
    for ch in range(len(polynomial)):
        if(polynomial[ch] == "x" and not polynomial[ch-1:ch-1].isdigit()):
            stri = ""
            if(ch+1 < len(polynomial) and polynomial[ch+1] == "^"):
                for ch2 in range(ch+2, len(polynomial)):
                    if(polynomial[ch2] == "{" or polynomial[ch2] == "}"):
                        continue
                    if not polynomial[ch2].isdigit():
                        break
                    stri += polynomial[ch2]
                index = int(stri)
            else:
                index = 1
            number = 0
            stri = ""
            for ch2 in reversed(range(0, ch)):
                if polynomial[ch2] == "-":
                    stri = "-"+stri
                if not polynomial[ch2].isdigit():
                    break
                stri = polynomial[ch2] + stri
            number = int(stri)
            coeffTotal += number
            coeff[index] += int(number)
    # Apply the linear transformation
    diff = np.matmul(shift, coeff)
    answer = ""
    # Construct the solutions matrix
    for x in reversed(range(len(diff))):
        if x == 0 and diff[x] > 0:
            answer += "+" + str(int(diff[x][0]))
        elif x == 0 and diff[x] < 0:
            answer += str(int(diff[x][0]))
        elif diff[x] > 0:
            answer += "+" + str(int(diff[x][0])) + "x^{" + str(x) + "}"
        elif diff[x] < 0:
            answer += str(int(diff[x][0])) + "x^{" + str(x) + "}"
    # Edge case where the derivative is zero
    if answer == "":
        answer = 0
    if answer[0] == "+":
        answer = answer[1:]
    # Return derivative
    return answer


def main():
    app = Flask(__name__)
    CORS(app)

    @app.route('/diff')
    def diff():
        # if key doesn't exist, returns None
        try:
            function = request.args.get('function')
            value = getDerivative(function)
            print(value)
            response = jsonify({"name": value})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response.json
        except Exception as ex:
            print(ex)
    serve(
        app,
        host="0.0.0.0",
        port=5000,
        url_scheme='https'
    )


if __name__ == '__main__':
    main()
