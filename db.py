from main import mysql

def getHouseListByCityName(city):
    sql = "select area,bed,bath,garage,price from properties where city= %s ORDER BY RAND() LIMIT 100"
    cityName = (city,)
    cur=mysql.connection.cursor()
    cur.execute(sql,cityName)
    houseList = cur.fetchall()
    cur.close()
    return houseList