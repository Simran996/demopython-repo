# -*- coding: utf-8 -*-
"""
Created on Sun May  3 11:43:38 2020

@author: HP
"""
import pandas as pd
r_realEstate_transCSV = 'realEstate_trans.csv'

w_realEstate_trans_CSV = 'realEstate_trans_simran.csv'
csv_read = pd.read_csv(r_realEstate_transCSV)
csv_read = csv_read[['beds','baths','sq__ft','price']]
# calculate the correlations
coefficients = ['pearson','kendall','spearman']
csv_corr = {}
for coeffiecient in coefficients:
    csv_corr[coeffiecient] = csv_read \
        .corr(method=coeffiecient) \
        .transpose()

with open(w_realEstate_trans_CSV,'w') as write_csv:
    for corr in csv_corr:
        write_csv.write(corr + '\n')
        write_csv.write(csv_corr[corr].to_csv(sep=','))
        write_csv.write('\n')