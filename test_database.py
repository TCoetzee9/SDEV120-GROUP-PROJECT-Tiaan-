import sqlite3  # Import SQLite module

# Function to connect to the database and fetch data
def get_hourly_rate(employeeID):
    connection = sqlite3.connect('payroll.db')
    cursor = connection.cursor()
    
    cursor.execute("SELECT hourlyRate FROM employees WHERE employeeID = ?", (employeeID,))
    result = cursor.fetchone()

    connection.close()
    
    if result:
        return result[0]
    else:
        return None

# Main program
employee_id = int(input("Enter Employee ID: "))
hourly_rate = get_hourly_rate(employee_id)

if hourly_rate is not None:
    print(f"Hourly rate for Employee ID {employee_id}: ${hourly_rate}")
else:
    print(f"Employee ID {employee_id} not found.")
