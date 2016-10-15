# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:29:18 2016

@author: sylvn_000
"""
import pandas as pd
from datetime import datetime


path = r'C:\Users\sylvn_000\Documents\GitHub\PySupplier'
file = path+'/Fournisseur.csv'


def file2df(elmnt):
    data = pd.read_csv(elmnt, sep=None)
    return data

suppliers_datas = file2df(file)
start = datetime(2015, 12, 1)
end = datetime(2016, 12, 31)
ranges = pd.date_range(start, end, freq='M')
rng = [x for x in ranges]
sup_datas = suppliers_datas.groupby('RE_FOUR').get_group(175)
sup_datas.LA_DECH = pd.to_datetime(sup_datas.LA_DECH)
sup = sup_datas[(sup_datas.LA_DECH < rng[1]) & (sup_datas.LA_DECH > rng[0])]
