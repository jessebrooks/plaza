import psycopg2
from db_util import db_conn, db_data

def get_person(event, context):
    query_cmd = "SELECT * FROM people"
    conn = db_conn()
    result = db_data(conn, query_cmd)
    conn.close()
    return result

def post_person(event, context)
    query_cmd = "INSERT INTO people(id_num, first_name, last_name) VALUES (DEFAULT," + event[1] + ", " + event[2] + ")"
    conn = db_conn()
    result = db_data(conn, query_cmd)
    conn.close()
    return result