# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:08:13 2022

@author: serda
"""

def read_csv_file():
    """
    Get file name from user and open file content also skip header of csv file
    and returns list of all rows
    if given file name not exisist raise an exception
    """
    
    filename = input("Enter an input filename:")
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
            


def admin_pop(content):
     """
     loop over list by rows
     """
     #result dict to keep admin cities count and population
     result = {}  
     for line in content:
         line_lst = line.split(",")
         try:
             pop = int(line_lst[7])
         except:
             pop = 0
         #if result dict not in a city adds it to the dict
         
         if line_lst[5] not in result:
             result[line_lst[5]] = (1, pop)
         else: # update count and population
            val = result[line_lst[5]]
            result[line_lst[5]] = (val[0] + 1, val[1] + pop)  
       
     return result

def write_file_to_pop_dict(pop_dict):
    """
    writes the pop_count dict to csv file that was given by
    """
    file_name = input("Enter an output filename:")
    file_writer = open(file_name, "w")
    #file header
    file_writer.write("Administrative City,Number of Its Cities/Towns,Total Population\n")
    #loop dictionary
    for admin_city, v in pop_dict.items():
        city_count = v[0]
        total_pop = v[1]
        file_writer.write(admin_city + "," + str(city_count) + "," + str(total_pop) + "\n")
    #close file     
    file_writer.close()

#Istanbul,41.0100,28.9603,Turkey,TR,Istanbul,admin,15154000,15029231
def get_capital(file_reader):
    """
    searches the capital city
    """
    for line in file_reader:
         line_lst = line.split(",")
         if line_lst[6] == "capital":
             return line_lst[5]


def get_border_cities(file_reader):
    """
    finds min lat, lng and max lat, ltd to find ...est cities in turkey
    """
    eastern = 0
    eastern_city = ""
    western = 180
    western_city = ""
    northest = 0
    northest_city = ""
    southest = 180
    southest_city = ""
    for line in file_reader:
         line_lst = line.split(",")
         lng = float(line_lst[2])
         ltd = float(line_lst[1])
         city = line_lst[0] 
         if eastern < lng:
             eastern =  lng
             eastern_city = city
         if western > lng:
             western =  lng
             western_city = city
         if northest < ltd:
             northest =  ltd
             northest_city = city
         if southest > ltd:
             southest =  ltd
             southest_city = city
             
    return northest_city, eastern_city, southest_city, western_city
             
        
         

def main():
    try:
        content_reader = read_csv_file()
       
        #creates pop dictionary
        pop_dict = admin_pop(content_reader)
        
        capital = get_capital(content_reader)
        print("Capital city :", capital)
    
        northest, eastern, southest, western = get_border_cities(content_reader)
        print("Most eastern city :", eastern)
        print("Most western city :", western)
        print("Most northest city :", northest)
        print("Most southest city :", southest)
        #writes population infomation to file
        write_file_to_pop_dict(pop_dict)
             
        
    except FileNotFoundError as fne:
        pass
        



main()