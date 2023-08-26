# Build gRPC server with AWS

This project will build a gRPC server with AWS services, deployed on an EC2 instance with S3 Bucket.


# Technology

**Programming language:** Python<br />
**IDE:** VS code, Postman<br />
**Framework:** gRPC<br />


# Description:

Run the gRPC protocol buffer file computeandstorage.proto to initiate the gRPC server.
 these steps are followed for the running of the project.
 
![Screenshot 2023-08-26 145644](https://github.com/akshitpatel3189/cloudProject/assets/65401508/a44013f7-f2b0-4c92-a861-47b239a1c783)
 
 JSON your gRPC server sends to app's /start
Your app will send me the following JSON in your POST to /start

{
	"Start": "Hi"
}

Request message sent to your app's StoreData

{
	"data": "A string you must store in a file on S3"
}

Your app's response message to StoreData method:
When a request message is sent to your app's StoreData, after you create the file on S3 you must return the following response message:

{
	"s3uri": "Public URL of the S3 file you created"
}

Request message sent to your app's AppendData

{
	"data": "string to append to the existing file on S3"
}

Request message sent to your app's DeleteFile
{
	"s3uri": "Public URL of the S3 file you created"
}
