import mysql.connector
mydb= mysql.connector.connect(
    host='localhost',
    user='root',
    password='#Engineering01',
    database='COLLEGE_ATTENDANCE')
cur = mydb.cursor()
def ShowingTables():
    print("SHOW TABLES")
    cur.execute("SHOW TABLES")
    # Fetch all tables
    tables = cur.fetchall()

    # Display the tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

def describe_tables():
    # Taking input from the user
    table  = input("Enter Table name :- ")
    print("Displaying all data in the " + table + " Table :")
    cur.execute("SELECT * FROM " + table)
    all_attendance = cur.fetchall()

    # Displaying all rows in the ATTENDANCE table
    for row in all_attendance:
        print(row)


def adding_data():
    identity = input("Specify the table where you want to add any data :-")

    # Execute the query to get column names from information_schema
    cur.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{identity}';")

    # Fetch all rows (each row represents a column name)
    columns_info = cur.fetchall()
    print(columns_info)
    # Extract column names from the result
    column_names = [column[0] for column in columns_info]

    # Print column names
    print("Column names:", column_names)

    cur.execute(f"SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{identity}';")
    arr = []
    column_count = cur.fetchone()[0]
    print("Enter the data:")
    g = ""
    for col in column_names:
        col_value = input(f"Enter {col}: ")

        # Check the datatype of the entered value
        if col_value.isdigit():
            g += col_value
            arr.append(int(col_value))  # Convert to int if it's a digit
        else:
            g += "\'" + col_value + "\'"
            arr.append(col_value)  # Keep it as a string
        g += ", "
    g = g[:-2]
    print(g)
    print(arr)
    # Enclose string elements in double quotes using a list comprehension
    quoted_list = ['"{}"'.format(item) if isinstance(item, str) else item for item in arr]
    # Construct a parameterized query for INSERT
    placeholders = ', '.join(['%s'] * len(quoted_list))
    query = f"INSERT INTO {identity} VALUES ({g})"
    #print(query,quoted_list)
    cur.execute(query)
    #print("INSERT INTO " + identity+" VALUES ("+addstr+") ")

    

def default():
    print("This is the default case")

# Dictionary mapping case values to functions
switch_dict = {
    1: ShowingTables,
    2: describe_tables,
    3: adding_data
}
# Function to emulate switch statement
def switch_case(case_value):
    # Get the function associated with the case_value, default to default() if not found
    switch_dict.get(case_value, default)()
while True:
    # Taking input from the user
    user_input = int(input("Enter the command : "))
    if user_input == -1:
        print("EXIT")
        break
    else:
        switch_case(user_input)





mydb.commit()
mydb.close()
