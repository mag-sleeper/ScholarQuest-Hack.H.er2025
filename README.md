# Hack(H)er413💻
Hack(H)er413 2025 Project

# 👾 ScholarQuest - An RPG-Based Academic Progress Tracker 

**ScholarQuest** is an **RPG-based academic planner** built with **RPG Maker**.  
It helps students track:
- 🎓 **Graduation requirements** (Major courses, GenEd, prerequisites)
- 📅 **Canvas assignments & deadlines** (via iCal `.ics` file)
- 🎖️ **Rewards system** (Pins, budgets, XP for completing assignments)

## Overview
Welcome to ScholarQuest! 🏫✨ This is an interactive project designed to help students track and manage their course requirements, schedules, and progress in a gamified way. Originally, we attempted to scrape course data from Canvas, but due to limitations like 2FA and the lack of Canvas API support, we pivoted to creating a custom Canvas Calendar system. This solution offers a more accurate and user-friendly way to display academic data. The project integrates a backend system to manage data and a frontend interface powered by RPG Maker, offering an immersive and interactive experience for students to track their academic journey and campus exploration.

## Features 🚀
- **Canvas Calendar**: Replaces the Canvas scraping approach. Instead of directly fetching data from Canvas, we implemented a custom calendar that tracks courses and requirements, providing an easier way to visualize academic progress. 📅
- **Web Scraping**: Initially used Playwright to scrape additional course data (GenEd and CS requirements) from Canvas but pivoted to using ICS files for data management after API issues. 🕸️
- **Course Management**: The demo includes real courses like ENGLWRIT112, LINGUIST101, CHEM111, and MICROBIO 140P, enabling students to track progress, GenEd requirements, and course completion. 📚
- **GenEd Tracking**: A GenEd requirement list that allows students to easily track which requirements they’ve satisfied, eliminating confusion about graduation requirements. 📜

## Technologies Used 🛠️
- **RPG Maker**: A game engine used to build an interactive campus map that allows students to explore and engage with their academic progress in a game-like format. 🎮
- **VSCode**: The preferred code editor for development. 🖥️
- **Python**: The main programming language for backend logic, including data extraction and server-side processing. 🐍
- **JavaScript**: Used for frontend development, handling dynamic interactions and campus map updates. 💻
- **JSON**: The format used for exchanging and managing course data between the backend and frontend. 📊
- **Playwright**: A tool used for web scraping to fetch GenEd and CS course data (initially), later replaced by ICS file integration. 🕵️‍♂️
- **Zsh & iTerm2**: Tools for managing shell and terminal environments efficiently. ⌨️ 

## Project Status ⚡
This project is actively being developed for a hackathon, with a demo deadline by February 16th at 8:30 AM. We switched from Canvas scraping to a custom Canvas Calendar and are in the final stages of integration and testing. 🎯 While the RPG Maker map currently only includes a small portion of the UMass campus (LGRT area), the full map is still in development. 

## Future Goals 🚀
- **Full Campus Map**: Expand the RPG Maker map to include the entire UMass campus, allowing students to explore all academic buildings, dorms, and event locations.
- **Routine Tracker**: Implement a feature to track students' routines, such as how many miles they walk and which locations they visit during the semester. This feature will encourage students to be more active on campus.
- **Improved Data Integration**: Further enhance the integration with Canvas and other student data systems to provide more real-time and accurate course and assignment data.
- **Enhanced Badging System**: Expand the badge rewards system to include additional milestones and challenges, such as completing GenEd requirements or attending a certain number of campus events.
- **User Profiles and Customization**: Enable students to create personalized profiles to track their academic and extracurricular progress, set goals, and see a history of their achievements.
- **Mobile App Integration**: In the future, we aim to integrate ScholarQuest into a mobile app to make it more accessible and interactive for students on the go, further enhancing the gamified experience.


