# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:00:13 2022

@author: Manisha Venkat
"""
from nltk.parse import DependencyGraph, DependencyEvaluator
import pandas as pd 

##Read CONLL06 Files ##

with open(r"C:\Users\Manisha Venkat\Documents\GitHub\SDP\wsj_dev.conll06.pred", encoding="utf-8") as file_pred:
    lines = file_pred.readlines()

##Write to Another File##

with open(r"C:\Users\Manisha Venkat\Documents\GitHub\SDP\dummypred.txt",'w', encoding="utf-8") as file_dummy:
    dummy_lines = file_dummy.writelines(lines)

## Tokenize file_pred ##

tokens_pred = [sub.split() for sub in lines]
print(tokens_pred)

## Print i-th token in j-th sentence and manually check ##

print(str(tokens_pred[1]))
print(str(tokens_pred[1][3]))

## manual check works ##

### Calculation UAS and LAS ###

## Adding Gold Standard file for comparison as we need no. of correct tokens ##

with open(r"C:\Users\Manisha Venkat\Documents\GitHub\SDP\wsj_dev.conll06.pred", encoding="utf-8") as file_gold:
    gold_lines = file_gold.readlines()
    
## Creating new pred and gold files with different columns for each token, see variable explorer for visual ##

index = [x[1] for x in tokens_pred]   # ['1', '2', '3', '4', '5']
form = [x[3][0] for x in lines] 


##split_lines = tokens_pred[0].str.split(" ", n=10, expand=True)

## Making seperate columns for each element such as ID, Form, Lemma etc ##

##lines["ID"] = split_lines[0]




