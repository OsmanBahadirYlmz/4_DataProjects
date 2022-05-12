# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 15:23:53 2022

@author: oby_pc
"""

def read_csv_file(filename):
    """
    Get file name from user and open file content also skip header of csv file
    and returns list of all rows
    if given file name not exisist raise an exception
    """
    
    
    try:
        file_reader = open(filename, "r")
        #skip header
        file_reader.readline()
        #reads all rows in file
        content_reader = file_reader.readlines()
        #close csv file
        file_reader.close()
        return content_reader
        
    except FileNotFoundError as fne:
        print(filename, "does not exist")
        raise fne

        
        


def do_playersdict(players):
    # take content as an argument and transfer it to a dictionary
    playersdict={}
    for line in players:
        line_lst = line.split(",")
        if line_lst[0] in playersdict:
          playersdict[line_lst[0]].append(line_lst[1])
        else:
          
          playersdict[line_lst[0].strip()] = int(line_lst[1].strip())
    return playersdict


def delta(player_1,player_2):
    return 1/(1+2**((player_1-player_2)/100))
    




def update_playersdict(playersdict,games):
    # create a new dict which contains uptaded selo
    playersdict2=playersdict.copy()
    for line in games:
     
        line_lst = line.split(",")
        
        player1=line_lst[0]
        player2=line_lst[1]
        # check if it is on plyerslist
        if player1 in  playersdict2:
            pass
        else:
            playersdict2[player1]=1500
            
        if player2 in  playersdict2:
            pass
        else:
            playersdict2[player2]=1500    
      
        player1selo=playersdict2[player1]
        player2selo=playersdict2[player2]
      
        
      
        
        # make selo increase or decrease depend on result
        if (line_lst[2].strip())=="1-0":
               
            
            point=round(200*delta(player1selo,player2selo))
            
            # update player
            playersdict2[player1]=playersdict2[player1]+point
            playersdict2[player2]=playersdict2[player2]-point
            
        
        if line_lst[2]=="0-1":
            
            point=round(200*delta(player2selo,player1selo))
            # update player
            playersdict2[player1]=playersdict2[player1]-point
            playersdict2[player2]=playersdict2[player2]+point
            
            
        
        if line_lst[2]=="1/2-1/2":
            pass
        return playersdict2
    
def print_result(updatedplayersdict):
    for key in updatedplayersdict:
        print(key+": ",updatedplayersdict[key])
 
    
def main():    
    players=read_csv_file("players.csv") 
    playersdict=do_playersdict(players)
    
    games= read_csv_file("games.csv") 
    updatedplayersdict =update_playersdict(playersdict,games)  
    print_result(updatedplayersdict)
        
    

main() 
      
     










