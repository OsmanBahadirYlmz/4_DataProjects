# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 22:42:27 2022

@author: oby_pc
"""
# which char accur how many times
def file_write(L,name)   :
    file_writer = open(name, "w")
    #file header
    
    #loop dictionary
    for word in L:
       
        file_writer.write(word+"\n")
    #close file     
    file_writer.close()
    return
def file_read(filename):
    """
    Get file name from user and open file content also skip header of csv file
    and returns list of all rows
    if given file name not exisist raise an exception
    """
    
    
    try:
        file_reader = open(filename, "r")
    
        #reads all rows in file
        content_reader = file_reader.readlines()
        #close csv file
        file_reader.close()
        return content_reader
        
    except FileNotFoundError as fne:
        print(filename, "does not exist")
        raise fne

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
              
    result2=sorted(result,key=result.get)
            
    return result,result2
# selected char accur which position,
def char_position(L,char):
    result={}
    for i in range(5):
        for word in L:
            if word[i]==char:
                if i in result:
                  result[i]=result[i]+1
                else:
                  result[i] = 1
    return result



# remove word which include "abd..."
def gray_char(L,words) : 
    result2=words.copy()            
    for word in words:
        for char in L:
            if char in word:
                result2.remove(word)
                break
           
    
    return result2

# remove word which not in psition
def green_char(char,words,position):
    result3=words.copy()
    for word in words:
        if word[position]!=char :
            result3.remove(word)
        else:
            pass
    return result3
# remove word which in pozition
def yellow_char(char,words,position):
    result4=words.copy()
    for word in words:
        if char not in word:
            result4.remove(word)
        if word[position]==char:
            result4.remove(word)
        else:
            pass
    return result4

    
import itertools

def find_subset(L,n):
    return list(itertools.combinations(L, n))
    
    


# def find_wordBysubset(analyse,n,words):
#     commonchars=find_subset(analyse[-n:],5)
#     result=find_word(commonchars,words)
#     if result==[]:
#         find_wordBysubset(analyse, n+1,words)
#     else:
#         return result
    
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
        
            
        
 
    
##sözlük okuma bölümü hız için comment yapıldı
# import pandas as pd
# import numpy as np
# sozluk=pd.read_csv("ortak_kelimeler.txt")
# print(len(sozluk))
# print(len(sozluk.iloc[4,0])==5)

# all5words=[]
# for i in range( len(sozluk)):
#     try:
#         if len(sozluk.iloc[i,0])==5:
#             all5words.append(sozluk.iloc[i,0])
#     except:
#         continue


import pandas as pd
import numpy as np
# sozluk=pd.read_csv("Birleştirilmiş_Sözlük_Kelime_Listesi.txt")
# print(len(sozluk))
# print(len(sozluk.iloc[4,0])==5)


# all5words2=[]
# for i in range( len(sozluk)):
#     try:
#         if len(sozluk.iloc[i,0])==5:
#             all5words2.append(sozluk.iloc[i,0])
#     except:
#         continue
        





# for sub in subs:
#         words=find_word(sub, all5words)
#         if words!=[]:
#             break
def wordByword(L):
    result={}
    for selected in L:
        counter=0
        for word in L:
            if selected==word:
                continue
            else:
                for i in range(5):
                    if selected[i]==word[i]:
                        counter+=2
                        continue
                    if selected[i] in word:
                        counter+=1
            result[selected]=counter
            
    return result
                     
def main1(L,words): #"ge,sr,yi,gk,ga"
    result=words.copy()
    L1=L.split(",")
    for item in L1:
        if item[0]=="g":
            result=gray_char(item[1], result)
        if item[0]=="s":
            result=yellow_char(item[1], result, L1.index(item))
        if item[0]=="y":
            result=green_char(item[1], result, L1.index(item))
      
    result2,result3=char_analyse(result)      
            
    
    
    return result,result2,result3 #remaining words,char analyse,sorted char analyse,

hitpoint=2
correctpoint=3
def main2(words):
    result={}
    for word in all5words:
        
        point=0
        for guess in words:
            
            for i in range(5):
               
                if word[i] in guess:
                    point+=hitpoint
                    if word[i]==guess[i]:
                        point+=correctpoint
        result[word]=point
        
        
        
    return result                


def main3(words):
    result={}
    for word in all5words:
        print(word)
        point=0
        for guess in words:
            
            lst1=[]
            for i in range (5):
                if word[i]==guess[i]:
                    lst1.append("y"+word[i])
                    continue
                elif word[i] in guess:
                    lst1.append("s"+word[i])
                    continue
                else:
                    lst1.append("g"+word[i])
                    
            lst1=",".join(lst1)  
          
            
            temp_result,result2,result3=main1(lst1,words)
            point+=len(temp_result)
        
            
        result[word]=point
        
    return result




#kelime okuma yazma
# file_write(all5words2, "all5words3.txt")
# file_write(all5words, "all5words.txt")
all5words=file_read("all5words.txt")
all5words2=file_read("all5words2.txt")


  





"""
erika
"""
tahmin1,char1,char2=main1("se,gr,si,gk,ga",all5words2)    
# tahmin2,char1,char2=main1("se,gr,gi,gk,ga",all5words)     
analyse1=main2(tahmin1)
analyse2=main3(tahmin1)


# # tahmin1_2=file_read("tahmin1.txt")
# analyse3=main3(tahmin1)



# """

# """
tahmin3,char1,char2=main1("yd,se,gn,gl,si",tahmin1)    
    
analyse1=main2(tahmin3)
analyse2=main3(tahmin3)
# file_write(tahmin2, "tahmin1.txt")

# tahmin1_2=file_read("tahmin1.txt")
# analyse3=main3(tahmin3)


# tahmin4,char1,char2=main1("ge,gr,gi,sk,sa",all5words2)  
# tahmin5,char1,char2=main1("sa,gn,sl,gı,sk",tahmin4)    





# tahmin7,char1,char2=main1("gç,ya,yk,ga,gl",tahmin5)  

# """
# kudüm
# """

# rk_eiauum2,char1,char2=main1("yk,gu,gd,yü,gm",rk_eia2)    
# analyse6=main2(rk_eiauum2)
# analyse7=main3(rk_eiauum2)






# """
# erika
# """
# ar_eik,char1,char2=main1("ge,sr,gi,gk,ya",all5words)    
    
# analyse1=main2(ar_eik)
# analyse2=main3(ar_eik)


# """
# sorum müthiş
# """
# ars_eikoum,char1,char2=main1("ys,go,sr,gu,gm",ar_eik)   

# analyse1=main2(ars_eikoum)
# analyse2=main3(ars_eikoum)



# """
# deneme barut
# """
# deneme,char1,char2=main1("gb,ya,sr,gu,gt",ar_eik)   










