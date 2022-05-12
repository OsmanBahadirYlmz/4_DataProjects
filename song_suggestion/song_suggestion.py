# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 18:08:43 2022

@author: Kemal Emre Özkaya, id:29455, section:A2 
"""


file_reader = open("songs.txt", "r")
content=file_reader.readlines()
file_reader.close()

def find_song(content,genre):
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
   
   if max_popularity > -1:
        song=song[2::] 
        print ("You can listen",song,"that has",max_popularity,"popularity and",max_beats,"beats per minute.")

        return
   else:
        print("There is no such genre",genre+".")
        return


def main():
    
    # I defined while loop in order to repeat code keep suggesting song 
    
    while(True):        
        # request an input from user
        genre=input("Please enter the genre that you want to listen: ")
        
        # checks user input is quit
        if genre=="quit":
            print("The program is closed.")
            break
        find_song(content,genre)
        




main()
