# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:06:37 2022

@author: oby_pc
"""


genre=input("Please enter the genre that you want to listen: ")
file_reader = open("songs.txt", "r")
content=file_reader.readlines()
file_reader.close()


song=""
max_popularity=-1
max_beats=-1
for line in content:
    line_lst = line.split(" | ")
    # print(line_lst[1])
    
    # convert to string parameters to int in order to make compare
    line_lst[2]=int(line_lst[2])
    line_lst[3]=int(line_lst[3])
    
    if line_lst[1]==genre:
        
        # comparing popularity score
        if line_lst[2]>max_popularity:
            song=line_lst[0]
            max_popularity=line_lst[2]
            max_beats=line_lst[3]
            
        # comparing beats_per_minute_score if popularity score is sama   
        elif line_lst[2]==max_popularity and line_lst[3]>max_beats:
            
            song=line_lst[0]
            max_popularity=line_lst[2]
            max_beats=line_lst[3]
    
print ("You can listen",song,"that has",max_popularity,"popularity and",max_beats,"beats per minute.")

 
if max_popularity > -1:
     song=song[2::] 
     print(song)
else:
     invalid_genre="There is no such",genre," genre.")
     print(invalid_genre)





def read_txt_file(filename):
    file_reader = open(filename, "r")
    content=file_reader.readlines()
    return (content)

def find_song(content,genre):
    for line in content:
        line_lst = line.split("|")
        if line_lst[1]==genre:
            print(line_lst[0]) 
    return

def main():
    genre=input("Please enter the genre that you want to listen: ")
    content=read_txt_file("songs.txt")
    song=find_song(content,genre)
    
    
    
    return content




