from connection import Connection

connection = Connection().connect()
print(Connection()._build_connection_string())

cursor = connection.cursor()
cursor.execute('SELECT * FROM dbo.Customers')
