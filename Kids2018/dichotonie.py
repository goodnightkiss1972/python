# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:43:19 2018

@author: fabie
"""

def F(x):
    return (6*x+1)

a=3
b=4
p=1E-20
limite=100

binf=a
bsup=b
comptetour=0

while (bsup-binf)>p:
    comptetour=comptetour+1
    if comptetour==limite:
        print ("error")
    if (F(binf)*F((binf+bsup)/2)) < 0:
        binf=binf
        bsup=(bsup+binf)/2
    else: 
        binf=(bsup+binf)/2
        bsup=bsup


print (binf,bsup)

            
    
