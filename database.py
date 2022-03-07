import psycopg2
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
import json

def conn():
    return psycopg2.connect(database="Cars", user="techadmin@test-fast-api-db", password="Mustwork!!", host="test-fast-api-db.postgres.database.azure.com", port="5432")

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

def update_one(reserve_id):
    reserve = reserve_id
    connection = conn()
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    cursor.execute('UPDATE public."Cars_Inventory" SET available="test" WHERE item_id='+reserve+';')
    connection.commit()

def handle_results(rows):
    columns = ('item_id', 'available', 'model', 'trim_level', 'color', 'price')
    results = []
    for row in rows:
        results.append(dict(zip(columns, row)))

    #return json.dumps(results, indent=2)
    return rows


