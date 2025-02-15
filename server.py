from flask import Flask, request, jsonify
app = Flask(__name__)
#store assignments data
assignments_data = {}

@app.route('/assignments', methods=['POST'])
def add_assignment():
    global assignments_data
    assignments_data = request.json
    return jsonify({"message": "Assignment data updated successfully"})

@app.route('/assignments', methods=['GET'])
def get_assignments():
    return jsonify(assignments_data)

if __name__ == '__main__':
    app.run(debug=True)

