import boto3
import json

def lambda_handler(event, context):
    # Get the bucket and object information from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    data_list = get_list(bucket_name)
    
    for file_info in data_list:
        file_key = file_info['Key']
        
        # Read the file contents from S3
        s3 = boto3.client('s3')
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        
        # Extract the named entity JSON
        named_entities = json.loads(content)
        
        # Update the DynamoDB table
        db_table(named_entities)
    
    return {
        'statusCode': 200,
        'body': 'Data inserted in DB'
    }

def get_list(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects(Bucket=bucket_name)
    
    data_list = response['Contents'] if 'Contents' in response else []
    return data_list

def db_table(named_entities):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ag3db')  # Replace with your actual DynamoDB table name

    for key, value in named_entities.items():
        for entity, entity_value in value.items():
            print(f"Entity Key: {entity}")
            # Check if the named entity already exists in the table
            response = table.get_item(
                Key={
                    'key': entity
                }
            )
            item = response.get('Item')

            if item:
                # Named entity exists, increment the value
                table.update_item(
                    Key={
                        'key': entity
                    },
                    UpdateExpression='SET #val = #val + :inc',
                    ExpressionAttributeNames={
                        '#val': 'value'
                    },
                    ExpressionAttributeValues={
                        ':inc': entity_value
                    }
                )
            else:
                # Named entity doesn't exist, insert with initial value
                table.put_item(
                    Item={
                        'key': entity,
                        'value': entity_value
                    }
                    )