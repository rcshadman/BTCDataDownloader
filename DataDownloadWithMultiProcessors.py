from main import *
import public_markets
import multiprocessing

def SaveDataFromMarkets(markets):
    db=DataBase.MongoDB('localhost',8003)
    marketDownload=MarketDataLoader(db)
    marketDownload.save_depth_info(markets)


if __name__=='__main__':
    public_markets.Market.get_market_list()
    markets=['Bitfinex','Bitstamp', 'Poloniex', 'Bithumb', 'Coinone', 'GDAX', 'Kraken','Huobi','OKCoin']
    jobs=[]
    for market in markets:
        p=multiprocessing.Process(target=SaveDataFromMarkets,args=([market],))
        jobs.append(p)
        p.start()