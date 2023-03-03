import mysql.connector
import os

db = mysql.connector.connect(
    host=os.getenv('MYSQL_HOST',default='127.0.0.1'),
    # port=os.getenv('MYSQL_PORT',default=3306),
    # only for port
    port=6227,
    user=os.getenv('MYSQL_USER',default='root'),
    password=os.getenv('MYSQL_PASSWORD',default='root'),
    database=os.getenv('MYSQL_DB',default='test')
)

def getHouseListByCityName(city):
    sql = "select area,bed,bath,garage,price from properties where city= %s ORDER BY RAND() LIMIT 100"
    cityName = (city,)

    cursor = db.cursor()
    cursor.execute(sql,cityName)

    houseList = cursor.fetchall()
    cursor.close()
    return houseList