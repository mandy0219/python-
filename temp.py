# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv

fn='c:/圖.csv'
with open(fn) as csvFile:
    csvReader=csv.reader(csvFile)
    listReport=list(csvReader)
print(listReport)