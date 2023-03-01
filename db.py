import mysql.connector

from dotenv import load_dotenv,dotenv_values
load_dotenv()
config = dotenv_values(".env")

#db connection
db = mysql.connector.connect(
  host=config["MYSQL_HOST"],
  user=config['MYSQL_USER'],
  password=config['MYSQL_PASSWORD'],
  database=config['MYSQL_DB']
)

#define cursor
cur = db.cursor()

def getHouseListByCityName(city):
    sql = "select area,bed,bath,garage,price from properties where city= %s ORDER BY RAND() LIMIT 100"
    cityName = (city,)
    cur.execute(sql,cityName)
    houseList = cur.fetchall()
    return houseList

