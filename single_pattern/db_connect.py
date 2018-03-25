# coding = utf-8
import sqlite3


class MetaSingleton(type):
    """
    单例
    """
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]


class DataBase(metaclass=MetaSingleton):
    """
    连接数据库
    """
    connection = None
    cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursor = self.connection.cursor()
        return self.cursor


if __name__ == '__main__':
    db1 = DataBase().connect()
    db2 = DataBase().connect()

    print("DataBase Objects DB1:", db1)
    print("DataBase Objects DB2:", db2)
