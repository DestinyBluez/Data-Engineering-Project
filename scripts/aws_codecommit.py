import boto3
import subprocess

# Set your AWS credentials
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'

# Set the repository name and file path
repository_name = 'Data-Engineering-Project'
file_path = 'scripts/'

# Create a CodeCommit client
codecommit = boto3.client('codecommit',
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key)

# Create a new repository
response = codecommit.create_repository(repositoryName=repository_name)

# Get the repository URL
repository_url = response['repositoryMetadata']['cloneUrlHttp']


# Task 2: Generate the Reports and upload them to GitHub
# a. Clone the repository that you created in Task 1
repo_url = repository_url
subprocess.run(['git', 'clone', repo_url])

# b. Create a branch for this activity, Create a file with all the queries from the above tasks
repo_directory = 'your-repository'
branch_name = 'data-versioning'
file_name = 'reports.sql'

# Write your SQL queries to the file
with open(f'{repo_directory}/{file_name}', 'w') as file:
    file.write('--- SQL queries for the reports ---\n')
    file.write('-- Report 1: Right mode to contact the customers\n')
    file.write('SELECT * FROM contacts WHERE contacted = 1;\n')
    file.write('-- Report 2: Count of customers by profession, income, age, education\n')
    file.write('SELECT profession, income, age, education, COUNT(*) AS count FROM customers GROUP BY profession, income, age, education;\n')
    file.write('-- Report 3: Possibility of existing loans, credit history, etc.\n')
    file.write('SELECT loan, credit_history, COUNT(*) AS count FROM customers GROUP BY loan, credit_history;\n')
    file.write('-- Report 4: Possibility of customers contacted earlier who subscribed to term deposits\n')
    file.write('SELECT contacted_earlier, subscribed, COUNT(*) AS count FROM customers GROUP BY contacted_earlier, subscribed;\n')
    file.write('-- Report 5: Existing customers with no term deposits\n')
    file.write('SELECT * FROM customers WHERE subscribed = 0;\n')

# c. List the version history (commit history), status of the local repository
subprocess.run(['git', 'checkout', branch_name])
subprocess.run(['git', 'log'])

# d. Commit the file to the branch
subprocess.run(['git', 'add', f'{repo_directory}/{file_name}'])
subprocess.run(['git', 'commit', '-m', 'Added reports.sql'])

# e. Push the changes to GitHub
subprocess.run(['git', 'push', 'origin', branch_name])

