from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Application!"

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(debug=True)