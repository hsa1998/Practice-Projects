from pycoingecko import CoinGeckoAPI
import shelve

cg = CoinGeckoAPI()
raw = cg.get_coins_markets(vs_currency='usd')
mcs = {}
for i in range(len(raw)):
    mcs.setdefault(raw[i]['symbol'],raw[i]['market_cap'])

shelfFile = shelve.open('index')

shelfFile['blacklist'] = ['xrp', 'usdt', 'usdc', 'ceth', 'dai', 'wbtc', 'busd', 'cdai', 'cusdc',
                          'hbtc', 'renbtc', 'husd', 'tusd', 'alink']

shelfFile['old_market_caps'] = {'btc': 802413737411, 'eth': 178719063426, 'dot': 20114659633, 'ada': 19857345265,
                                'bnb': 13666342816, 'ltc': 15147204342, 'link': 11320776887, 'doge': 5164021993,
                                'bch': 8576062023, 'xlm': 8625122207}

shelfFile['old_weights'] = {'btc': 0.6644674199058247, 'eth': 0.24736501395375737, 'dot': 0.016656663969571925,
                            'ada': 0.016443585595862474, 'bnb': 0.011316904393730207, 'ltc': 0.012543184791912151,
                            'link': 0.01268691775131382, 'doge': 0.004276253271905419, 'bch': 0.007101715162257164,
                            'xlm': 0.0071423412038647835}

shelfFile['old_portfolio_total'] = 100000
shelfFile.close

