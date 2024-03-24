#!/bin/bash

# Set your AWS credentials and region
export AWS_ACCESS_KEY_ID="Enter Access key"
export AWS_SECRET_ACCESS_KEY="Enter secret access key"
export AWS_DEFAULT_REGION="us-east-1"

# Set S3 bucket and folder paths
S3_BUCKET="2048game-bucket"
S3_FOLDER_PATH="2048"

# Set local directory on EC2 to copy files to
LOCAL_DIR="/home/ec2-user/2048"

# Create the local directory if it doesn't exist
mkdir -p $LOCAL_DIR

# Use AWS CLI to copy files from S3 to EC2
aws s3 sync s3://$S3_BUCKET/$S3_FOLDER_PATH $LOCAL_DIR

echo "Transfer complete."