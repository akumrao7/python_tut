import psycopg2

def table():
    conn=psycopg2.connect(dbname="postgres", user="postgres", password="umrao777", host="localhost", port="5433")

    cursor=conn.cursor()
    cursor.execute('''create table employees(Name Text, ID int, Age int);''')
    print("Table Created Successfully")

    conn.commit()
    conn.close()

def data():
    conn=psycopg2.connect(dbname="postgres", user="postgres", password="umrao777", host="localhost", port="5433")

    cursor=conn.cursor()

    name=input("Enter Name: ")
    id=input("Enter id: ")
    age=input("Enter age: ")


    query='''insert into employees(Name, ID, Age) values(%s, %s, %s);'''
    cursor.execute(query, (name,id,age))
    # cursor.execute('''insert into employees(Name, ID, Age) values('Ram', 02, 29);''')
    print("Data Added Successfully")

    conn.commit()
    conn.close()

data()

# def extract():
#     conn=psycopg2.connect(dbname="postgres", user="postgres", password="umrao777", host="localhost", port="5433")
#
#     cursor=conn.cursor()
#     cursor.execute('''select * from employees;''')
#     # print(cursor.fetchone())
#     show=cursor.fetchone()
#     print(show[0])
#
#     conn.commit()
#     conn.close()
#
# extract()

