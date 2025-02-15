async function showAdvisorDialogue() {
    let major = await prompt("Are you in 'cs_major' or 'informatics_major'?");
    let completed = await prompt("Enter completed courses (comma-separated):").split(",").map(c => c.trim());

    // Apply course overrides
    let adjustedCompleted = await applyCourseOverrides(completed);
    
    // Get remaining courses
    let remaining = await getRemainingCourses(major, adjustedCompleted);

    let message = `You still need to take: \n${remaining.join("\n")}`;
    $gameMessage.add(message);
}
// NPC interaction
showAdvisorDialogue();
