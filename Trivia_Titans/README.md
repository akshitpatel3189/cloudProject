# Trivia_Titans

This project is a multi-cloud serverless online trivia game that allows users to form teams, compete against other teams in real-time, and track their progress on global and category-specific leaderboards. The game will provide a personalized experience by adapting to users' preferences and offering a diverse mix of questions tailored to their interests and skill levels. Additionally, administrators will have access to analytics tools for monitoring the game's performance and user engagement, enabling them to make data-driven decisions to improve the overall gaming experience.

# Technology

**Frontend:** React<br />
**Backend:** Flask Framework
**IDE:** VS code<br />
**Cloud services:**
| AWS | GCP |
|--|--|
| DynamoDB |  Firestore |
| Cognito | Cloud function |
| Lambda | Natural Language API |
| S3 | Cloud Run |
| Athena |
| QuickSight |
| SQS-SNS |
| Lex |



# Features:

1. User Authentication:
	• Sign up and log in using social media accounts or email addresses
	• Password recovery and reset if provided by the cloud service
	• Register the second factor (3 pre-defined questions and answers) to the NoSQL database, and run a code to access and validate the question answers.

2. User Profile Management:
	• Edit personal information (e.g. profile picture, name, and contact information, etc.)
	• View user statistics (e.g., games played, win/loss ratio, and total points earned)
	• View and manage team affiliations
	• View and compare achievements with other users

3. Team Management (Includes usage of AI):
	• Create a team with AI (artificial intelligence) generated team name
	• Invite other users to join the team // sending invitation
	• Accept or decline team invitations // sending acknowledgment
	• View team statistics (e.g., games played, win/loss ratio, and total points earned)
	• Manage team members (e.g., promote to admin, remove members, or leave the team)

4. Trivia Game Lobby:
	• Browse and join available trivia games created by administrators
	• Filter trivia games by category, difficulty level, or time frame
	• View game details, such as the number of participants, time remaining, and a short description

5. In-Game Experience:
	• Answer multiple-choice trivia questions within a specified time frame
	• View real-time team scores
	• Request and share hints with team members
	• View the correct answer and explanation after the time has elapsed for each question
	• Track individual and team performance

6. Leaderboards:
	• View global and category-specific leaderboards for teams and individual players
	• Filter leaderboards by time frame (e.g., daily, weekly, monthly, or all-time)
	• View detailed statistics for top-performing teams and players

7. Trivia Content Management (Administrators):
	• Add, edit, and delete trivia questions, including category and difficulty level
	• Create and manage trivia games with custom settings (e.g., categories, difficulty levels, and time frames)
	• Monitor and analyze gameplay data and user engagement

8. Automated Question Tagging:
	• Automatically tag each trivia question with relevant categories based on its content, such as sports, science, and general knowledge.

9. Virtual Assistance
	• Implement a chatbot to provide navigation support, dynamic database search for scores based on entered Team name

## Architecture Diagram:
![Cloud_Architecture](https://github.com/akshitpatel3189/cloudProject/assets/65401508/a8cd414d-6fff-49ca-bb67-4d16cd18b561)

### Contribution:
This is a group project consisting of 5 members. I have done this project as a part of my Master's degree to demonstrate real-time application using multi-cloud structure.

### Team Members

- Parth Champaneria
- Jainil Sevalia
- Raj Patel
- Akshit Patel
- Dhruv Kothari
