import psycopg2

mydb = psycopg2.connect(
    database="nce@",
    user="postgres",
    password="nce123##",
    host="localhost",
    port=5432,
)
cursor = mydb.cursor()
print(cursor)
query = 'Select * from "nce"'
cursor.execute(query)
array = list(cursor.fetchall())
print(array)
print("give data is:")
for x in array:
    print(x)