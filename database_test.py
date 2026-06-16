import sqlite3

connection = sqlite3.connect("scan_history.db")

cursor = connection.cursor()

cursor.execute('''
               INSERT INTO scan_history (username, score, risk, timestamp)
               VALUES (?, ?, ?, ?)
''', ('john_doe', 85, 'High', '2023-10-01 12:00:00'))

connection.commit()

print("Data inserted successfully!")

connection.close()