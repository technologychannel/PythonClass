from main import create_connection

### Create New Contact
con = create_connection()
cursor = con.cursor()
id = input("Enter id: ")
cursor.execute(f"DELETE FROM  contacts WHERE id = {id}")
con.commit()
print("Record Deleted Successfully.")
con.close()