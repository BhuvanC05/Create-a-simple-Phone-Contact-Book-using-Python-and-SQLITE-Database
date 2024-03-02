import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 Name TEXT,
                 Cell TEXT,
                 Email TEXT)''')
    conn.commit()
    conn.close()

# Function to insert data into the database
def insert_data(name, cell, email):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (Name, Cell, Email) VALUES (?, ?, ?)", (name, cell, email))
    conn.commit()
    conn.close()

# Function to fetch and display all data from the database
def fetch_data():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    conn.close()
    return rows

# Main function to interact with the user
def main():
    create_table()
    
    # Inserting sample data
    insert_data("John Doe", "1234567890", "john@example.com")
    insert_data("Jane Smith", "9876543210", "jane@example.com")
    insert_data("Alice Johnson", "5555555555", "alice@example.com")
    insert_data("Bob Brown", "9998887776", "bob@example.com")
    insert_data("Eve Wilson", "1112223333", "eve@example.com")
    
    # Fetching and displaying all data
    contacts = fetch_data()
    print("Contacts:")
    for contact in contacts:
        print(contact)

if __name__ == "__main__":
    main()
