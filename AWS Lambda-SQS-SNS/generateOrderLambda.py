import random
import boto3

# Predefined lists of car types, car accessories, and delivery addresses
CAR_TYPES = ["Toyota Supra Mark IV", "Nissan Skyline GT-Rs", "Dodge Charger Daytona", "Nissan 350Z"]
ACCESSORIES = ["Nitro", "Performance fuel pump", "V12 Engine", "All accessories"]
CLIENT_ADDRESSES = ["Franschhoek, 7690, South Africa", "Yas Marina Circuit, Yas Island, Abu Dhabi", "964-0088 Fukushima, Nihommatsu, Sawamatsukura, Japan"]

def lambda_handler(event, context):
    # Randomly select car type, car accessory, and delivery address
    car_type = random.choice(CAR_TYPES)
    accessory = random.choice(ACCESSORIES)
    address = random.choice(CLIENT_ADDRESSES)

    # Publish the generated order details to the three SQS queues
    sqs_client = boto3.client('sqs')

    # Send car type, accessory, and address in a single message to the respective queues
    order_message = f"Car Type: {car_type}, Accessory: {accessory}, Delivery Address: {address}"

    # Send order details to the CarTypeQueue
    car_type_queue_url = 'https://sqs.us-east-1.amazonaws.com/587316788154/CarTypeQueue'
    sqs_client.send_message(QueueUrl=car_type_queue_url, MessageBody=order_message)

    # Send order details to the AccessoryQueue
    accessory_queue_url = 'https://sqs.us-east-1.amazonaws.com/587316788154/AccessoryQueue'
    sqs_client.send_message(QueueUrl=accessory_queue_url, MessageBody=order_message)

    # Send order details to the AddressQueue
    address_queue_url = 'https://sqs.us-east-1.amazonaws.com/587316788154/AddressQueue'
    sqs_client.send_message(QueueUrl=address_queue_url, MessageBody=order_message)

    # Publish the generated order details to the SNS topic (optional)
    sns_client = boto3.client('sns')
    sns_topic_arn = 'arn:aws:sns:us-east-1:587316788154:HalifaxTxiOrders'
    sns_client.publish(TopicArn=sns_topic_arn, Message=order_message)

    return {
        'statusCode': 200,
        'body': 'Order generated and sent to SQS queues.'
    }