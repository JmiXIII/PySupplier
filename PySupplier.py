# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:29:18 2016

@author: sylvn_000
"""
import pandas as pd
from datetime import datetime
import xlwings as xl


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
list_sup = []

sup_datas = suppliers_datas.groupby('RE_FOUR').get_group(175)
sup_datas.LA_DECH = pd.to_datetime(sup_datas.LA_DECH)
#writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
sup_datas.to_excel(path+'/175.xls', '175')
sup_ret = []
writer = pd.ExcelWriter(path+'/'+sup_datas.FO_DESI+'.xls', engine='xlsxwriter')
for i in range(len(rng)-1):
    sup = sup_datas[(sup_datas.LA_DECH < rng[i + 1]) &
                    (sup_datas.LA_DECH > rng[i])]
    sup.to_excel(writer,str(i))
    writer.save()
