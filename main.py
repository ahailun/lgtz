#!/usr/bin/python
# -*- coding: utf8 -*-

from Lugang import Exchange
# Binance Exchange Api文档： https://binance-docs.github.io/apidocs/spot/cn/#45fa4e00db
# Okex Exchange Api文档：  https://www.okexcn.com/docs/zh/#vedio
# Huobi Exchange Api文档： https://huobiapi.github.io/docs/spot/v1/cn/
from Lugang.ExchangeAdapter import BinanceExchangeAdapter, OkexExchangeAdapter, HuobiExchangeAdapter

settings = {
    'symbol': "BTC-USDT",        # 币对
    'start':'',                  # 开始时间（ISO 8601标准）
    'end':'',                    # 结束时间（ISO 8601标准）
}

okexAdapter = OkexExchangeAdapter(settings)
exchange = Exchange(okexAdapter, dict(GetRecords=okexAdapter.GetRecords))
exchange.setAdapter()

#todo 考虑频率限制
#todo 考虑请求数量限制
allData = exchange.GetRecords("PERIOD_M1")
for i in range(1, 500):
    print(allData[0][:i])