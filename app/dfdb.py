import MySQLdb

__author__ = 'xosauce'

def db_connect():
    global db
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="", # your username
                         passwd="", # your password
                         db="eikon") # name of the data base

def db_close():
    global db
    db.close()

def selectAll(stmt=""):
    cursor = db.cursor()
    cursor.execute(stmt)
    data = cursor.fetchall()
    return data

def insert(stmt="",arguments=None):
    cursor = db.cursor()
    cursor.execute(stmt, arguments)
    db.commit()

def remove(stmt="",arguments=None):
    cursor = db.cursor()
    cursor.execute(stmt, arguments)
    db.commit()
