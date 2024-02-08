import Polynomial
from waitress import serve
from flask import Flask, jsonify, request

def main():
    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def diff():
        try:
            function = request.args.get('function')
            value = "Error"
            if function is not None:
                value = Polynomial.getDerivative(function)
            response = jsonify({"name": value})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        except Exception as ex:
            response = jsonify({"name": "Error"})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response

    serve(
        app,
        host="0.0.0.0",
        port=5100,
        url_scheme='https'
    )


if __name__ == '__main__':
    main()
