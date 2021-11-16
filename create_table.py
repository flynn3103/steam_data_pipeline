import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():

    conn = psycopg2.connect("host=localhost dbname=airflow user=airflow password=airflow")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS steam")
    cur.execute("CREATE DATABASE steam WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()
    conn = psycopg2.connect("host=localhost dbname=steam user=airflow password=airflow")
    cur = conn.cursor()
    return cur, conn

def drop_table(cur, conn):
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_table(cur,conn):
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    cur, conn = create_database()

    drop_table(cur, conn)
    print("Table dropped sucessfully!!")
    create_table(cur,conn)
    print("Table created successfully!!")

    conn.close()

if __name__ == '__main__':
    main()