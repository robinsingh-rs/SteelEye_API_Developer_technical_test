import random
import datetime as dt
import uvicorn
from typing import Union, List
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()


# temp data
trades_db = []

buysellindicator = ['BUY', 'SELL']
asset_classes = ['Share', 'Stock', 'Commodity']
counterparties = ['Wefunder', 'Techstars', 'Kickstarter', 'bob']
id = ['APL', 'GGL', 'AMZN', 'MS', 'bob']
name = ['Apple', 'Google', 'Amazon', 'Microsoft', 'bob']
traders = ['Tim Cook','Sundar Pichai', 'Andy Jassy', 'Satya Nadella', 'bob']

for i in range(20):
    buySellIndicator = random.choice(buysellindicator)
    asset_class = random.choice(asset_classes)
    counterparty = random.choice(counterparties)
    instrument_id = random.choice(id)
    instrument_name = random.choice(name)
    tradeid = i + 1
    trader = random.choice(traders)




    trades = {
        "trade_id" : tradeid ,
        "asset_class" : asset_class,
        "counterparty" : counterparty,
        "instrument_id" : instrument_id,
        "instrument_name" : instrument_name,
        "trade_date_time" : dt.datetime.now(),
        "trade_details": {
            "buySellIndicator": buySellIndicator,
            "price": random.randrange(1,20),
            "quantity": random.randrange(1,20)
        },
        "trader" : trader
    }

    trades_db.append(trades)




# trades filter
@app.get("/trades")
def trade_and_filter(assetClass: Union[str, None] = None,
                 end: Union[str, None] = None,
                 maxPrice: Union[int, None] = None, 
                 minPrice: Union[int, None] = None,
                 start: Union[str, None] = None,
                 tradeType: Union[str, None] = None):
    
    result = []

    if type(assetClass) == str:
        now = []
        for trade in trades_db:
            if assetClass == trade['asset_class']:
                now.append(trade)
        
        result = now
    
    if type(end)== str:
        now = []
        if len(result) > 0:
            for trade in result:
                d1 = trade['trade_date_time'].date().strftime("%d-%m-%Y")
                d = dt.datetime.strptime(end, "%d-%m-%Y").date().strftime("%d-%m-%Y")
                if d >= d1:
                    now.append(trade)
        else:
            for trade in trades_db:
                d1 = trade['trade_date_time'].date().strftime("%d-%m-%Y")
                d = dt.datetime.strptime(end, "%d-%m-%Y").date().strftime("%d-%m-%Y")
                if d >= d1:
                    now.append(trade)
        result = now

    if type(maxPrice) == int:
        now = []
        if len(result) > 0:
            for trade in result:
                if trade['trade_details']['price'] <= maxPrice:
                    now.append(trade)
        else:
            for trade in trades_db:
                if trade['trade_details']['price'] <= maxPrice:
                    now.append(trade)
        result = now

    if type(minPrice) == int:
        now = []
        if len(result) > 0:
            for trade in result:
                if trade['trade_details']['price'] >= minPrice:
                    now.append(trade)
        else:
            for trade in trades_db:
                if trade['trade_details']['price'] >= minPrice:
                    now.append(trade)
        result = now

    if type(start)== str:
        now = []
        if len(result) > 0:
            for trade in result:
            
                d1 = trade['trade_date_time'].date().strftime("%d-%m-%Y")
                d = dt.datetime.strptime(end, "%d-%m-%Y").date().strftime("%d-%m-%Y")
                if d <= d1:
                    now.append(trade)
        else:
            for trade in trades_db:
            
                d1 = trade['trade_date_time'].date().strftime("%d-%m-%Y")
                d = dt.datetime.strptime(end, "%d-%m-%Y").date().strftime("%d-%m-%Y")
                if d <= d1:
                    now.append(trade)
        result = now

    if type(tradeType) == str:
        now = []
        if len(result) > 0:
            for trade in result:
                if tradeType == trade['trade_details']['buySellIndicator']:
                    now.append(trade)
        else:
            for trade in trades_db:
                if tradeType == trade['trade_details']['buySellIndicator']:
                    now.append(trade)

        result = now
    if len(result) > 0:
        return result
    else:
        return trades_db


# trades by id / Single trade

@app.get("/trades/{id}")
def trade_id(id: int = Path(None, description='Id of the trade you want to view', gt=0)):
    
    result = []
    for trade in trades_db:
        if id == trade['trade_id']:
            return trade
    
    return {"Data": "Not found"}
    

# searching trades
@app.get("/search")
def searching(search: str):
    trade_id_repeat_check = [] # help to handle duplicate values
    result = []

    for trade in trades_db:
        if search == trade['counterparty']:
            trade_id_repeat_check.append(trade['trade_id'])
            result.append(trade)
    

    for trade in trades_db:
        if search.lower() == trade['instrument_id'].lower():
            if trade['trade_id'] in trade_id_repeat_check:
                continue
            else:
                trade_id_repeat_check.append(trade['trade_id'])
                result.append(trade)
    

    for trade in trades_db:
        if search == trade['instrument_name']:
            if trade['trade_id'] in trade_id_repeat_check:
                continue
            else:
                trade_id_repeat_check.append(trade['trade_id'])
                result.append(trade)
    

    for trade in trades_db:
        if search == trade['trader']:
            if trade['trade_id'] in trade_id_repeat_check:
                continue
            else:
                trade_id_repeat_check.append(trade['trade_id'])
                result.append(trade)
        
    return result


if __name__ == "__main__":
    uvicorn.run(app, debug=True)




