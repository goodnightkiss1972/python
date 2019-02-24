# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:43:19 2018

@author: fabie
"""

def F(x):
    return (6*x+1)

def dichotomie(a,b,p,limite):

    binf=a
    bsup=b
    comptetour=0
    
    while (bsup-binf)>p:
        comptetour=comptetour+1
        if comptetour==limite:
            return ("j'abandonne j'ai fait trop de tours")
        if (F(binf)*F((binf+bsup)/2)) < 0:
            binf=binf
            bsup=(bsup+binf)/2
        else: 
            binf=(bsup+binf)/2
            bsup=bsup
        
    return (binf,bsup,comptetour)

print(dichotomie(-10000,10000,1E-5,500))

           
    
