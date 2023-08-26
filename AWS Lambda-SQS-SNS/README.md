# AWS Lambda-SQS-SNS

This project gives basic information on how to use SQS and SNS services with Lambda function. As lambda function perform task which is in SQS and send notification using SNS services.

# Technology

**Programming language:** Python<br />
**IDE:** VS code<br />
**Cloud services:** SQS, SNS, Lambda<br />

# Detailed Steps:

1. A Lambda Function randomly generates customer orders by selecting car types (Compact, Mid-size Sedan, SUV, etc.), car accessories (GPS, Camera, etc.), and delivery addresses from predefined lists. The customer orders are split into three separate messages, each containing information about car type, car accessories, and street address. These messages are then added to three standard SQS queues: one for car types, another for car accessories, and the third for delivery addresses. select one item from each list and send it to 3 SQS queue

2. Order Checking: The user periodically checks the three SQS queues every 2 minutes using a Lambda Function to see if there are any orders waiting for processing.

3. Notification Service: When an order message is available in any of the SQS queues, a notification service (SNS) is triggered. The SNS sends the order details to the subscribed email.
