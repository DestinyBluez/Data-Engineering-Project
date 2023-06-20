import boto3

# Set your AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Create an EMR client
emr = boto3.client('emr',
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key)

# Create an EMR cluster
# ...

# Submit your data engineering tasks to the cluster
# ...

# Terminate the EMR cluster
# ...

