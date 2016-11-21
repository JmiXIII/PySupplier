# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 22:29:18 2016

@author: sylvn_000
"""

import os
import glob
import re
import pandas as pd
from datetime import datetime
import xlwings as xw

# %% Configuration des chemins
path = 'C:/Users/user11.HPO-SAMAT/Documents/GitHub/PySupplier'
file = path+'/Fournisseur.csv'
doc = path + '/H2075-02.xlsx'


# %% fonction import csv
def file2df(elmnt):
    data = pd.read_csv(elmnt, sep=None)
    return data

# %% Découpage périodes mois
suppliers_datas = file2df(file)
suppliers_datas['RE_QMOU'] = suppliers_datas['RE_QMOU'].str.replace(",",".")
suppliers_datas.LA_DECH = pd.to_datetime(suppliers_datas.LA_DECH, format='%d/%m/%Y')
suppliers_datas.RE_DMOU = pd.to_datetime(suppliers_datas.RE_DMOU, format='%d/%m/%Y')
start = datetime(2015, 12, 1)
end = datetime(2016, 12, 31)
ranges = pd.date_range(start, end, freq='M')
rng = [x for x in ranges]
list_sup = []

# %% boucle de création des fichiers .xls
for supplier in suppliers_datas.RE_FOUR.dropna().unique():
    wb = xw.Book(doc)
    wb.app.screen_updating = False
    wb.app.calculation = 'manual'
    sup_datas = suppliers_datas.groupby('RE_FOUR').get_group(supplier)
    sup_datas.LA_DECH = pd.to_datetime(sup_datas.LA_DECH, format='%d/%m/%Y')
    sup_datas.RE_DMOU = pd.to_datetime(sup_datas.RE_DMOU, format='%d/%m/%Y')
    fourn = sup_datas.FO_DESI.unique()[-1]
    re_four = sup_datas.RE_FOUR.unique()[-1]
    unit = sup_datas.AR_UNIT.unique()[-1]
    fourn = re.sub('[!@#$.?/]', '', fourn) #Nettoyage des caractères spéciaux
    wb.sheets(1).range('J4').value = re_four # Ecriture code fournisseur
    wb.sheets(1).range('G13').value = unit # Ecriture unités
# %% boucle d'écriture des onglets
    for i in range(len(rng)-1):
        sup = sup_datas[(sup_datas.LA_DECH < rng[i + 1]) &
                        (sup_datas.LA_DECH > rng[i])]
        if wb.sheets(str(i+1)).range('B1').value == 'oui':
            pass
        else:
            wb.sheets(str(i+1)).range('A3').value = sup
    wb.app.calculation = 'automatic'
    wb.save(path + '/H2075-02 - ' + str(re_four)+' '+str(fourn) + '.xlsx')
    wb.app.screen_updating = True
    wb.app.quit()
# %% fin
print ('end')