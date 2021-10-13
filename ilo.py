#!/usr/bin/python
# taken from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
import sys
import mariadb
import webbrowser

conn = mariadb.connect(
    user="root",
    password="bdhnssnhdb",
    host="localhost",
    database="glpi")
cur = conn.cursor()

# retrieving information and print ilo url on screen

some_name = sys.argv[1]

cur.execute("SELECT contact_num FROM glpi_computers WHERE name=?", (some_name,))

for contact_num in cur:
    ilo = contact_num
    print(f"Connecting to {ilo}")

# open url in browser:

webbrowser.open_new({ilo})
