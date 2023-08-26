import os
import time
import boto3

aws_access_key_id = 'ASIAYRPWO7O5KIHQE54I'
aws_secret_access_key = 'EZIlK/M84dyDV1gqY0Zp12k2QFL8audwz/xuEAh1'
region_name = 'us-east-1'
aws_session_token = 'FwoGZXIvYXdzEBoaDHNRnLCqP5iW+AsCACLAAVHewpyXOJ52B4ffpESE80OFAgF8JJc0QUg3tg/v22KmaNlp7jiNAsO4tKVdNFq4WLHiSwlVCCr6aYXEifXjcC41y8v2bXusd1uA09znnuTO8pMw60y34j+B5sNlhKkisg+D4e/LsEgcX9gEsjOBdM1L4h3pys2V+FgAprBX1DoUFKNMlDcD6D7/n3kCSYWbRxXTnvd1ml15Ri6mWW1BbELpbLFXpOrWhBHAoAosAbH3T/8qdkqwDC9D9nlK4eiSXyidpOClBjItP939uEtQBCHETRU7oBeu13v/no1h/8iitSzaNbICGvEuLMOBwLQVThTwDlLo'
BUCKET_NAME = 'samplesdatab00927718'
DELAY = 0.1  # 100 milliseconds

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name,
                  aws_session_token=aws_session_token)

# Local directory path
local_dir = r'F:\OneDrive - Dalhousie University\Dal Master\Summer Term\CSCI 5410 - Serverless Data Processing\Assignments\A3\tech'

# Function to upload files with a delay
def upload_files(bucket_name, local_dir, delay):
    for root, _, files in os.walk(local_dir):
        for file in files:
            file_path = os.path.join(root, file)
            s3_key = os.path.relpath(file_path, local_dir).replace("\\", "/")
            
            try:
                s3.upload_file(file_path, bucket_name, s3_key)
                print(f"Uploaded {file_path} to s3://{bucket_name}/{s3_key}")
            except Exception as e:
                print(f"Error uploading {file_path}: {e}")
            
            time.sleep(delay)

# Call the function to upload files with a delay
upload_files(BUCKET_NAME, local_dir, DELAY)
