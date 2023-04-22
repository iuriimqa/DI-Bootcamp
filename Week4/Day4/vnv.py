import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'admin'
DATABASE = 'hollywood'

connection = psycopg2.connect(host = HOSTNAME,user = USERNAME, password = PASSWORD, dbname = DATABASE)