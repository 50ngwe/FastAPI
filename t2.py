import psycopg2

con = psycopg2.connect(database="Cars", user="techadmin@test-fast-api-db", password="Mustwork!!", host="test-fast-api-db.postgres.database.azure.com", port="5432")

print("Database opened successfully")
