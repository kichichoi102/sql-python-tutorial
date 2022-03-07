from connection import Connection

connection = Connection().connect()
print(Connection()._build_connection_string())
print(connection)