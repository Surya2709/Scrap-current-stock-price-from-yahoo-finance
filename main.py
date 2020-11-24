import requests
from bs4 import  BeautifulSoup
import pandas as pd

def get_data(data):
    url="https://in.finance.yahoo.com/quote/"+data+"?p="+data+"&.tsrc=fin-srch"
    r=requests.get(url)
    soup = BeautifulSoup(r.content,'html5lib')
    table = soup.find('span',{"class":"Trsdu(0.3s)","data-reactid":"32"})
    t=str(table)
    b=t.split(">")
    a=b[1].split("<")
    return a[0]

l=[]
given = str(input("Enter the input data : "))
a=given.split()
for string in a:
    l.append(string)
    print(string)

data=l[0]

curr_price = []
stocks = []

for stock_name in l:
    print(f"Getting the data for {stock_name} ...")
    stocks.append(stock_name)
    price=get_data(stock_name)
    print("Current price : ", price)
    curr_price.append(price)


data_tuples=list(zip(stocks,curr_price))
print("Writing data to csv file !")
frame=pd.DataFrame(data_tuples,columns=["Stock","Price"])
print(frame)
frame.to_csv("stock_data.csv",index=False)
print(" Done ! ")
