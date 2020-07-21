import mysql.connector as connector


# cursor.execute('SELECT name FROM Regions')


class Connector:

    def __init__(self):
        self.db = connector.connect(
            host="localhost",
            user="mapaApp",
            passwd="lyceum11f2_2020",
            database="MapaApp"
        )
    def __del__(self):
        self.db.close()

    async def store(self, update, code = ''):
        cursor = self.db.cursor()
        ex_exceprion = Exception('This version already exist')

        cursor.execute('SELECT code FROM versions')
        try:
            for cd in cursor:
                if(cd[-1] == code):
                    raise ex_exceprion
        except ex_exceprion as e:
            print(e)  # todo make a log!
        finally:
            cursor.execute(update) # todo format update
    
    async def read(self, code):
        return code
        # cursor = self.db.cursor()
        # ex_exceprion = Exception('This version already exist')

        # cursor.execute('SELECT code FROM versions')
        # try:
        #     for cd in cursor:
        #         if(cd[-1] == code):
        #             raise ex_exceprion
        # except ex_exceprion as e:
        #     print(e)  # todo make a log!
        # finally:
        #     cursor.execute(update) todo format update