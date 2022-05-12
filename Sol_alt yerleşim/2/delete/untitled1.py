# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:51:18 2022

@author: oby_pc
"""

# İmport values
import pandas as pd
import numpy as np

data = pd.read_excel('data.xlsx')
siparis=pd.read_excel('siparis.xlsx')
siparisArray=siparis.values


def findDimentions(kod):    
    veri=data[data["Kod No"] ==kod]
    en=float(veri["EN"].values)
    boy=float(veri["BOY"].values)
    
    return (en,boy,kod)

a1=findDimentions(4078)
print(a1)
print(siparisArray[0,0])
      

kod=(siparisArray[0,0])
a2=findDimentions(kod)






# packing----------------------------------------------------
from rectpack import newPacker
from itertools import repeat

rectangles = []
# rectangles.extend(repeat((472,378),3))
# rectangles.extend(repeat((525,420),3))
# rectangles.extend(repeat((577,493),3))
# rectangles.extend(repeat((420,477),3))

# rectangles.extend(repeat((246.75,1060.5),6))
# rectangles.extend(repeat((490.35,561.75),1))


# take input from sipariş excel and make a rectangle  
for i in range(len(siparisArray)):
    
    kod=siparisArray[i,0]
    
    #checks kod in veri if not raise error
    if kod not in data["Kod No"].values:
        raise Exception("{} nolu kod veri listesinde bulunmamaktadır!!".format(kod) )   
    
    adet=siparisArray[i,1]
    enboy=findDimentions(kod)
    rectangles.extend(repeat(enboy,adet))
    print(i)
    


bins = [(3200, 1500)]*170

packer = newPacker()

# Add the rectangles to packing queue
for r in rectangles:
	packer.add_rect(*r)

# Add the bins where the rectangles will be placed
for b in bins:
	packer.add_bin(*b)

# Start packing
packer.pack()

import matplotlib.pyplot as plt
from matplotlib import patches

#for different colors i added color list for each rect
colorList=["#00ffff","#85C1E9","#E5E7E9","#E6B0AA","#D2B4DE"
           "#A9DFBF","#F9E79F","#B2BABB","#16A085","#EB984E"
           "#8E44AD","#909497","#2ECC71","#424949","#0E6655"
           "#BB8FCE","#27AE60","#F7DC6F"]

siparisIndex=siparis[siparis["Kod No"]==4045].index.values


output = []
for index, abin in enumerate(packer):
  bw, bh  = abin.width, abin.height
  print('bin', bw, bh, "number of rectangles in bin", len(abin))
  fig = plt.figure()
  ax = fig.add_subplot(111, aspect='equal')
  for rect in abin:
    x, y, w, h,rid = rect.x, rect.y, rect.width, rect.height, rect.rid
    output.append([x,y,w,h])
    plt.axis([0,bw,0,bh])
    print('rectangle', w,h,rid)
    
    #different color index
    siparisIndex=siparis[siparis["Kod No"]==rid].index.values
    boxColor=colorList[int(siparisIndex)]
    
    ax.add_patch(
        patches.Rectangle(
            (x, y),  # (x,y)
            w,          # width
            h,          # height
            facecolor=boxColor,
            edgecolor="black",
            linewidth=3,
            
        )
   
    )
    plt.text(x+(w/2)-190, y+h/2,"%d, %d, %d" %(w,h,rid),color="red", fontsize=5)

  fig.savefig("rect_%(index)s.png" % locals(), dpi=144, bbox_inches='tight')

# printing the rectangle coordinates to plot them in P5JS
print(output)
print("---------")
print(packer.rect_list())


all_rects = packer.rect_list()
for rect in all_rects:
	b, x, y, w, h, rid = rect


