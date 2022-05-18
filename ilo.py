#!/usr/bin/python
# taken from https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/
import sys
import mariadb
import webbrowser

conn = mariadb.connect(
    user="root",
    password="bdhnssnhdb",
    host="192.168.11.10",
    database="glpi")
cur = conn.cursor()

# Getting machine to find details for:

#def start():
while True:
    print(f"Welcome to the ilo connector. \n")

    #some_name = input ("Enter server-name:- ")
    some_name = sys.argv[1]
    cur.execute("SELECT contact_num FROM glpi_computers WHERE name=?", (some_name,))

    for contact_num in cur:
        ilo_raw = contact_num
        ilo = ilo_raw[-1]

    print(f"Connecting to: {ilo}")

# open url in browser:

    url = ilo

    webbrowser.open_new(url)

#    check = input("Do you want to connect to another ILO or exit? enter Y to restart or another key to end: ")
#    if check.upper() == "Y": #go back to the top
#        continue    
#    print("Bye...")
    break #exit
