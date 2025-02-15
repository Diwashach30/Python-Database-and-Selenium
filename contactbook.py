import mysql.connector
import os

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mycontactbookdb"
)

##creating cursor object to execute queries

mycursor = mydb.cursor()

# ## display database connection is established or not
# if mydb.is_connected():
#     print("Database connection is established")
# else:
#     print("Database connection is not established")


## add new contact

# def add_contact():
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     phone = input("Enter phone: ")
#     query = "INSERT INTO contacts (name, age, phone) VALUES (%s, %s, %s)"
#     values = (name, age, phone)
#     mycursor.execute(query, values)
   
#     mydb.commit()
#     print("Contact added successfully")
    
# add_contact()
    
    
# view contacts
def view_contacts():
    query = "SELECT * FROM contacts"
    mycursor.execute(query)
    
    contacts = mycursor.fetchall()
    for contact in contacts:
        print(contact)
        
view_contacts()


# ##update contact
# def update_contact():
#     view_contacts()
#     id = input("Enter id: ")
#     name = input("Enter name: ")
#     age = input("Enter age: ")
#     phone = input("Enter phone: ")
#     query = "UPDATE contacts SET name = %s, age = %s, phone = %s WHERE id = %s"
#     values = (name, age, phone, id)
#     mycursor.execute(query, values)
#     mydb.commit()
#     print("Contact updated successfully")
    
##update_contact()

##delete contact
def delete_contact():
    view_contacts()
    id = input("Enter id: ")
    query = "DELETE FROM contacts WHERE id = %s"
    values = (id,)
    mycursor.execute(query, values)
    mydb.commit()
    print("Contact deleted successfully")
    
delete_contact()    