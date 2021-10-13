#!/usr/bin/python
# taken from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
import sys
import mariadb

conn = mariadb.connect(
    user="root",
    password="bdhnssnhdb",
    host="localhost",
    database="glpi")
cur = conn.cursor()

#retrieving information

some_name = sys.argv[1]
#print (some_name)
cur.execute("SELECT contact_num FROM glpi_computers WHERE name=?", (some_name,))

for contact_num in cur:
    url = contact_num
    print(url)
