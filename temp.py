# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv

fn='c:/圖.csv'
with open(fn,'w',newline='')as csvFile:
    csvWriter=csv.writer(csvFile)
    csvWriter.writerow(['時間','速度','高度'])
    csvWriter.writerow(['0.6','3','20'])
    csvWriter.writerow(['0.8','5','60'])