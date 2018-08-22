import psycopg2

db_host = "plaza.c2wsmdjwnmys.us-west-2.rds.amazonaws.com"
db_name = "plaza"
db_user = "caesar"
db_pass = "Coco4658210."

def db_conn():
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print("Unable to connect to database")
    return conn

def db_data(conn, query):
    result = []
    print("Now executing: %s" % (query))
    cursor = conn.cursor()
    cursor.execute(query)
    raw = cursor.fetchall()
    for line in raw:
        result.append(line)
    return result