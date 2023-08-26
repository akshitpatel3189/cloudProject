# Textractor

Textractor is a simple web application that takes images that contain text from the user extract the text using AWS Textract services and send email notification of extracted Text.


# Technology

**Programming language:** Python<br />
**Framework:** Flask
**Cloud services:** Lambda, EC2, S3, API Gateway (REST API), SNS, Cloud Formation, Secrate manager<br />


# Description:

This simple web application where 4 tasks are involved
1. Registration and Login:
	The user first registers with name, email, and password. this data is stored in one session when the user starts registering. Then user login with the correct credentials
2. Upload image:
	After the user uploads images consisting of jpg, png, and jpeg format. These images are stored in an S3 bucket which is automatically created.
3. Text Extraction:
	Now lambda function triggers when a new file is inserted in the S3 bucket. The function passes the file to Textract. Textract extract text and send to lambda function.
5. Email notification:
	Now another lambda function receives extracted text and sends it to SNS which will send an email notification that contains the extracted Text

### Architecture diagram for the system:

![architecture](https://github.com/akshitpatel3189/cloudProject/assets/65401508/2a64be61-f02d-486c-b403-404026ba9b25)
