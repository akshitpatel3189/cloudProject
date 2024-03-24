#!/bin/bash

# Set your AWS credentials and region
export AWS_ACCESS_KEY_ID="ASIAZUA6JXKKLEAM6PVB"
export AWS_SECRET_ACCESS_KEY="KBWDyepbfdOdO33U/bRvo8m0VHntl4JTXN5iqP1G"
export AWS_SESSION_TOKEN="FwoGZXIvYXdzEA4aDLVN5v4Vkid3XDX6cSK9AdE7voZAIy82bI3odWJbv4Ye9bTZ3JSH3ldkHmCGlLky8U2qg8Mq9QvNYy4pO2/P/UwbgkHthMBsp5tKPC0fo9mPxnKc/L1E59gko1OOwSq8lS0E/XUeIllE8fM3NbbBuxAPJOcJZ/kbkbWh+VY2JuRT9q3fwOsFYmE5TGhSadZ5kkMvXg/wTt5OtDTjWkPADZF9BRLK2Z2mL33N4yM7OgrCHr3jPHZqwZqfZOrxRn16CYCB+oBJWWXa51+2+Cjh57irBjIt+B0RXB0fY4a4cEika1Yzpakei7MwHlvoXVI5DxhWgoVhxLUcPPzMeYzDHImW"
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