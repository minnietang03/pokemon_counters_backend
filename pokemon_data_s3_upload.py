import boto3


# Initialize S3 client
s3 = boto3.client('s3')

# Define bucket name and CSV file key
bucket_name = 'pokemon-counters'
local_csv_file = 'Pokemon Data.csv'  # Path to your local CSV file
s3_csv_file_key = 'Pokemon Data.csv'  # Key is the file path in the S3 bucket

# Upload CSV file to S3 bucket
try:
    s3.upload_file(local_csv_file, bucket_name, s3_csv_file_key)
    print(f"CSV file '{local_csv_file}' uploaded successfully to S3 bucket '{bucket_name}' with key '{s3_csv_file_key}'.")
except Exception as e:
    print(f"Error uploading CSV file to S3: {e}")
