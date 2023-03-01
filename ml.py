import pandas as pd
from sklearn import linear_model
import db

def predict(city,area,bed,bath,garage) :

    #get houses from database
    houseList = db.getHouseListByCityName(city)

    #data frame
    df = pd.DataFrame(houseList)

    #reame data frame columns
    df.rename(columns={0: 'area',1:'bed',2:'bath',3:'garage',4:'price'}, inplace = True)
    
    #median of all data fream
    df.area = df.area.fillna(df.area.median())
    df.bed = df.bed.fillna(df.bed.median())
    df.bath =  df.bath.fillna(df.bath.median())
    df.garage =  df.garage.fillna(df.garage.median())
    df.price =  df.price.fillna(df.price.median())

    #implementing LinearRegression
    reg = linear_model.LinearRegression()
    reg.fit(df.drop('price',axis='columns').values,df.price)
    reg.coef_
    reg.intercept_

    price = reg.predict([[area, bed, bath,garage]] )
    return price[0].round()







