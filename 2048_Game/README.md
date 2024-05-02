# 2048 Game

In this project, I created 2048 game which is running in local computer. Then migrate whole game into AWS cloud using various sevices. This project is showcase of how local game or any software migreated on the cloud.


There are different types of services are used to migrate the game. It follows as,

Compute: EC2
Storage: S3
Networking & Content Delivery: VPC
Developer Tools: Cloud Shell (AWS CLI)
Management & Governance: Cloud Formation

Here is Architecture Diagram

![Architecture Diagram](https://github.com/akshitpatel3189/cloudProject/assets/65401508/fbee91fd-1312-4c34-8efa-dd83d1aa774b)

To Run this project on AWS.

First create EC2 instance. Then add 2048Game.yml into Cloud Formation, it will create S3 bucktet, Internet Gateway and VPC. 
Now upload 2048 folder into S3 buctket and transfer it into EC2 instance. If this is not working then dierectly upload Folder into EC2 instance using AWS CLI. 
((Optional)Now create Load balancer and Auto Scallling group and connect with EC2 instance). 
Using public URL of EC2 instance you can run 2048 game in Cloud. 😊😊
