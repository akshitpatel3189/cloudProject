# AWS VPC

This project builds a web application, deployed on an EC2 instance behind a Virtual Private Cloud (VPC) of AWS.


# Technology

**Programming language:** Python<br />
**IDE:** VS code, Postman<br />
**Cloud services:** EC2, VPC, Amazon RDS (Aurora MySQL)<br />


# Description:

The application running on EC2 will be public facing (accessible through a Public IP), and listen to POST requests to /store-products and GET requests to /list-products.

**/store-products** will:
	
 - Receive and parse a JSON body. 
 - Connect to an AWS RDS database server running on a private subnet inside your VPC. 	
 - Insert one record into the products table in the database for each item in the
   products array in the JSON body.
  - Return a status 200 code if everything works, or the appropriate HTML status code if there is an error or invalid input.

**/list-products** will:
	
 - Connect to the AWS RDS database running on the private subnet inside your VPC.
  - Query the products table and return a list of all products with status 200 code.

<br />
When you are finished the system will look and function like this:

![Screenshot 2023-08-26 151100](https://github.com/akshitpatel3189/cloudProject/assets/65401508/a247aff2-c755-4b85-b930-6376b0b1b0ce)
