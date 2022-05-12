# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:37:10 2021

@author: oby_pc
"""


import numpy as np
import pandas as pd
import re
import nltk
from nltk import FreqDist



yor1=pd.read_csv("Amazon Brand.csv")
yor2=pd.read_csv("American Soft Linen.csv")
yor3=pd.read_csv("GLAMBURG.csv")
yor4=pd.read_csv("Hammam.csv")
yor5=pd.read_csv("Hotel.csv")
yor6=pd.read_csv("Luxury Hotel.csv")
yor7=pd.read_csv("Luxury White.csv")
yor8=pd.read_csv("Qute.csv")



yorumlar = pd.concat([yor1,yor2,yor3,yor4,yor5,yor6,yor7,yor8], ignore_index="false",axis=0)
yorumlar=yorumlar.fillna(" ")
yorumlar1yıl=yorumlar[yorumlar["Rating"]==1]
yorumlar2yıl=yorumlar[yorumlar["Rating"]==2]
yorumlar3yıl=yorumlar[yorumlar["Rating"]==3]
yorumlar4yıl=yorumlar[yorumlar["Rating"]==4]
yorumlar5yıl=yorumlar[yorumlar["Rating"]==5]

yorumlar2=[yorumlar,yorumlar1yıl,yorumlar2yıl,yorumlar3yıl,yorumlar4yıl,yorumlar5yıl]


from nltk.stem.porter import PorterStemmer
# gövdesine ayarmak
ps=PorterStemmer()

from nltk.corpus import stopwords

#Preprocessing
derlem = []
allwords=[]

index_wash=[]
index_soft=[]
index_color=[]
index_absorb=[]
index_qualiti=[]
index_thick=[]
index_set=[]
index_dri=[]
index_price=[]
index_lint=[]
index_time=[]
index_look=[]
index_feel=[]
index_size=[]
index_thin =[]
index_fluffi =[]
index_shed=[]
index_dryer=[]


# tüm yıldız değerleri için 
# for j in range(5)
#     yorumlar=yorumlar2[5]
yorumlar=yorumlar2[1].reset_index()

for i in range(yorumlar.shape[0]):
    #başında ^işareti değil demek. bunları bul ve boş karakterle değiştir diyoruz
    yorum = re.sub("[^a-zA-Z]"," ", yorumlar["Body"] [i])
    #tümünü küçük harfle değiştirdik
    yorum=yorum.lower()
    # tüm kelimeleri ayırıp liste haline getirdik
    yorum= yorum.split()
    yorum=[ps.stem(kelime) for kelime in yorum if not kelime in set(stopwords.words("english"))]
    
    for kelime in yorum:
        allwords.append(kelime)
        
        # kelimelerin indexlerini bulma
        if kelime=="wash":
            index_wash.append(i)
        if kelime=="soft":
            index_soft.append(i)  
        if kelime=="color":
            index_color.append(i)    
        if kelime=="absorb":
            index_absorb.append(i)    
        if kelime=="qualiti":
            index_qualiti.append(i)
        if kelime=="thick":
            index_thick.append(i)  
        if kelime=="set":
            index_set.append(i)   
        if kelime=="dri":
            index_dri.append(i)   
        if kelime=="price":
            index_price.append(i)   
        if kelime=="lint":
            index_lint.append(i)   
        if kelime=="time":
            index_time.append(i)   
        if kelime=="look":
            index_look.append(i)   
        if kelime=="feel":
            index_feel.append(i)   
        if kelime=="size":
            index_size.append(i)   
        if kelime=="thin":
            index_thin.append(i)   
        if kelime=="fluffi":
            index_fluffi.append(i)   
        if kelime=="shed":
            index_shed.append(i)   
        if kelime=="dryer":
            index_dryer.append(i)   
                  
            
            
    yorum= " ".join(yorum)
    derlem.append(yorum)
"""
#Feautre Extraction ( Öznitelik Çıkarımı)
#Bag of Words (BOW)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 500)
X = cv.fit_transform(derlem).toarray()
y= yorumlar.iloc[:,6].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
gnb.fit(X_train,y_train)
y_pred=gnb.predict(X_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print (cm)
"""

# frequency distribution
from nltk import FreqDist

frequency_distribution = FreqDist(derlem)
freq=frequency_distribution

freq_words=frequency_distribution.most_common(50)

# freq dist 2
wordlist= " ".join(allwords)

import collections

freq_words2 = collections.Counter(allwords)


# derlem içindeki geçen xxx kelimeli yorumları bulmak
index_wash= list(dict.fromkeys(index_wash)) #duplicateleri ayırmak
yorum_wash=yorumlar.iloc[index_wash]
index_soft=list(dict.fromkeys(index_soft))
index_color=list(dict.fromkeys(index_color))
index_absorb=list(dict.fromkeys(index_absorb))
index_qualiti=list(dict.fromkeys(index_qualiti))
index_thick=list(dict.fromkeys(index_thick))
index_set=list(dict.fromkeys(index_set))
index_dri=list(dict.fromkeys(index_dri))
index_price=list(dict.fromkeys(index_price))
index_lint=list(dict.fromkeys(index_lint))
index_time=list(dict.fromkeys(index_time))
index_look=list(dict.fromkeys(index_look))
index_feel=list(dict.fromkeys(index_feel))
index_size=list(dict.fromkeys(index_size))
index_thin =list(dict.fromkeys(index_thin))
index_fluffi =list(dict.fromkeys(index_fluffi))
index_shed=list(dict.fromkeys(index_shed))
index_dryer=list(dict.fromkeys(index_dryer))

yorum_qualiti=yorumlar.iloc[index_wash]
yorum_set=yorumlar.iloc[index_set]
yorum_dri=yorumlar.iloc[index_dri]
yorum_lint=yorumlar.iloc[index_lint]
yorum_time=yorumlar.iloc[index_time]
yorum_feel=yorumlar.iloc[index_feel]
yorum_fluffi=yorumlar.iloc[index_fluffi]
yorum_shed=yorumlar.iloc[index_shed]
yorum_dryer=yorumlar.iloc[index_dryer]









