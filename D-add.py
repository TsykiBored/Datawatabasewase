import sqlite3

con = sqlite3.connect("Students")
cur = con.cursor()

cur.execute("""
INSERT INTO Students VALUES (659,'Phil','Swift',52,'M')
""")