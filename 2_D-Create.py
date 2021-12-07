import sqlite3

con = sqlite3.connect("Students")
cur = con.cursor()

cur.execute("""
CREATE TABLE Students
(StudentID INTEGER, StudentFirstName Text(15), StudentSurname Text(15), StudentAge INTEGER(2), StudentGender Text(1))
""")
