import grpc
import computeandstorage_pb2
import computeandstorage_pb2_grpc
import boto3
import botocore.exceptions
from concurrent import futures

class EC2OperationsServicer(computeandstorage_pb2_grpc.EC2OperationsServicer):
    def __init__(self):
        
        # Authenticate with AWS using access key, secret key, and region
        session = boto3.Session(
            aws_access_key_id ='Enter access key here',
            aws_secret_access_key ='Enter secret access key here',
            aws_session_token ='enter session token', #this is optional. I used AWS acadamy so I have to add this filed. If you are using persional account then delete this field
            region_name = 'us-east-1'
        )
        self.s3_client = session.client('s3')
        self.bucket_name = 'a2cloud'
        self.file_name = 'a2.txt'

        # Create S3 bucket if it doesn't exist
        if not self._check_bucket_exists():
            self._create_bucket()

    def StoreData(self, request, context):
        # Store the data in the S3 file
        data = request.data.encode('utf-8')

        self.s3_client.put_object(Bucket=self.bucket_name, Key=self.file_name,Body=data)

        # Generate the public S3 URL
        s3uri = f"https://{self.bucket_name}.s3.us-east-1.amazonaws.com/{self.file_name}"

        # Return the StoreReply message with the S3 URL.
        return computeandstorage_pb2.StoreReply(s3uri=s3uri)

    def AppendData(self, request, context):
        # Retrieve the existing file contents
        response = self.s3_client.get_object(Bucket=self.bucket_name, Key=self.file_name)

        existing_data = response['Body'].read().decode('utf-8')

        # Append the new data
        new_data = request.data.encode('utf-8')
        appended_data = existing_data + new_data.decode('utf-8')

        # Overwrite the existing file with the appended data
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=self.file_name,
            Body=appended_data.encode('utf-8')
        )

        # Since AppendReply message has no fields, no need to return anything.
        return computeandstorage_pb2.AppendReply()

    def DeleteFile(self, request, context):
        try:
            # Delete the file from S3
            self.s3_client.delete_object(Bucket=self.bucket_name,Key=self.file_name)
            
        except botocore.exceptions.ClientError as e:
            error_code = e.response.get("Error", {}).get("Code")
            if error_code == "404":
                # Handle the case where the file does not exist
                context.abort(404, "File not found")
                return computeandstorage_pb2.DeleteReply()
            
        except Exception as e:
            # Handle any other exceptions that occur during the deletion process
            print(f"Error deleting file from S3: {str(e)}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return computeandstorage_pb2.DeleteReply()

        # Successful deletion, return empty DeleteReply message
        return computeandstorage_pb2.DeleteReply()

    def _check_bucket_exists(self):
        response = self.s3_client.list_buckets()
        buckets = response['Buckets']
        for bucket in buckets:
            if bucket['Name'] == self.bucket_name:
                print("Bucket Exists")
                return True
        return False

    def _create_bucket(self):
        self.s3_client.create_bucket(Bucket=self.bucket_name)
        print("Bucket Created")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    computeandstorage_pb2_grpc.add_EC2OperationsServicer_to_server(EC2OperationsServicer(), server)
    #server.add_insecure_port('[::]:50051')
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
