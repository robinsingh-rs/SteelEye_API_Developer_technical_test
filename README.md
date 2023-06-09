# API Name: Trades Filtering API
Description: The Trades Filtering API provides a flexible and powerful way to filter and retrieve trades based on various criteria. It allows users to retrieve a list of trades from a database and apply filtering based on parameters such as asset class, trade date, trade price, and trade type.


Endpoint:
1: /trades/: This endpoint accepts optional query parameters to filter trades based on specific criteria. The supported query parameters include:
    * assetClass: Filters trades by the asset class of the trade.
    * minPrice: Filters trades by the minimum value for the trade price.
    * maxPrice: Filters trades by the maximum value for the trade price.
    * start: Filters trades by the minimum trade date in format(DD-MM-YYYY).
    * end: Filters trades by the maximum trade date in format (DD-MM-YYYY)..
    * tradeType: Filters trades by the trade type (BUY or SELL).
note: if no filter given endpoint will return all trades.

2: /trades/{id}: This endpoint give trade for the id

3: /search/?search=bob: Search across the trades using this API through the following fields:
    * counterparty
    * instrumentId
    * instrumentName
    * trader

Response:
The API returns a JSON response containing the filtered trades that match the specified filter criteria. The response includes trade details such as the trade ID, asset class, counterparty, instrument ID, instrument name, trade date and time, trade details (buy/sell indicator, price, quantity), and trader information.

Usage:
Users can make HTTP GET requests to the /trades/filter endpoint and provide the desired filter parameters as query parameters. The API will process the requests and return the filtered trades based on the provided criteria.

Example:

http://localhost:8000/trades

http://localhost:8000/trades?assetClass=Share&end=09-06-2023&maxPrice=10&minPrice=5&start=09-06-2023&tradeType=SELL

http://localhost:8000/trades?assetClass=Share&maxPrice=10&tradeType=SELL

http://localhost:8000/search?search=Bob

