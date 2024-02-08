from Config import connection
cursor = connection.cursor()

# Define your SQL query
query = "SELECT * FROM Users"

# Execute the query
cursor.execute(query)

# Fetch all rows from the result set
rows = cursor.fetchall()

# Process the fetched data
for row in rows:
    # Access row values by index or column name
    column1_value = row[0]  # Access by index
    column2_value = row[1]  # Access by index
    # Alternatively, you can access by column name if you use a dictionary cursor
    # column1_value = row['column1_name']
    # column2_value = row['column2_name']
    print(column1_value, column2_value)