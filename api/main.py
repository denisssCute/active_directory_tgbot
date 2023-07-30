from flask import Flask, jsonify
import connector


app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    data = connector.get()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=999, debug=False)
