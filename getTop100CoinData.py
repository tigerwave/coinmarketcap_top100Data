from coinmarketcapapi import CoinMarketCapAPI
import os
from dotenv import load_dotenv
import logging
import sys

load_dotenv()

api_key = os.environ.get('apiKey')
cmc = CoinMarketCapAPI()

STOP_ON_ERROR = True
DEBUG = True


if api_key is not None:
    api_data = api_key
else:
    api_data = sys.argv[1]

cmc = CoinMarketCapAPI(api_key=api_data, debug=True, logger=logging.getLogger(__name__)) # Sandbox

fullData = cmc.cryptocurrency_listings_latest()
data_list = []
range_int = 0

for eachData in fullData.data:  
    
    coinData = str(eachData['name']) + ',' + str(eachData['quote']['USD']['price']) + ',' + str(eachData['quote']['USD']['price'])  + ',' +  str(eachData['quote']['USD']['percent_change_1h'])  + ',' +  str(eachData['quote']['USD']['volume_change_24h']) + ',' +  str(eachData['quote']['USD']['percent_change_7d'])  + ',' + str(eachData['quote']['USD']['market_cap']) + ',' +  str(eachData['quote']['USD']['volume_24h']) + ',' +  str(eachData['total_supply'])
    data_list.append(coinData)

    range_int+=1
    if range_int == 100:
        print(data_list)
        break    


# you can get list data
# each content sorted with comma .
# can change list data to json format with dictionary using key value.