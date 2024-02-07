import psycopg2

# Replace these variables with your actual database connection details
dbname = 'botdb'
user = 'user'
password = '12345678'
host = 'localhost'  


conn = psycopg2.connect(dbname=botdb, user=user, password=12345678, host=host)


cur = conn.cursor()



rows = cur.fetchall()
for row in rows:
    print(row)


cur.close()
conn.close()
