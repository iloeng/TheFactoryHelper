#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
   @Name:     main.py
   @Desc:     
   @Author:   liangz.org@gmail.com
   @Create:   2020.10.21   22:59
-------------------------------------------------------------------------------
   @Change:   2020.10.21
-------------------------------------------------------------------------------
"""
from config import Config
from features import Production


if __name__ == '__main__':
    a = Production(Config.Purchasing, Config.ManuFacturing)
    # for k, v in Config.ManuFacturing.items():
    #     print('{:<20}'.format(k))
    #     print('{:.2f}'.format(a.product_cost(k)), '\n')
    # print(a.product_cost('Speakers'))
    for k, v in Config.ManuFacturing.items():
        print('{:<20}'.format(k))
        print('{:.2%}'.format(a.product_profit_rate(k)), '\n')
    print('{:.2%}'.format(a.product_profit_rate('Hose')), '\n')