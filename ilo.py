#!/usr/bin/python
# taken from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
import sys
import mariadb
import webbrowser

conn = mariadb.connect(
    user="root",
    password="bdhnssnhdb",
    host="192.168.11.100",
    database="glpi")
cur = conn.cursor()

# Getting machine to find details for:

#def start():
print(f"Welcome to the ilo connector. \n")

#while True:
some_name = input ("Enter server-name:- ")

cur.execute("SELECT contact_num FROM glpi_computers WHERE name=?", (some_name,))

for contact_num in cur:
    ilo_raw = contact_num
    ilo = ilo_raw[-1]

    print(f"Connecting to: {ilo}")

# open url in browser:

url = ilo

webbrowser.open_new(url)
