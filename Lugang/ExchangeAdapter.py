#!/usr/bin/python
# -*- coding: utf8 -*-
import requests

granularity_d = {
                "PERIOD_M1":60,
                "PERIOD_M5":300,
                "PERIOD_M15":900,
                "PERIOD_M30":1800,
                "PERIOD_H1":3600,
                "PERIOD_D1":86400, 
                }

class BinanceExchangeAdapter():
    def __init__():
        pass

class OkexExchangeAdapter(object):
    def __init__(self, settings):
        self.settings = settings
        self.symbol = self.settings.get('symbol', None)
        self.start  = self.settings.get('start', None)
        self.end    = self.settings.get('end', None)
        #todo： 检查上述参数的合法性

    def GetRecords(self, PD):
        """
        todo:
        1.考虑异常处理
        """
        real_PD = granularity_d.get(PD, None)
        okexApiUrl = "https://www.okex.com/api/spot/v3/instruments/{symbol}/candles?granularity={granularity}&start={start}&end={end}".format(
                                                                                                                                            symbol=self.symbol, 
                                                                                                                                            granularity=real_PD, 
                                                                                                                                            start=self.start, 
                                                                                                                                            end=self.end
                                                                                                                                            )
        print(okexApiUrl)                                                                                                                                     
        req = requests.get(okexApiUrl)
        print("end OkexExchangeAdapter GetRecords")

class HuobiExchangeAdapter():
    def __init__():
        pass