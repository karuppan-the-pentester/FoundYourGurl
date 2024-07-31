import sqlite3
import csv

# Connect to the SQLite3 database
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Function to insert data into app_gallery from CSV
def insert_app_gallery_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            try:
                cursor.execute("""
                INSERT INTO app_gallery (userid, title, image, status)
                VALUES (?, ?, ?, ?)
                """, (row[0], row[1], row[2], row[3]))
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
    conn.commit()

# Function to insert data into app_notes from CSV
def insert_app_notes_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            try:
                cursor.execute("""
                INSERT INTO app_notes (userid, title, photo, description, message)
                VALUES (?, ?, ?, ?, ?)
                """, (row[0], row[1], row[2], row[3], row[4]))
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
    conn.commit()

# Function to insert data into app_notification from CSV
def insert_app_notification_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            try:
                cursor.execute("""
                INSERT INTO app_notification (userid, title, message, time, url)
                VALUES (?, ?, ?, ?, ?)
                """, (row[0], row[1], row[2], row[3], row[4]))
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
    conn.commit()

# Function to insert data into app_usersdatabase from CSV
def insert_app_usersdatabase_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            try:
                cursor.execute("""
                INSERT INTO app_usersdatabase (id, name, RegNo, PassWord, Department, Batch, FatherName, MotherName, DateOfBirth, Address, Phone, Photo)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))
            except Exception as e:
                print(f"Error inserting row {row}: {e}")
    conn.commit()

def InitalSetup():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS app_gallery (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL,
        title TEXT NOT NULL,
        image VARCHAR(100) NOT NULL,
        status TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS app_notes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL,
        title TEXT NOT NULL,
        photo TEXT NOT NULL,
        description TEXT NOT NULL,
        message TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS app_notification (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        userid TEXT NOT NULL,
        title TEXT NOT NULL,
        message TEXT NOT NULL,
        time TEXT NOT NULL,
        url TEXT NOT NULL
    );
    CREATE TABLE IF NOT EXISTS app_usersdatabase (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        RegNo TEXT NOT NULL,
        PassWord TEXT NOT NULL,
        Department TEXT NOT NULL,
        Batch TEXT NOT NULL,
        FatherName TEXT NOT NULL,
        MotherName TEXT NOT NULL,
        DateOfBirth TEXT NOT NULL,
        Address TEXT NOT NULL,
        Phone TEXT NOT NULL,
        Photo TEXT NOT NULL
    );
    """)
    conn.commit()

# Example usage
# InitalSetup()
insert_app_gallery_from_csv('DBFiles/app_gallery.csv')
insert_app_notes_from_csv('DBFiles/app_notes.csv')
insert_app_notification_from_csv('DBFiles/app_notification.csv')
insert_app_usersdatabase_from_csv('DBFiles/app_usersdatabase.csv')

# Close the connection
conn.close()
