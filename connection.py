import os
import pyodbc
import traceback
from dotenv import load_dotenv

load_dotenv()

class Connection:
    """Connection
    Class that outlines the methods to connect to the database
    
    Attributes
    ----------
    serverName : str
        Name of the server
    databaseName : str
        Name of the database
    dbUserName : str
        Name of the username
    dbPassword : str
        DB password
    
    Methods
    ----------
    def connect(self):
        Method to make an instance of a connection to the database
    def _build_connection_string(self):
        Private method to return a connection string.
    """

    def __init__(
        self, 
        serverName=None,
        databaseName=None,
        dbUserName=None, 
        dbPassword=None,
        dsn=None
    ):
        """
        Method to construct all the necessary attributes to make a connection to the database
        
        Parameters
        ----------
        serverName : str
            The name of the server where the database is hosted.
        databaseName : str
            The name of the database.
        dbUserName : str
            The name of user to be used when connecting to the database.
        dbPassword : str
            The password to be used when connecting to the database.
        dsn : str
            The DSN.
        """
        self.driver = os.getenv("DB_DRIVER")
        self.dsn = dsn or os.getenv("DSN")
        self.serverName = serverName or os.getenv("SERVERNAME")
        self.databaseName =  databaseName or os.getenv("DATABASENAME")
        self.dbUserName =  dbUserName or os.getenv("DBUSERNAME")
        self.dbPassword =  dbPassword or os.getenv("DBUSERPASSWORD")


    def connect(self):
        """
        Method that makes a new instance of a database connection
        
        Parameters
        ----------
        None
        
        Exceptions:
        ----------
        None
        
        Return Values:
        ----------
        pyodbc/Connection
        """

        try:
            connection = pyodbc.connect(self._build_connection_string())
        except:
            print(traceback.format_exc())
            return traceback.format_exc()
        
        return connection

    def _build_connection_string(self):
        """
        Method to build a connection string
        
        Parameters
        ----------
        None
        
        Exceptions:
        ----------
        None
        
        Return Values:
        ----------
        output : str
            output string address to DB connection
        """
        output = ""

        # Add Driver
        output += 'DRIVER='+self.driver+';'
        # Add Server
        output += 'SERVER='+self.serverName+';'
        # Add DatabaseName
        output += 'DATABASE='+self.databaseName+';'
        #Add Username
        output += 'UID='+self.dbUserName+';'
        #Add Password
        output += 'PWD='+self.dbPassword + ';'
        output += 'Trusted_Connection=yes;'

        return output