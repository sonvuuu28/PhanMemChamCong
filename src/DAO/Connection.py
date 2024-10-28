import os
import configparser
import pyodbc

class Connection:
    def __init__(self):
        self.config = self.read_config('config.ini')

    def read_config(self, config_file):
        config = configparser.ConfigParser()
        config_path = os.path.join(os.path.dirname(__file__), config_file)
        config.read(config_path)
        return config

    def getConnection(self):
        server = self.config['DATABASE']['Server']
        db = self.config['DATABASE']['Database']

        try:
            con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + db + ';Trusted_Connection=yes;')
            return con
        except pyodbc.Error as e:
            return None

def main():
    connection_obj = Connection()
    conn = connection_obj.getConnection()

    if conn:
        print("Connected to the database.")
        conn.close()
    else:
        print("Error connecting to the database.")

if __name__ == "__main__":
    main()