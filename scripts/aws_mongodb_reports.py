import pymongo

# Set your MongoDB connection string
connection_string = 'mongodb://admin123:admin123@docdb-2023-06-20-13-26-04.cluster-cy7ttu6ib1ip.us-east-1.docdb.amazonaws.com:27017/?ssl=true&ssl_ca_certs=us-east-1-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false'

# Create a MongoDB client
client = pymongo.MongoClient(connection_string)

# Specify the database and collection names
database_name = 'my_database'
collection_name = 'my_collection'

# Access the MongoDB database and collection
db = client[database_name]
collection = db[collection_name]

# Report 1: Right mode to contact the customers
report1 = collection.aggregate([
    {'$group': {'_id': '$contact', 'count': {'$sum': 1}}},
    {'$sort': {'count': -1}}
])

# Report 2: Count of customers by profession, income, age, education
report2 = collection.aggregate([
    {'$group': {'_id': {'profession': '$profession', 'income': '$income', 'age': '$custAge', 'education': '$schooling'}, 'count': {'$sum': 1}}}
])

# Report 3: Possibility of existing loans and credit history
report3 = collection.aggregate([
    {'$group': {'_id': {'existing_loans': '$loan', 'credit_history': '$credit_history'}, 'count': {'$sum': 1}}}
])

# Report 4: Possibility of customers contacted earlier who subscribed to term deposits
report4 = collection.aggregate([
    {'$match': {'previous': {'$gt': 0}, 'responded': 'yes'}},
    {'$group': {'_id': {'contacted_earlier': '$previous'}, 'count': {'$sum': 1}}}
])

# Report 5: Existing customers with no term deposits
report5 = collection.find({'responded': 'no'})

# Print the reports
print('Report 1: Right mode to contact the customers')
for doc in report1:
    print(doc)

print('\nReport 2: Count of customers by profession, income, age, education')
for doc in report2:
    print(doc)

print('\nReport 3: Possibility of existing loans and credit history')
for doc in report3:
    print(doc)

print('\nReport 4: Possibility of customers contacted earlier who subscribed to term deposits')
for doc in report4:
    print(doc)

print('\nReport 5: Existing customers with no term deposits')
for doc in report5:
    print(doc)

# Close the MongoDB connection
client.close()
