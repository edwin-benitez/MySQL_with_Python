import requests
import mysql.connector

f = open("apikey.txt", "r")
d = open("dbalogin.txt", "r") 
API_KEY = f.readline()
r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GE&apikey=' + API_KEY)
result = r.json()
allDays = result['Time Series (Daily)']

#Update the date you want to display the stock price.
date = '2019-01-08'
singleDay = allDays[date]

mydb = mysql.connector.connect(
  host= d.readline(),
  user= d.readline(),
  password=d.readline(9),
  database=d.read()
)

mycursor = mydb.cursor()

sql = "INSERT INTO stock (date, open, high, low, close, volume) VALUES (%s, %s, %s, %s, %s, %s)"
val = (date, singleDay['1. open'], singleDay['2. high'], singleDay['3. low'], singleDay['4. close'], singleDay['5. volume'])
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

