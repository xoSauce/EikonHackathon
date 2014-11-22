__author__ = 'xosauce'
import  dfdb

def run():
    content = None
    dfdb.db_connect()
    f = open('../countryID.txt')
    while True:
        line1= f.readline().strip()
        line2= f.readline().strip()
        if not line2:
            break
        dfdb.insert("REPLACE INTO countries (id,name) values (%s,%s)",(int(line1), line2.lower()))
    dfdb.db_close()
if __name__ == '__main__':
    run()