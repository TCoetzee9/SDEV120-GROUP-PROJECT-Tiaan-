import sqlite3  # Import SQLite module

# Set up the database and table
def setup_database():
    # Connect to the database (will create the file if it doesn't exist)
    connection = sqlite3.connect('payroll.db')
    
    # Create a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Create a table to store employee data if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employeeID INTEGER PRIMARY KEY,
            employeeName TEXT NOT NULL,
            hourlyRate REAL NOT NULL
        )
    ''')

    # Insert 20 sample employee data with whole number hourly rates
    cursor.executemany('''
        INSERT INTO employees (employeeID, employeeName, hourlyRate)
        VALUES (?, ?, ?)
    ''', [
        (101, 'Sophia Evans', 19),
        (102, 'Liam O’Brien', 21),
        (103, 'Olivia Wright', 23),
        (104, 'Noah Thompson', 20),
        (105, 'Emma Walker', 24),
        (106, 'Mason Brown', 19),
        (107, 'Ava Scott', 21),
        (108, 'Lucas Young', 24),
        (109, 'Isabella Martinez', 22),
        (110, 'Ethan Hill', 19),
        (111, 'Mia Moore', 21),
        (112, 'James Taylor', 23),
        (113, 'Charlotte Green', 22),
        (114, 'Amelia Wilson', 23),
        (115, 'Elijah Adams', 20),
        (116, 'Harper Clark', 21),
        (117, 'Benjamin Lewis', 22),
        (118, 'Abigail Robinson', 23),
        (119, 'Sebastian Perez', 24),
        (120, 'Zoe Ramirez', 22)
    ])

    # Commit changes and close the connection
    connection.commit()
    connection.close()

# Call the function to set up the database
setup_database()
