# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:06:50 2015

@author: VANCHAO
"""
from decimal import *
SERVICE=open("SERVICE.TXT")
dic=dict()
alpha=[chr(e) for e in range(65,91)]
#read data from file
for j in range(13):
    a=[]
    for i in range(500):
        line=SERVICE.readline().strip().split(' ')
        line.pop(3)
        line.pop(1)
        line.pop(0)
        line[0]=Decimal(line[0])
        line[1]=Decimal(line[1])
        a.append(line)
    dic[chr(j+65)]=a
del a
SERVICE.close()

REQ=open("REQ.TXT")
line=REQ.readline().strip().split(',')
temp=line[0].split('(')
qd=Decimal(temp[1])
temp=line[1].split(')')
pd=Decimal(temp[0])
REQ.close()

#read the point from the file
PROCESS=open("PROCESS.TXT")
dic1=list()
line=PROCESS.readline().strip().split(',')
for e in line:
    temp=e.split('(')
    for k in temp:
        if k in alpha:
            dic1.append(k)
for e in line:
    temp=e.split(')')
    for k in temp:
        if k in alpha:
            dic1.append(k)
dic2=list()
for i in dic1:
    if i not in dic2:
        dic2.append(i)
del dic1
del temp
del line
PROCESS.close()



info=[[]]#0 represent quality and 1 represent price
for e in dic2:
	info.append(dic[e])
f=[{Decimal('0'):Decimal('1')}]
#algorithm for manipulating
for i in range(1,len(dic2)+1):
    f.append({})
    for j in f[i-1]:
        for k in range(len(info[i])):
            if j + info[i][k][1] > pd:
                continue
            else:
                tmp=(f[i-1][j] * info[i][k][0]).quantize(Decimal('1.00'))
            if tmp < qd:
                continue
            elif j + info[i][k][1] not in f[i]:
                f[i][j + info[i][k][1]]=tmp
            elif tmp > f[i][j + info[i][k][1]]:
                    f[i][j + info[i][k][1]]=tmp
            
                
                
	
	
	
	
	
