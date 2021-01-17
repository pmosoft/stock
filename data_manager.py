import pandas as pd
import os

print("data_manager start")

stock2000_v2 = pd.read_csv("Korea_Stocks_Full_v2/stock2000_v2.csv", converters=dict(StockCode=str))
stock2000_v2.head()

stock2000_v2.loc[0:5, ['Date', 'StockCode', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj_Close']]
stock2000_v2.loc[0:0]

def preprocess_stock3():
    pass

# 일자별로 재정렬. 일회성 작업.
def preprocess_stock2():
    # 로드
    stock1 = pd.read_csv("Korea_Stocks_Full_v2/stock2000_v1.csv")

    # 일자별로 가공
    stock2 = stock1.loc[:, ['Date', 'StockCode', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj_Close']]
    stock2.StockCode = stock2.StockCode.apply(lambda x: str(x).zfill(6))
    stock2.to_csv('Korea_Stocks_Full_v2/stock2000_v2.csv', index=False)

    # 종목별 카운트, min일자, max일자
    stock3 = stock2[['Date', 'StockCode']].groupby(['StockCode']).agg(['count', 'min', 'max'])
    stock3.to_csv('Korea_Stocks_Full_v2/stock2000_v3.csv')

# 종목별 csv를 하나의 csv로 merge. 일회성 작업.
def preprocess_stock():
    dirname = "Korea_Stocks_Full/"
    filenames = os.listdir(dirname)
    i = 0
    for filename in filenames:
        if not len(filename) == 10:
            continue
        filenameonly = filename[:6]
        full_filename = os.path.join(dirname, filename)
        i = i + 1
        if i == 1:
            print('1')
            print(full_filename)
            stock1 = pd.read_csv(full_filename)
            stock1["StockCode"] = str(filenameonly)
        else:
            print(full_filename)
            stock2 = pd.read_csv(full_filename)
            stock2["StockCode"] = str(filenameonly)
            stock1 = pd.concat([stock1, stock2])

    print(len(stock1))
    stock1.to_csv('Korea_Stocks_Full_v2/stock2000_v1.csv')

def test():
    pass

# preprocess_stock2()


print("data_manager end")
