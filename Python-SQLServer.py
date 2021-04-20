# Program to access a table Persons in the SQL Server database
import pyodbc

first_name = input("Enter the first name of the person to search: ")
last_name = input("Enter the last name of the person to search : ")
conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=SHUBHAM-HP\SQLEXPRESS;"
                      "Database=Test;"
                      "Trusted_Connection=yes;"
                     )
cursor = conn.cursor()
query = cursor.execute("select * from dbo.Customers where FirstName ='{fname}' and LastName = '{lname}'".format(1, fname = first_name,lname = last_name))
results = cursor.fetchall()

if len(results) > 0:
    for row in results:
        print("Id : %s"%row[0], "Name : {fname} {lname}".format(1, fname=row[1],lname=row[2]), "Email : %s"%row[3], sep="\n")
else:
    print("This person does not exist in our database.")
#print(results)

