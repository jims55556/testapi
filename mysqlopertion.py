#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql.cursors
import configparser
from testdata.getpath import GetTestConfig


config = configparser.ConfigParser()
config.read(GetTestConfig("dbconfig.conf"))
db='TESTDB'
host = config[db]['host']
user = config[db]['user']
password = config[db]['passwd']
db = config[db]['db']

class MySQLcaozuo():
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
            user=user,
            password=password,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            )
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
            self.connection.commit()

    def insert(self, table_name, data):
        for key in data:
            data[key] = "'" + str(data[key]) + "'"
        key = ','.join(data.keys())
        value = ','.join(data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
            self.connection.commit()

    def close(self):
        self.connection.close()

    # if __name__ == '__main__':
    #     db = MySQLcaozuo()
    #     table_name = "poll_question"
    #     data = {'id': 1, 'question_text': '你喜欢的游戏是什么？'}
    #     db.clear(table_name)
    #     db.insert(table_name, data)
    #     db.close()