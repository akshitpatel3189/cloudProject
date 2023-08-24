import boto3
import json

topic_name = 'snsText'
region = 'us-east-1'  # your region
aws_account_id = '138927234469'

def lambda_handler(event, context):
    # Get the S3 bucket and key from the event
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_key = event['Records'][0]['s3']['object']['key']

    # Initialize the Amazon Textract client
    textract_client = boto3.client('textract')

    # Call Amazon Textract to extract text from the image
    response = textract_client.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': s3_bucket,
                'Name': s3_key
            }
        }
    )

    # Extracted text from the response
    extracted_text = ""

    '''
    Adapted from
        https://docs.aws.amazon.com/textract/latest/dg/lambda.html '''
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            extracted_text += item['Text'] + "\n"

    sns_topic_arn = f'arn:aws:sns:{region}:{aws_account_id}:{topic_name}'

    # Initialize the Amazon SNS client
    sns_client = boto3.client('sns')

    # Publish the extracted text to the SNS topic
    sns_client.publish(
        TopicArn=sns_topic_arn,
        Message=extracted_text,
        Subject='Text Extracted from Image'
    )

    return {
        'statusCode': 200,
        'body': 'Text extraction and notification sent successfully.'
    }
