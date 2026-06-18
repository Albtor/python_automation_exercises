import boto3
from botocore.exceptions import NoCredentialsError
# pip install boto3
# pip install google-cloud
# pip install azure-mgmt-resource azure-storage-blob

# aws_access_key_id=YOUR_ACCESS_KEY
# aws_secret_access_key=YOUR_SECRET_KEY
# region=YOUR_AWS_REGION

def cloud_automation():
    s3 = boto3.client('s3')
    # upload file
    def upload_file(file_name, bucket_name, object_name=None):
        try:
            if object_name is None:
                object_name = file_name
                s3.upload_file(file_name, bucket_name, object_name)
                print(f"File '{file_name}' uploaded to '{bucket_name}/{object_name}'.")
        except NoCredentialsError:
            print("Credentials not available.")

    # Download a file
    def download_file(bucket_name, object_name, file_name):
        try:
            s3.download_file(bucket_name, object_name, file_name)
            print(f"File '{object_name}' downloaded from '{bucket_name} to {file_name}'.")
        except NoCredentialsError:
            print("Credentials not available.")

    # list files
    def list_files(bucket_name):
        try:
            response = s3.list_objects_v2(Bucket=bucket_name)
            print(f"Files in S3 bucket")
            for obj in response.get("Contents",[]):
                print(f"{obj['Key']}")
        except NoCredentialsError:
            print("Credentials not available.")

    # delete a file
    def delete_file(bucket_name, object_name):
        try:
            s3.delete_object(Bucket=bucket_name, Key=object_name)
            print(f"File '{object_name}' deleted from '{bucket_name}'")
        except NoCredentialsError:
            print("Credentials not available.")

    # example usage
    bucket_name = 'your_bucket_name'
    file_to_upload = 'local_file.txt'
    object_name = 'uploaded_file.txt'

    # use of methods
    upload_file(file_to_upload, bucket_name, object_name)
    list_files(bucket_name)
    download_file(bucket_name, object_name)
    delete_file(bucket_name, object_name)