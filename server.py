from flask import Flask, request, jsonify
from canvas_calendar import fetch_calendar_events
import json

app = Flask(__name__)

with open("graduation_requirements.json") as f:
    graduation_requirements = json.load(f)

def check_gen_ed_requirements(req, completed_cor, current_cor, remaining_cor):
    remaining_cor = {}
    
    all_courses = completed_cor + current_cor
    
    for category, category_data in req["general_education"].items():
        unsatisfied_courses = [course for course in category_data["courses"] if course not in all_courses]
        if unsatisfied_courses:
            remaining_cor[category] = unsatisfied_courses
    
    return remaining_cor

@app.route('/remaining_gen_ed', methods=['POST'])
def remaining_gen_ed():
    data = request.json
    completed_cor = data.get('completed_courses', [])
    current_cor = data.get('current_semester_courses', [])
    
    remaining_cor = check_gen_ed_requirements(graduation_requirements, completed_cor, current_cor, remaining_cor)
    
    return jsonify(remaining_cor)
    
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
            "due_date": assignments_data.get("due_date")
        }
        print("📌 DEBUG: assignments_data =", assignments_data)
        return jsonify(assignment_data)
    
if __name__ == '__main__':
    app.run(debug=True)

