import boto3

aws_access_key_id = 'ASIAYRPWO7O5KIHQE54I'
aws_secret_access_key = 'EZIlK/M84dyDV1gqY0Zp12k2QFL8audwz/xuEAh1'
region_name = 'us-east-1'
aws_session_token = 'FwoGZXIvYXdzEBoaDHNRnLCqP5iW+AsCACLAAVHewpyXOJ52B4ffpESE80OFAgF8JJc0QUg3tg/v22KmaNlp7jiNAsO4tKVdNFq4WLHiSwlVCCr6aYXEifXjcC41y8v2bXusd1uA09znnuTO8pMw60y34j+B5sNlhKkisg+D4e/LsEgcX9gEsjOBdM1L4h3pys2V+FgAprBX1DoUFKNMlDcD6D7/n3kCSYWbRxXTnvd1ml15Ri6mWW1BbELpbLFXpOrWhBHAoAosAbH3T/8qdkqwDC9D9nlK4eiSXyidpOClBjItP939uEtQBCHETRU7oBeu13v/no1h/8iitSzaNbICGvEuLMOBwLQVThTwDlLo'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name,
                  aws_session_token=aws_session_token)

 # Bucket names
bucket_names = ["samplesdatab00927718", "tagb00927718"]


# Function to create a bucket with retries
def create_bucket(s3_client, bucket_name, retries=2):
    for i in range(retries):
            s3_client.create_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} created successfully.")
            return True
    return False

# Create buckets with retries
for bucket_name in bucket_names:
    create_bucket(s3, bucket_name)