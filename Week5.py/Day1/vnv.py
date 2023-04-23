import psycopg2
from datetime import date

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'admin'
DATABASE = 'hollywood'

connection = psycopg2.connect(host = HOSTNAME,user = USERNAME, password = PASSWORD, dbname = DATABASE)

# query = "select * from actors"
# with connection.cursor() as cursor:
#     cursor.execute(query)
#     result = cursor.fetchall()


# print(result)

f_name = 'Brad'
l_name = 'Pitt'
age = date(1970, 1, 1)
num_oscars = 2

q = f"insert into actors (first_name, last_name, age, number_oscars) values ('{f_name}', '{l_name}', '{age}', {num_oscars});"


def select_columns(columns: list[str], table_name: str) -> str:
    start = 'select '

    columns_str = ", ".join(columns)

    end = f' from {table_name}'

    query = start + columns_str + end
    return query


def run_change_query(query: str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        connection.commit()


run_change_query(q)

