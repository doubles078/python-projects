import pyodbc
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=VA-NeoDB1-Q.eftsd.com;"
                      "Database=Marketing;"
                      "Trusted_Connection=yes;"
                      "uid=dan.donohue;pwd=St3adman")


cursor = cnxn.cursor()
cursor.execute('SELECT TOP 1000 FROM dbo.Individual')

for row in cursor:
    print('row = %r' % (row,))
