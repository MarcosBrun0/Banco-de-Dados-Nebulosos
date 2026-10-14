import os
from dotenv import load_dotenv
from arango import ArangoClient


load_dotenv()
db_password = os.getenv("DB_PASSWORD")
# Initialize the client for ArangoDB.
client = ArangoClient(hosts="http://localhost:8529")

# Connect to "_system" database as root user.
sys_db = client.db("_system", username="root", password=db_password)

# Create a new database named "test".
sys_db.create_database("test")

# Connect to "test" database as root user.
db = client.db("test", username="root", password="dijkstra")

# Create a new collection named "students".
students = db.create_collection("students")

# Add a persistent index to the collection.
students.add_index({'type': 'persistent', 'fields': ['name'], 'unique': True})

# Insert new documents into the collection.
students.insert({"name": "jane", "age": 39})
students.insert({"name": "josh", "age": 18})
students.insert({"name": "judy", "age": 21})

# Execute an AQL query and iterate through the result cursor.
cursor = db.aql.execute("FOR doc IN students RETURN doc")
student_names = [document["name"] for document in cursor]
