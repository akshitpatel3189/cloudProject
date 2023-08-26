# Serverless application with AWS Lambda

In this project, we store data in the S3 bucket from the tech folder then trigger the lambda function to perform extraction of the Named entity and store this Named entity into a second S3 bucket in the form of .txt format. then using the second lambda function store this updated count of a Named entity in the DynamoDB database.

# Technology

**Programming language:** Python<br />
**IDE:** VS code<br />
**Cloud services:** S3, Lambda, DynamoDB<br />

# Detailed Steps:


**Step 1:** Create the first S3 bucket and upload the files from the tech folder.<br />

**Step 2:** When a file is available in the first bucket, trigger the "extractFeatures" Lambda function. This is the first Lambda function in the application. The "extractFeatures" function extracts the named entities from the file and creates a JSON array of named entities (Any word that starts with uppercase or all letters of the word are in uppercase, then can be considered as a named entity) in that file. For example, if "001.txt" contains entities like "Asia," "Soviet," or "Serbia," the JSON array created by the function should be: 
"001ne": {"Asia":1, "Soviet":1, ...}.<br />

**Step 3:** The JSON array created in Step 2 will be saved as "001ne.txt" in a new bucket.<br />

**Step 4:** Once a file is available in the second bucket, it triggers the "accessDB" Lambda function. This is the second Lambda function in the application. The "accessDB" function reads each named entity JSON file and updates the DynamoDB database table with two fields: key and value. For example, if "001ne.txt" contains "001ne": {"Asia":1, "Soviet":1, ...}, then this Lambda function will update a DynamoDB table where "Asia" will be a key and "1" will be the corresponding value.
