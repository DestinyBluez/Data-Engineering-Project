# Data Engineering – Final Assessment

## Business Scenario

DB Bank is a large public sector bank which has branches across the cities. It provides various services like savings account, current account, term deposits, personal loans, home loans etc. to customers. The bank conducts marketing campaigns to promote its schemes and tracks data related to customers' personal, social, and economic details. The recent campaign focused on marketing their term-deposit scheme.

## Challenges

The bank faces the challenge of targeting the right people for a successful campaign. The marketing team needs to analyze various customer details such as profession, income, age, education, existing loans, and credit history to determine their suitability for the term-deposit scheme.

## Project Tasks

### Data Discovery, Processing, Loading Task:

#### Task 1: Identify MongoDB Data Model and Populate Data

- Identify the data model in terms of database, collections, and documents for MongoDB.
- Populate the data from the CSV file into the MongoDB data store.

#### Task 2: Create Five Reports

- Generate reports based on the data analysis.
- Example report: "Right Mode to Contact Customers"

### Data Versioning Task:

#### Task 1: Create GitHub Repository and Upload Dataset

- Create a repository on GitHub.com.
- Upload the dataset to the repository using the GitHub website.

#### Task 2: Generate Reports and Upload to GitHub

- Clone the repository to your local machine.
- Create a branch for this activity and create a file with all the queries from the previous tasks.
- List the version history and status of the local repository.
- Commit the file to the branch and push the changes to GitHub.

### Cloud Data Engineering Tasks:

- Upload the dataset to AWS S3.
- Create an AWS managed MongoDB instance and generate the five reports.
- Create AWS CodeCommit repositories and follow the steps mentioned in the Data Versioning Task.
- Create an AWS EMR instance and perform data engineering tasks such as cleaning, removing unknown values, and imputing missing values.

## Data Dictionary

### Bank Client Data

- `custAge`: Age of the customer.
- `profession`: Type of job.
- `marital`: Marital status.
- `schooling`: Educational qualification.
- `default`: Has credit in default?
- `housing`: Has housing loan?
- `loan`: Has personal loan?

### Data Related with the Last Contact of the Current Campaign

- `contact`: Contact communication type.
- `month`: Last contact month of the year.
- `day_of_week`: Last contact day of the week.
- `campaign`: Number of contacts performed during this campaign and for this client.
- `pdays`: Number of days passed by after the client was last contacted from a previous campaign.
- `previous`: Number of contacts performed before this campaign and for this client.
- `poutcome`: Outcome of the previous marketing campaign.

### Data Related to Social and Economic Context Attributes

- `emp.var.rate`: Employment variation rate - quarterly indicator.
- `cons.price.idx`: Consumer price index - monthly indicator.
- `cons.conf.idx`: Consumer confidence index - monthly indicator.
- `euribor3m`: Euribor 3-month rate - daily indicator.
- `nr.employed`: Number of employees - quarterly indicator.

### Target Variable

- `responded`: Has the client subscribed a term deposit?


