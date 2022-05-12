# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:42:27 2022

@author: oby_pc
"""
def char_analyse(L):
    result={}
    for word in L:
        chars=list(word)
        for char in chars:
            if char in result:
                value=result[char]
                result[char]=value+1
            else:
              result[char] = 1
            
    return result

# find word which include "abc.."
def find_word(L,words):
    
    lenght=len(L)
    
    result=[]
    for word in words:
        for char in L:
            if char not in word:
                break
            if char==L[-1]:
                result.append(word)
    return result

# remove word which include "abd..."
def remove_word(L,words) : 
    result=words.copy()            
    for word in words:
        for char in L:
            if char in word:
                result.remove(word)
                break
           
    
    return result

# remove word which not in psition
def remove_wordbychar(char,words,position):
    result=[]
    for word in words:
        if word[position]==char:
            result.append(word)
        else:
            pass
    return result
# remove word which in pozition
def remove_wordbychar2(char,words,position):
    result=words.copy()
    for word in words:
        if word[position]==char:
            result.remove(word)
        else:
            pass
    return result

    
import itertools

def find_subset(L,n):
    return list(itertools.combinations(L, n))
    
    


def find_wordBysubset(analyse,n,words):
    commonchars=find_subset(analyse[-n:],5)
    result=find_word(commonchars,words)
    if result==[]:
        find_wordBysubset(analyse, n+1,words)
    else:
        return result
    
#try to give all word a point related its commens 
def word_points(words,analysedict)  :
    
    result={}
    for word in words:
        point=0
        for i in range(5):
            charpoint=analysedict[word[i]]
            point+=charpoint
      
        result[word] = point
    return result
        
            
        
 
    

import pandas as pd
import numpy as np
sozluk=pd.read_csv("ortak_kelimeler.txt")
print(len(sozluk))
print(len(sozluk.iloc[4,0])==5)

all5words=[]
for i in range( len(sozluk)):
    try:
        if len(sozluk.iloc[i,0])==5:
            all5words.append(sozluk.iloc[i,0])
    except:
        continue
        
analyse1=char_analyse(all5words)
analyse2=sorted(analyse1,key=analyse1.get)


mostCommon=analyse2[-6:]
subs=find_subset(mostCommon, 5)


for sub in subs:
        words=find_word(sub, all5words)
        if words!=[]:
            break

"""
"""
# guess1






"""
vakıf tahmin
"""
# ka=find_word("ka",all5words)
# analyse3=char_analyse(ka)
# analyse4=sorted(analyse3,key=analyse3.get)


# kaı=find_word("kaı",all5words)

# kaı_erimnt=remove_word("erimnt", kaı)
# analyse5=char_analyse(kaı_erimnt)
# analyse6=sorted(analyse5,key=analyse5.get)

# kaı_erimnt_1=remove_wordbychar("a", kaı_erimnt, 1)

# kaı_erimnt_2=remove_wordbychar2("a", kaı_erimnt_1, 4)


# kaı_erimnt_3=remove_wordbychar2("k", kaı_erimnt_2, 3)

# kaı_erimnt_4=remove_wordbychar2("ı", kaı_erimnt_3, 4)



# analyse6=char_analyse(kaı_erimnt_4)
# analyse7=sorted(analyse6,key=analyse5.get)


# kaı_erimnt_4_points=word_points(kaı_erimnt_4, analyse6)

# kaı_erimnt_5=remove_wordbychar("k", kaı_erimnt_3, 0)




# #guess3

# kaı_erimntlps_1=remove_word("lps", kaı_erimnt_4)
# kaı_erimntlps_2=remove_wordbychar2("k",kaı_erimntlps_1,0)





# akı=remove_wordbychar("a", all5words, 1)
# akı2=remove_wordbychar("k", akı, 2)
# akı3=remove_wordbychar("ı", akı2, 3)
# akı4=remove_word("mrlçbşvf", akı3)







