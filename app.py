import pymongo
import os
import sys
import pprint

def main():
    connection_string = os.environ["MONGO_CONNECTION_STRING"]
    db_name = os.environ["MONGO_DBNAME"]
    
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collection = db['test'] #1. put the name of your collection in the quotes
    
    #2. add a document to your collection using the insert_one method
    person1 = {
        'name': 'Bob Smith',
        'birthdate': '01/02/2003',
    }
    collection.insert_one( person1 )
    
    #3. print the number of documents in the collection
    print( f"There are {collection.count_documents({})} documents in the collection.")
    
    #4. print the first document in the collection
    print( "\nThe first documnet in the collection is" )
    print( collection.find_one() )
    
    #5. print all documents in the collection
    print( "\nHere are all the doucments in the collection")
    for doc in collection.find():
        print( doc )
    
    #6. print all documents with a particular value for some attribute
    #ex. print all documents with the birth date 12/1/1990
    print( "\nAll the people born on 01/02/2003 are" )
    for doc in collection.find({ 'birthdate': '01/02/2003'}):
        print( doc )
    
if __name__=="__main__":
    main()