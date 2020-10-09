import pymysql


try:
    conn=pymysql.connect("localhost", "root", "alxalx", "testowa", charset="utf8")
    c=conn.cursor()
    print("Polaczenie OK")
except:
    print("błąd połączenia")
