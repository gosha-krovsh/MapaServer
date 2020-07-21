import format
import dataBase as DB

async def work(buff):
    input = format.input_check(buff)

    if (type(input) == Exception):
        raise input
    if(type(input) == int):
        connection = DB.Connector()
        res = connection.read(code=input)
        connection.__del__()

        return res
    if(type(input) == dict):
        connection = DB.Connector()
        connection.store(update = input)
        connection.__del__()