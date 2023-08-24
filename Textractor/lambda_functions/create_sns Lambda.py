import json
import boto3

def lambda_handler(event, context):
    # Initialize the boto3 client for SNS
    sns_client = boto3.client('sns', region_name='us-east-1') # replace with your region

    # Get the email from the POST request
    email = json.loads(event['body'])['email']

    # Create a new SNS topic
    response = sns_client.create_topic(Name='snsText')
    topic_arn = response['TopicArn']

    '''
    Adapted from
        https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html '''
    # Create an email subscription to the topic
    subscription = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol='email',
        Endpoint=email
    )

    # Return the ARN of the newly created SNS topic
    return {
        'statusCode': 200,
        'body': topic_arn
    }
