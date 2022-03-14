import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
import json

#db connection
def conn():
    conn = psycopg2.connect(database="Cars", user="techadmin@test-fast-api-db", password="Mustwork!!", host="test-fast-api-db.postgres.database.azure.com", port="5432")
    conn.autocommit = True
    return conn
    
def fetch_one(field, value):
    where_q = field+"='"+value+"'"
    connection = conn()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT item_id, available, model, trim_level, color, price FROM public."Cars_Inventory" WHERE '+where_q+';')
    rows = cursor.fetchall()
    return handle_results(rows)
    
def fetch_all():
    connection = conn()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT item_id, available, model, trim_level, color, price FROM public."Cars_Inventory";')
    rows = cursor.fetchall()
    return handle_results(rows)

#change car availability status
def update_one(item_id):
    try:
        connection = conn()
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        #cursor = connection.cursor()
        sql_update_query = """UPDATE public.\"Cars_Inventory\" SET available=%s WHERE item_id=%s"""
        cursor.execute(sql_update_query, ('Not Available', item_id))
        #connection.commit()
        count = cursor.rowcount
        print(count, "Record Updated successfully ")
        return {"status": "SUCCESS", "message": format(count) + " Record Updated successfully"}

    except (Exception, psycopg2.Error) as error:
        print("Error in update operation", error)
        return {"status": "ERROR", "message": "Error in update operation"}

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

def handle_results(rows):
    columns = ('item_id', 'available', 'model', 'trim_level', 'color', 'price')
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))

    #return json.dumps(results, indent=2)
    return rows


