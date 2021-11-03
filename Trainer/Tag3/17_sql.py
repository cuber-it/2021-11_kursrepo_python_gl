#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

""" SQL Lite 2 dict
>>> from sqlitedict import SqliteDict
>>> mydict = SqliteDict('./my_db.sqlite', autocommit=True)
>>> mydict['some_key'] = any_picklable_object
>>> print mydict['some_key']  # prints the new value
>>> for key, value in mydict.iteritems():
>>>     print key, value
>>> print len(mydict) # etc... all dict functions work
>>> mydict.close()
"""