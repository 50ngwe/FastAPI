import psycopg2

#establishing the connection
conn = psycopg2.connect(database="Cars", user="techadmin@test-fast-api-db", password="Mustwork!!", host="test-fast-api-db.postgres.database.azure.com", port="5432")

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()