import mysql.connector
import random
import string

# Generate a random database name
# random_suffix = ''.join(random.choices(string.ascii_lowercase, k=8))
# database_name = f'mydatabase_{random_suffix}'

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Datascience_2023',
    database = 'mydatabase'
)

# # Check connection ###################
# if mydb.is_connected():
#     print("Connection is established")

mycursor = mydb.cursor()

# # Attempt to create the database ####################
# try:
#     mycursor.execute(f"CREATE DATABASE {database_name}")
#     print(f"Database '{database_name}' created.")
# except mysql.connector.Error as err:
#     if err.errno == 1007:
#         # Database already exists, ignore the error
#         print(f"Database '{database_name}' already exists.")
#     else:
#         # Another error occurred, print the error
#         print(f"Error: {err}")

# # Fetch and print the list of databases
# mycursor.execute("SHOW DATABASES")

# print("\nList of databases:")
# for i in mycursor:
#     print(i)

# mycursor.execute("USE mydatabase")

# # Close the cursor and the connection
# mycursor.close()
# mydb.close()


# # ############## CREATE  ##################
# Create Table (only one table per name)
# mycursor.execute('Create TABLE customers (name VARCHAR(255), address VARCHAR(255))')
# mycursor.execute('Create TABLE Products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR (255))')

# # ALTER TABLE
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# print("Table 'customers' created")

# Show tables
# mycursor.execute("SHOW TABLES")
# print("\nList of tables:")
# for x in mycursor:
#     print(x)

# # ################ INSERT ###############
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21") # insert one row only
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean Boulevard 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]

# mycursor.execute(sql, val) # (only for one row)
# mycursor.executemany(sql, val)

# # Commit the changes
# mydb.commit()

# print(mycursor.rowcount, 'record wer inserted')

# # Get inserted ID
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)

# mydb.commit()
# print(" 1 record inserted, ID:", mycursor.lastrowid)


# ######### SELECT ############
# Select from a Table and Selecting Columns
# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# # Select Columns
# mycursor.execute("SELECT name, address FROM customers")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # Select one row only (return the first row in table)
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)

# # ################# MYSQL WHERE #####################
# # Select with a filter
# sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# # Wildcard Characters
# sql = "SELECT * FROM customers WHERE address LIKE '%WAY%'"

# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # SQL Injection Prevention (cyber security)
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2",)

# mycursor.execute(sql,adr)
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # # ######### MYSQL ORDER BY ############
# # Sort the result ascending order

# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# # Sort the result ascending order

# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# # # ##### MYSQL DELETE AND DROP TABLE ########3
# # Delete Record
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# # Prevent SQL injection
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2",)

# mycursor.execute(sql, adr)

# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

# # Drop a table and drop Only if exist
# sql = "DROP TABLE users"
# mycursor.execute(sql)

# # # ============ MYSQL UPDATE =====================
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# # Prevent SQL Injection

# sql = "UPDATE customers SET address = %s where address = %s"
# val = ("Valley 345", "Canyon 123")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record(s) affected")

# # Limit the results
# mycursor.execute("SELECT * FROM customers LIMIT 5")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# # Start from another position
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)


# # # ============ MYSQL JOIN =====================
# Join two or more tables
# mycursor.execute('Create TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR (255), fav VARCHAR(255))')
# mycursor.execute("ALTER TABLE users MODIFY COLUMN fav INT")
# mycursor.execute('Create TABLE Products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR (255))')

# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#     ('John', 154),
#     ('Peter', 154),
#     ('Amy', 155),
#     ('Hannah', None),
#     ('Michael', None)
# ]

# mycursor.executemany(sql, val)

# # Commit the changes
# mydb.commit()

# sql = "INSERT INTO products (ID, name) VALUES (%s, %s)"
# val = [
#     (154, 'Chocolate Heaven'),
#     (155, 'Tasty Lemons'),
#     (156, 'Vanilla Dreams')
# ]

# mycursor.executemany(sql, val)

# # Commit the changes
# mydb.commit()

# # Display the contents
# mycursor.execute("SELECT * FROM users")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# mycursor.execute("SELECT * FROM products")

# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

# sql = "SELECT " \
# "users.name AS user, " \
# "products.name AS favourite " \
# "FROM users " \
# "INNER JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#         print(x)

# # LEFT JOIN
# sql = "SELECT " \
# "users.name AS user, " \
# "products.name AS favourite " \
# "FROM users " \
# "LEFT JOIN products ON users.fav = products.id"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#         print(x)    

# RIGHT JOIN
sql = "SELECT " \
"users.name AS user, " \
"products.name AS favourite " \
"FROM users " \
"RIGHT JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
        print(x)   