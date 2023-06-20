import boto3

# Create an EMR client
emr_client = boto3.client('emr', region_name='us-west-2')  

# Configure the EMR cluster
emr_cluster = emr_client.run_job_flow(
    Name='DataEngineeringCluster',
    ReleaseLabel='emr-6.3.0',  
    Instances={
        'InstanceGroups': [
            {
                'Name': 'Master node',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm5.xlarge',  
            },
            {
                'Name': 'Core nodes',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm5.xlarge',  
            }
        ],
        'KeepJobFlowAliveWhenNoSteps': False,
        'TerminationProtected': False
    },
    Applications=[
        {'Name': 'Spark'},
        {'Name': 'Hadoop'},
        {'Name': 'Hive'},
        {'Name': 'Pig'}
    ],
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole',
    VisibleToAllUsers=True
)

# Get the ClusterId of the EMR cluster
cluster_id = emr_cluster['JobFlowId']
print(f'EMR Cluster created with ClusterId: {cluster_id}')

# Define the Spark script for data engineering tasks
spark_script = """
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# Create Spark session
spark = SparkSession.builder.appName('DataEngineeringTasks').getOrCreate()

# Load the dataset
df = spark.read.csv('s3://data-engg-project-bucket/MarketingDataset.csv', header=True, inferSchema=True)

# Task 1: Removing column values with unknown or null values and replacing with 0
df = df.fillna(0)

# Task 2: Identify & Remove duplicate values from the dataset
df = df.dropDuplicates()

# Task 3: Replace special characters from the dataset
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
for char in special_chars:
    df = df.withColumn('col_name', regexp_replace(col('col_name'), char, ''))

# Save the modified dataset
df.write.mode('overwrite').csv('s3://data-engg-project-bucket/processed-dataset.csv', header=True)

# Stop the Spark session
spark.stop()
"""

# Submit the Spark script to the EMR cluster
emr_client.add_job_flow_steps(
    JobFlowId=cluster_id,
    Steps=[
        {
            'Name': 'DataEngineeringTasks',
            'ActionOnFailure': 'CONTINUE',
            'HadoopJarStep': {
                'Jar': 'command-runner.jar',
                'Args': ['spark-submit', '--deploy-mode', 'cluster', '--master', 'yarn', '--conf', 'spark.yarn.submit.waitAppCompletion=true', '--conf', 'spark.driver.extraJavaOptions=-Dlog4j.configuration=log4j.properties', '--conf', 'spark.executor.extraJavaOptions=-Dlog4j.configuration=log4j.properties', '--conf', 'spark.executor.memory=2g', '--conf', 'spark.driver.memory=2g', '--conf', 'spark.executor.cores=1', '--conf', 'spark.driver.cores=1', '--conf', 'spark.executor.instances=3', '--conf', 'spark.driver.maxResultSize=4g', 's3://your-bucket/spark_script.py']
            }
        }
    ]
)
