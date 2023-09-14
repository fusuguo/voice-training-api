from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if not all(key in data for key in ('a', 'b')):
        return jsonify({"error": "Both 'a' and 'b' are required."}), 400

    result = data['a'] + data['b']
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
