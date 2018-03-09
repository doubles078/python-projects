import sqlite3

sqlite_file = './Workspace/Python/PiMonitor/pimonitor_db.sqlite';
table = 'Pi_Stats'
new_field = 'Key'
field_type = 'INTEGER'

def open_conn(sqlite_file):
    #Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

def close_conn():
    # Commit the changes to the database and close the connection
    conn.commit()
    conn.close()

def create_database(table, field, ftype):


    #Create the table with a primary key column
    c.execute('CREATE TABLE {tn} ({nf} {ft})' \
                .format(tn=table, nf=field, ft=ftype))
    close_conn()


def add_columns(table):
    cols = {"User": "TEXT", "CPU_Percent": "REAL", "Memory_Percent": "REAL", "Battery_Percent": "REAL", "Plugged_In": "INTEGER", "Log_Date": "TEXT", "Boot_Date": "TEXT"}

    c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table, cn=new_column1, ct=column_type))


def setup_db(sqlite_file, table, field, ftype):
    open_conn(sqlite_file)
    create_database(table, field, ftype)
    add_columns(table)
    close_conn()

if __name__ == '__main__':
    setup_db(sqlite_file, table, new_field, field_type)
