# Serverless application with Step Function

This project builds REST API entry points using serverless computing mechanisms. In this mechanism, It will create a State Machine, configured with an API gateway, which will evaluate a choice based on an input, and based on this choice, you will invoke a Lambda function, which will perform a hashing operation on a provided input data.


# Technology

**Programming language:** Python<br />
**Cloud services:** Lambda, Step function, API Gateway (REST API)<br />


# Description:

The application performs hashing in 3 ways SHA-256, MD5, and Bcrypt triggering the Lambda function through API Gateway with the help of the Step Function script.

Here is a rough state diagram for the system:

![Screenshot 2023-08-26 152055](https://github.com/akshitpatel3189/cloudProject/assets/65401508/b1e98c7f-7a67-4635-9077-c641b19f1614)
