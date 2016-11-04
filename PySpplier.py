# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 12:45:44 2016

@author: user11
"""
import sys
import pandas as pd
from datetime import datetime, date

file = r'C:\Users\user11.HPO-SAMAT\Documents\GitHub\PySupplier/data.csv'

def file2df(fname):
    """CSV import function"""

    data = pd.read_csv(fname,
                       sep=None)
    return data

data = file2df(file)
data = data[data['RE_FOUR'] == 175]
grouped = data.groupby('LA_DECH')
start = date(2016, 1, 1)
end = date(2016, 12, 31)
rng = pd.date_range(start, end, freq='BM')
