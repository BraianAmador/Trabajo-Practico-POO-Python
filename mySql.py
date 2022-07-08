import mysql.connector

mydb = {
    'host': "localhost",
    'user': "root",
    'password': "",
    'database': "tp1",
    'port': "3306"
}


class DB():
    def __init__(self):
        self.__conexion = mysql.connector.Connect(**mydb)
        self.__cursor = self.__conexion.cursor()

    def get_cursor(self):
        return self.__cursor

    def get_conexion(self):
        return self.__conexion


dba = DB()
