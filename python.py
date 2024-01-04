import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='#Engineering01',
    database='COLLEGE_ATTENDANCE')
cur = mydb.cursor()
# # Insert data into the Students table
# cur.execute("INSERT INTO Students VALUES (1, 'John', 1)")
# cur.execute("INSERT INTO Students VALUES (2, 'Jane', 2)")

# # Insert data into the Classes table
# cur.execute("INSERT INTO Clases VALUES (1, 'Math Class', 101)")
# cur.execute("INSERT INTO Clases VALUES (2, 'History Class', 102)")

# # Insert data into the Teachers table
# cur.execute("INSERT INTO Teachers VALUES (101, 'Mr.', 'Smith', 'Math')")
# cur.execute("INSERT INTO Teachers VALUES (102, 'Mrs.', 'Johnson', 'History')")

# # Insert data into the Attendance table
# cur.execute("INSERT INTO Attendance VALUES (1, 1, 1, '2023-01-01', 'Present')")
# cur.execute("INSERT INTO Attendance VALUES (2, 2, 2, '2023-01-01', 'Absent')")

# # Commit the changes and close the connection

cur.execute("SELECT * FROM STUDENTS;")
s=cur.fetchall()
for row in s:
    print(row)

# Specify the table name for which you want to get headers
table_name = 'STUDENTS'

# Execute the query to get column names from information_schema
cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}';")

# Fetch all rows (each row represents a column name)
columns_info = cur.fetchall()

# Extract column names from the result
column_names = [column[0] for column in columns_info]

# Print column names
print("Column names:", column_names)


mydb.commit()
mydb.close()
