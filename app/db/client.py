import pyodbc

class DB(object):
    '''Объект подключение к базе данных'''
    connection_string = ''
    count = 0

    def connect(self):
        self.connection = pyodbc.connect(DB.connection_string)
        self.connection.autocommit = True

    def __init__(self, conn_str):
        DB.count += 1
        DB.connection_string = conn_str
        self.error = None
        self.connect()

    def __del__(self):
        DB.count -= 1
        self.connection.close()

    def __len__(self):
        return (DB.count)

    def get_cursor(self):
        if self.connection is None:
            self.connect()
        self.error = None
        self.cursor = self.connection.cursor()

    def execute(self, sql):
        '''Выполнить запрос к базе данных
            "dictionary": "(True, False)"'''

        self.get_cursor()
        try:
            self.cursor.execute(sql)
            return True
        except pyodbc.Error as e:
            self.error = '{0}. {1}'.format(type(e).__name__, e.args)
            print(self.error, sql)
            return None
        finally:
            self.cursor.close()