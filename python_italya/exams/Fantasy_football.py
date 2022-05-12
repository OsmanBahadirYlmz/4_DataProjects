# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:08:30 2022

@author: oby_pc
"""

def read_data(filename):
    data = dict()
    try:
        with open(filename) as input_file:
            for line in input_file:
                surname,name,pos,value = line.split(", ")
                if surname not in data:
                    data[surname] = set()
                data[surname]=[name,pos,value.strip()]
    except OSError as problem_description:
        print(f"Yeuch: {problem_description}")
        exit(1)
    return data

def buy(budget,pos,number,players2):
    players=players2.copy()
    rem_budget=budget
    print("\n\n")
    print(f"{pos}: ", end=" ")
    for i in range (number):
       
        max_budget=rem_budget-(number-i-1)
        selected_value=int(1)
        
        for player in players:
            
           
            
            if (players[player][1]==pos)and(int(players[player][2])<=max_budget)and(int(players[player][2])>=selected_value):
                
                selected=(player,players[player][2])
                selected_value=int(players[player][2])
       
        rem_budget=rem_budget-selected_value
        
        
        players.pop(selected[0])
        print(" ".join(selected), end=" ")
       
        
    
    
    
    
    
    return selected

filename="Fantasy_football.txt"
players=read_data(filename)
# goalkeepers
c=buy(20,"portiere",3,players)

buy(40,"difensore",8,players)

buy(80,"centrocampista",8,players)
buy(120,"attaccante",8,players)















