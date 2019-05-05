import sqlite3

sqlite_file = './pimonitor_db.sqlite';
table = 'Pi_Stats'
new_field = 'Key'
field_type = 'INTEGER PRIMARY KEY'

def create_database(table, field, ftype):
    #Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    #Create the table with a primary key column
    c.execute('CREATE TABLE {tn} ({nf} {ft})' \
                .format(tn=table, nf=field, ft=ftype))
    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()


def add_columns(table):
    #Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    cols = {"User": "STRING", "CPU_Percent": "STRING", "Memory_Percent": "STRING", "Battery_Percent": "STRING", "Plugged_In": "INTEGER", "Log_Date": "STRING", "Boot_Date": "STRING"}
    for key, value in cols.items():
        c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
            .format(tn=table, cn=key, ct=value))
    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()


def setup_db(sqlite_file, table, field, ftype):
    #Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    create_database(table,field,ftype)
    add_columns(table)
    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

def insert_to_db(user, cpu, mem, batt, pluggedin, log, boot):
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    params = (user, cpu, mem, batt, pluggedin, log, boot)
    sql = '''INSERT INTO Pi_Stats (User, CPU_Percent, Memory_Percent, Battery_Percent, Plugged_In, Log_Date, Boot_Date)
             VALUES (?, ?, ?, ?, ?, ?, ?)'''
    #Need to fix this so it pulls in correctly.
    c.execute(sql, params)

    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_db(sqlite_file, table, new_field, field_type)
