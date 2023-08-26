# Containerization with Docker

This project gives a basic understanding of how multiple Docker containers communicate with each other and the use of Docker compose files to run multiple containers simultaneously.


# Technology

**Programming language:** Python<br />
**IDE:** VS code, Postman<br />


# Description:

Build two simple web app containers that communicate with each other through a docker  
network to provide more complex functionality, a very small microservice architecture. When you are finished your system will look and function like this:

.![Screenshot 2023-08-26 143355](https://github.com/akshitpatel3189/cloudProject/assets/65401508/19826e23-ff86-4986-a563-58f6ed296c3b)

**Container 1**
The first container's role is to serve as an orchestrator and gatekeeper, making sure that the input into the system is clean and valid. It must:
   1. Listen on exposed port 6000 for JSON input sent via an HTTP POST to
    "/calculate", e.g. "http://localhost:6000/calculate"
    2. Validate the input JSON to ensure a file name was provided, if the "file" parameter is null, return the invalid JSON input result.
    3. Verify that the file exists, if it does not exist return the file not found error message.
    4. Send the "file" and "product" parameters to container 2 (you don't have to use JSON to do this, do it however you like, but I
    recommend JSON) and return the response from container 2.

**Container 2**
The second container's role is to listen on another port and endpoint that you define within your docker network for requests to calculate MD5 checksums. It must:
   1. Mount the host machine directory '.' to a docker volume
  	2. Listen on an endpoint/port you define to respond to calculate requests: 		
  	     a. Load the file.
  	     b. Parse the CSV file with a CSV  library.
  	     c. Calculate the sum of all rows matching the given product parameter.
  	     d. Return the sum in the appropriate JSON format, or an error indicating the file is not a proper CSV file in the appropriate JSON format.

Prepare a **docker-compose.yml** file that defines a docker network and runs the  
two containers from your docker hub.

### JSON Input

Your first container will receive JSON in the following format:
{
	"file": "file.dat",
	"product": "wheat"
}
The intent of the message is for your microservice architecture to perform a calculation and return a response. In this case, we want you to load the file, parse the file as a CSV file, and sum all values where the 'product' column matches the value passed in the product argument.

For example, if file.dat contained:
product, amount
wheat,10
wheat,20
oats,5
barley,6
The JSON above would cause your program to return 30 as the sum.


### JSON Output

If the filename provided via the input JSON is found, the calculation is performed
{
	"file": "file.dat",
	"sum": 30
}

If a filename is provided, but the file contents cannot be parsed due to not following the CSV format, this message is returned:
{
	"file": "file.dat",
	"error": "Input file not in CSV format."
}

If a filename is provided, but not found, this message is returned:
{
	"file": "file.dat",
	"error": "File not found."
}

If the file name is not provided, an error message is returned:
{
	"file": null,
	"error": "Invalid JSON input."
}
