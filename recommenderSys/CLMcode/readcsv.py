#-*-coding:utf8-*-
"""
author:xiaofan
"""

path = "../data/departuredelays.csv"
def readcsv(path):
    list = []
    f = open(path,"r")
    flag = True
    for line in f:
        if flag:
            print(line)
            flag=False
        arrs = line.strip().split(",")
        list.append(arrs)
    return list