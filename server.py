from flask import Flask, request, jsonify
from canvas_calendar import fetch_calendar_events

app = Flask(__name__)
#store assignments data
assignments_data = {}

@app.route('/assignments', methods=['GET','POST'])
def get_assignment():
    global assignments_data
    if request.method == 'POST':
        assignments_data = request.json
        return jsonify({"message": "Assignment data updated successfully"})
    
    elif request.method == 'GET':
        assignment_data = {
            "title": assignments_data.get("title"),
            "due_date": assignments_data.get("due_date"),
            "assignment description": assignments_data.get("assignment description") 
        }
        print("📌 DEBUG: assignments_data =", assignments_data)
        return jsonify(assignment_data)


if __name__ == '__main__':
    app.run(debug=True)

