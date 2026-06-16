import sqlite3

connection = sqlite3.connect("scan_history.db")

cursor = connection.cursor()

cursor.executemany('''INSERT INTO scan_history (username, score, risk, timestamp)
               VALUES (?, ?, ?, ?)''',
               [
               ("test_user1", 75, "High", "2023-10-01"),
               ("test_user2", 43, "Low", "2026-09-06"),
               ("test_user3", 60, "Medium", "2024-05-20")
               ]
            )

connection.commit()
print("Records inserted successfully")

connection.close()