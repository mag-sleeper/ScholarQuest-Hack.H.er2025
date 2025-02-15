async function loadCourseData(){
    return fetch("www/data/grad_requirements.json")
    .then(response => response.json())
    .catch(error => console.error("Error loading course data:", error));
}

async function applyMajorRules(completedCourses){
    let data = await loadCourseData();
    let overrides = data.cs_major.overrides;
    let adjustCompleted = [...completedCourses];

    completedCourses.forEach(course => {
        if (overrides[course]){
            let overridenCourses = overides[course];
            overridenCourses.forEach(overridenCourse => {
                if (!adjustCompleted.includes(overridenCourse)){
                    adjustCompleted.push(overridenCourse);
                }
            });
        }
    });
    return adjustedCompleted;

}
async function getRemainingCourses(major, completedCourses){
    let data = await loadCourseData();
    let requiredCourses = data[major].core.concat(data[major.electives]);
    let remainingCourses = requiredCourses.filter(course => !completedCourses.includes(course));
    return remainingCourses;
}

async function checkPrerequisites(selectedCourses, completedCourses){
    let data = await loadCourseData();
    let major = "cs_major";
    let prerequisites = data[major].prerequisites;

    if (selectedCourse in prerequisites){
        let required = prerequisites[selectedCourse];
        let missing = required.filter(req => !completedCourses.includes(req));
        
        if (missing.length >0){
            return 'You cannot take ${selectedCourse} yet. We recommend taking: ${missing.join(", ")} first.';
        }
    }
    return 'You can enroll in ${selectedCourse}';
}
