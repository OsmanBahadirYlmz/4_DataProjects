# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 00:40:10 2021

@author: oby_pc
"""

import numpy as np
import pandas as pd
import re
from nltk.stem.porter import PorterStemmer
# gövdesine ayarmak
ps=PorterStemmer()
from nltk.corpus import stopwords

yorumlar = pd.read_excel("yorumlar.xlsx")
stop_words=pd.read_excel("stop_words.xlsx")
derlem=[]
for i in range(yorumlar.shape[0]):
    yorum=re.sub("[^a-zA-ZığĞüÜşŞİöÖçÇ]"," ", yorumlar["yorum"] [i])
    yorum=yorum.lower()
    yorum=yorum.split()
    yorum=[ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words("turkish"))]
    yorum= " ".join(yorum)
    
    
    derlem.append(yorum)




