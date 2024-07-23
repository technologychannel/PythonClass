from main import create_connection

### Create New Contact
con = create_connection()
cursor = con.cursor()
cursor.execute("SELECT * FROM  contacts")
contcts = cursor.fetchall()
for i in contcts:
    print(i)
con.close()