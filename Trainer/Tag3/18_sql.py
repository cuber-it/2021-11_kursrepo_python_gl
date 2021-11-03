import cx_Oracle

# create and populate Oracle objects

db_connection_string = 'username/passwort@servicename'
con = cx_Oracle.connect(db_connection_string)

# create table, if necessary
cursor = con.cursor()
cursor.execute("""
        select count(*)
        from user_tables
        where table_name = 'TEST'""")
count, = cursor.fetchone()
if count == 0:
    print("Creating table...")
    cursor.execute("""
            create table TEST (
                i number not null,
                j varchar2(200)
            )""")

# remove all existing rows and then add a new one
print("Removing any existing rows...")
cursor.execute("delete from test")
print("Adding row to table...")
cursor.execute("insert into test values (1, 'test')")
con.commit()
print("Success!")