# import pymongo
# from urllib.parse import quote_plus

# username = quote_plus("layerasps8z")
# password = quote_plus("MYPASSWORDisnetrual")
# cluster = "chapo-bot3.odmsslj.mongodb.net"
# dbname = "chapo_db"
# uri = f"mongodb+srv://{username}:{password}@{cluster}/{dbname}?retryWrites=true&w=majority"

# # Create MongoDB client
# client = pymongo.MongoClient(uri)

# # Get collection data
# result = client[dbname]["logs"].find()

# # Print results
# for doc in result:
#     print(doc)



from urllib.parse import quote_plus

# Original password
password = "MYPASSWORDisnetrual"  # Replace with your actual password if different

# URL-encode the password
encoded_password = quote_plus(password)

print(encoded_password)
