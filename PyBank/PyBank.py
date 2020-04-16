# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:31:12 2020

@author: aditm
"""
import os
import csv

TotalMonths = 0
Net = []
Month = []
Diff_Net = []
csvpath = os.path.join('..', 'PyBank','Resources','budget_data.csv') 
with open(csvpath, encoding = 'utf-8') as csvfile:
    next(csvfile)
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        TotalMonths += 1
        #Work on Parts 2 - 5. 
        #Profit/Loss
        NetAmount = row[1]
        Net.append(NetAmount)
        TotalNet = Net[:-3]
        for i in range(0, len(TotalNet)):
            TotalNet[i] = int(TotalNet[i])
        for j in range(1, len(TotalNet)):
            Diff_Net.append(TotalNet[i] - TotalNet[i-1])
        Diff_Net = list(dict.fromkeys(Diff_Net))
        #Months
        MonthTotal = row[0]
        Month.append(MonthTotal)
        TotalMonth = Month[:-3]
        #Turn Diff_Net and Months into a zip file so that you can retrieve months for parts 4-5
        Data = zip(TotalMonth, TotalNet)
        data = zip(TotalMonth, TotalNet)
    #Calculations
    SumTotal = sum(TotalNet)
    #Maximum
    Maximum = max(Diff_Net)
    Max = TotalNet.index(max(TotalNet))
    MaxZip = list(Data)[Max][0]
    #Mininum
    Mininum = min(Diff_Net)
    Min = TotalNet.index(min(TotalNet))
    MinZip = list(data)[Min][0]
    #Average Change in Profits
    Average = sum(Diff_Net)/len(Diff_Net)
    print(f'Financial Analysis')
    print(f'------------------------------')
    print(f'Number of Months: {TotalMonths - 3}')
    print(f'Net Profit/Loss: $ {SumTotal}')
    print(f'Average Change: $ {round(Average, 2)}')
    print(f'Greatest Increase in Profits: {MaxZip} ($ {Maximum})')
    print(f'Greatest Decrease in Profits: {MinZip} ($ {Mininum})')




