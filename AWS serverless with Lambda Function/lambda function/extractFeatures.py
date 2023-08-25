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
        
        # Extract named entities from the file content
        named_entities = {}
        for word in content.split():
            if word[0].isupper() or word.isupper():
                named_entities[word] = named_entities.get(word, 0) + 1
        
        # Create a JSON object with named entities
        json_object = {file_key + 'ne': named_entities}
        json_string = json.dumps(json_object)
        
        # Upload the JSON file to the new bucket
        new_bucket_name = 'tagb00927718'
        s3.put_object(Body=json_string, Bucket=new_bucket_name, Key=file_key.replace('.txt', 'ne.txt'))
    
    return {
        'statusCode': 200,
        'body': 'File saved.'
    }

def get_list(bucket_name):
    s3 = boto3.client('s3')
    response = s3.list_objects(Bucket=bucket_name)
    
    data_list = response['Contents'] if 'Contents' in response else []
    return data_list