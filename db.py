import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

#db connection
db = mysql.connector.connect(
  host=os.getenv("MYSQL_HOST"),
  user=os.getenv('MYSQL_USER'),
  password=os.getenv('MYSQL_PASSWORD'),
  database=os.getenv('MYSQL_DB')
)

#define cursor
cur = db.cursor()

def getHouseListByCityName(city):
    sql = "select area,bed,bath,garage,price from properties where city= %s ORDER BY RAND() LIMIT 100"
    cityName = (city,)
    cur.execute(sql,cityName)
    houseList = cur.fetchall()
    return houseList

