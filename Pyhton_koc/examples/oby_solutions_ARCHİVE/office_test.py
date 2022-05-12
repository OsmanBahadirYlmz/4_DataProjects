# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 15:53:51 2022

@author: oby_pc
"""
import office
def main():
    L = []
    office.display_all(L)
    print('---------------------------------')
   
    office.add_employee(L, 'Cigdem Gunduz', 1853, 'ENG108A')
    office.add_employee(L, 'Serkan Cil', 1111, 'GRT 02')
    office.add_employee(L, 'Mehmet SAYAR', 2222, 'ENG118A')
    office.add_employee(L, 'Seher Ozcelik', 3333, 'ENG123')
    office.add_employee(L, 'Ulkem Kasapoglu', 3333, 'ENG123')
    office.display_all(L)
    print('----------++++++++++-----------------------')
    
    office.add_employee(L, 'CIGdem GuNduz', 4444, 'SNA 52')
    office.add_employee(L, 'Seher Ozcelik', 5555, 'SOS B7')
    print('---------------------------------')
    office.display_all(L)
    print('---------------------------------')
    office.show_employee(L, 'Cigdem GUNDUZ')
    print('---------------------------------')
    office.show_employee(L, 'Ulkem Kasapoglu')
    print('---------------------------------')
    office.show_employee(L, 'Mehmet Sayar')
    print('---------------------------------')
    office.show_employee(L, 'Merve KUNAK')
    print('---------------------------------')
    office.remove_employee(L, 'Mehmet Sayar')
    office.display_all(L)
    print('---------------------------------')
    office.show_employee(L, 'Mehmet Sayar')
    print('---------------------------------')
    office.remove_employee(L, 'Merve KUNAK')
    print('---------------------------------')
    office.remove_employee(L, 'Cigdem Gunduz')
    office.remove_employee(L, 'Seher Ozcelik')
    office.remove_employee(L, 'Ulkem KASapoglu')
    office.display_all(L)
    print('---------------------------------')
    office.remove_employee(L, 'Serkan Cil')
    office.display_all(L)
    print('---------------------------------')
main()