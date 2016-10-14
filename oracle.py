import cx_Oracle

credo = cx_Oracle.connect('testcredo', 'testcredo', 'oracle2.itworks.brest:1521/testcredo2')
forpost = cx_Oracle.connect('forpost', 'welc0me0208', '172.22.157.15:1521/forp_d3')

cursor = credo.cursor()
print(credo.version)
cursor.execute('select * from clients')

for row in cursor:
    print(row)
