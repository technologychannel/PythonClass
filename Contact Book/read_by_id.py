from main import create_connection

### Create New Contact
con = create_connection()
cursor = con.cursor()
id = input("Enter id: ")
cursor.execute(f"SELECT * FROM  contacts WHERE id = {id}")
contcts = cursor.fetchall()
for i in contcts:
    print(i)
con.close()