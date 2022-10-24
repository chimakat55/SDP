# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:00:13 2022

@author: Manisha Venkat
"""
from nltk.parse import DependencyGraph, DependencyEvaluator
import pandas as pd 
import numpy as np

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

print(tokens_pred[1])
print(tokens_pred[1][3])

## manual check works ##

### Calculation UAS and LAS ###

## Adding Gold Standard file for comparison as we need no. of correct tokens ##

with open(r"C:\Users\Manisha Venkat\Documents\GitHub\SDP\wsj_dev.conll06.gold", encoding="utf-8") as file_gold:
    gold_lines = file_gold.readlines()

tokens_gold = [sub.split() for sub in gold_lines]
print(tokens_gold)    

## Creating new pred and gold files with different columns for each token, see variable explorer for visual ##
## Making seperate columns for each element such as ID, Form, Lemma etc ##

tokens_pred_sorted = pd.DataFrame(tokens_pred)
tokens_pred_sorted.rename(columns = {0:'ID', 1:'Form', 6:'Head', 7:'Relation' }, inplace = True)
tokens_pred_sorted = tokens_pred_sorted.dropna(how='all')


tokens_gold_sorted = pd.DataFrame(tokens_gold)
tokens_gold_sorted.rename(columns = {0:'ID', 1:'Form', 6:'Head', 7:'Relation' }, inplace = True)
tokens_gold_sorted = tokens_gold_sorted.dropna(how='all')

## Creating new column 'Correst Tokens' to identify mismatched heads between the pred and gold dataframes##

tokens_pred_sorted['Correct Tokens'] = np.where((tokens_pred_sorted['Head'] == tokens_gold_sorted['Head']),'1', '0')

## Count the no. of 0s or mismatches ##

Correct_Heads = (tokens_pred_sorted['Correct Tokens'] != '0').values.sum()
print(Correct_Heads)

UAS = (Correct_Heads/26595)*100
print(UAS)

## Calculating LAS ##

tokens_pred_sorted['Correct Head-Label'] = np.where(((tokens_pred_sorted['Head'] == tokens_gold_sorted['Head']) & (tokens_pred_sorted['Relation'] == tokens_gold_sorted['Relation'])),'1', '0')

Correct_Heads_Labels = (tokens_pred_sorted['Correct Head-Label'] != '0').values.sum()
print(Correct_Heads_Labels)

LAS = (Correct_Heads_Labels/26595)*100
print(LAS)
