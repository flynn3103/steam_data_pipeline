import random
import string
import functools
import time
import mysql.connector
import argparse
import sys
from halo import Halo
from helper import percentage_calculator, rand_string_generator




def insert_rows(rows=100000):
    i = 0
    spinner.start()
    for i in range(1, int(rows) + 1):
        spinner.text = '{0}% - preparing sql statements..'.format(percentage_calculator(i, rows))
        name = rand_string_generator(size=3) + str(i)
        address = rand_string_generator(size=6) + str(i) + name
        insert_query = "INSERT INTO random_table (rand_column_1, rand_column_2) VALUES ('{}', '{}')".format(name,
                                                                                                            address)
        db_cursor.execute(insert_query)
    db.commit()
    spinner.succeed('preparing sql statements..')
    spinner.succeed("{}  - rows inserted to database".format(i))

if __name__ == '__main__':
    spinner = Halo(text='preparing sql statements..', spinner='dots')
    arg_parser = argparse.ArgumentParser("Script to insert random data to Mysql database.")
    arg_parser.add_argument("host", help="database hostname/ip")
    arg_parser.add_argument("username", help="database username")
    arg_parser.add_argument("password", help="database password")
    arg_parser.add_argument("database", help="database name to generate random data")
    arg_parser.add_argument("--rows", help="count of rows to be inserted to database.")
    if len(sys.argv) < 4:
        arg_parser.print_help()
        sys.exit(1)

    arguments = arg_parser.parse_args()
    db_host = arguments.host
    db_username = arguments.username
    db_password = arguments.password
    db_name = arguments.database
    db_rows = arguments.rows
    try:
        db = mysql.connector.connect(
            host=db_host,
            user=db_username,
            passwd=db_password,
            database=db_name
        )
        db_cursor = db.cursor()
        spinner.succeed("connected to MySQL server..")
        db_cursor.execute(
            "CREATE TABLE IF NOT EXISTS random_table "
            "(id BIGINT AUTO_INCREMENT PRIMARY KEY, rand_column_1 VARCHAR(255), rand_column_2 VARCHAR(255))")
        db.commit()
        spinner.succeed("created table..")
        insert_rows(rows=db_rows)
    except mysql.connector.errors.ProgrammingError as pro_e:
        if 'Unknown database' in pro_e.msg:
            spinner.fail("Error:  {}".format(pro_e))
        elif 'Access denied' in pro_e.msg:
            spinner.fail("Error:  {}".format(pro_e))
        else:
            spinner.fail("unknown error occurred: ".format(pro_e.msg))
    except mysql.connector.errors.DatabaseError as conn_e:
        if 'Unknown MySQL server host' in conn_e.msg:
            spinner.fail("Error:  {}".format(conn_e))
        else:
            spinner.fail("unknown error occurred: check the database server".format(conn_e.msg))