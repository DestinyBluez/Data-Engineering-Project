import boto3

# Set your AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Set the S3 bucket and file path
bucket_name = 'your-bucket'
file_path = 'data/MarketingDataset.csv'

# Create an S3 client
s3 = boto3.client('s3',
                  aws_access_key_id=aws_access_key_id,
                  aws_secret_access_key=aws_secret_access_key)

# Upload the file to S3 bucket
s3.upload_file(file_path, bucket_name, 'MarketingDataset.csv')
