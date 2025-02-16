
/*:
 * @plugindesc RPG Advisor plugin for showing remaining courses and Gen Ed progress.
 * @author YourName
 *
 * @help This plugin allows the player to interact with an advisor and get information
 * about remaining courses and Gen Ed progress.
 *
 * @command ShowAdvisorDialogue
 * @text Show Advisor Dialogue
 * @desc Opens the advisor dialogue for course and Gen Ed progress.
 */
(function() {
    const API_URL = "http://127.0.0.1:5000"; // Flask server URL

    // 定义插件命令
    PluginManager.registerCommand('RPGAdvisor', 'ShowAdvisorDialogue', async function() {
        console.log("ShowAdvisorDialogue command triggered");

        const playerChoice = await new Promise((resolve) => {
            // 使用 RPG Maker MV 提示玩家选择
            const choice = confirm("Would you like to check:\n1. Remaining Courses\n2. Gen Ed Progress");
            resolve(choice ? "1" : "2");
        });

        console.log(`Player selected: ${playerChoice}`);

        switch (playerChoice) {
            case "1":
                showRemainingCourses();
                break;
            case "2":
                showGenEdProgress();
                break;
            default:
                alert("Invalid choice.");
        }
    });

    // 显示剩余课程
    async function showRemainingCourses() {
        console.log("Fetching remaining courses...");
        
        const response = await fetch(`${API_URL}/remaining_gen_ed`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ completed_courses: [] })
        });

        const data = await response.json();
        const message = `Remaining Courses:\n${data.result.join("\n")}`;
        $gameMessage.add(message);
    }

    // 显示 Gen Ed 进度
    async function showGenEdProgress() {
        console.log("Fetching Gen Ed progress...");
        
        const response = await fetch(`${API_URL}/remaining_gen_ed`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({})
        });

        const data = await response.json();
        
        let message = "Gen Ed Progress:\n";
        for (let category in data.result) {
            message += `${category}: ${data.result[category].join(", ") || "None"}\n`;
        }
        $gameMessage.add(message);
    }

})();