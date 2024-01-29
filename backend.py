from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pap', methods=['POST'])
def den():
    # Accessing request data
    data = request.json
    # Process the data (for demonstration, just echoing back)
    return jsonify(data)

@app.route('/', methods=['GET'])
def hello():
    return 'hello'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
