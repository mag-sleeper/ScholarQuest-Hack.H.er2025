from flask import Flask, request, jsonify
from canvas_calendar import fetch_calendar_events

app = Flask(__name__)
#store assignments data

graduation_requirements = {
    "general_education": {
        "writing": {
            "courses": ["ENGLWRIT112", "Junior Year Writing"]
        },
        "math": {
            "courses": ["R1 - Basic Math", "R2 - Analytical Reasoning"]
        },
        "science": {
            "courses": ["BS - Biological Science", "PS - Physical Science"]
        },
        "social_world": {
            "literature_arts": {
                "courses": ["AL - Literature", "AT - Theatre", "ART - Design"]
            },
            "historical_studies": {
                "courses": ["HS - Historical Studies"]
            },
            "social_behavioral": {
                "courses": ["SB - Social and Behavioral Sciences"]
            },
            "additional_social_world": {
                "courses": ["AL/AT/SB or Interdisciplinary (I or SI)"]
            },
            "diversity": {
                "us_diversity": ["DU - Diversity in the US"],
                "global_diversity": ["DG - Global Diversity"]
            }
        },
        "integrative_experience": {
            "courses": ["3 credits (Major Specific)"]
        }
    }
}

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

def remaining_gen_ed(requirements, completed_courses, current_courses, remaining_courses):
    remaining_courses = {}
    all_course = completed_courses + current_courses
    for category



if __name__ == '__main__':
    app.run(debug=True)

