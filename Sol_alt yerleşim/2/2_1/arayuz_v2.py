# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:51:18 2022

@author: oby_pc
"""

# İmport values
import pandas as pd
import numpy as np

def packMyItems(siparisArray):
    data = pd.read_excel('data.xlsx')
    siparis=pd.DataFrame(siparisArray,columns=["Kod No","Adet"])
    
    
    def findDimentions(kod):    
        veri=data[data["Kod No"] ==kod]
        en=float(veri["EN"].values)
        boy=float(veri["BOY"].values)
        
        return (en,boy,kod)
    
    
         
    
    # packing----------------------------------------------------
    from rectpack import newPacker
    from itertools import repeat
    
    rectangles = []
 

        
    for i in range(len(siparisArray)):
        
        kod=siparisArray[i,0]
        
        #checks kod in veri if not raise error
        if kod not in data["Kod No"].values:
            popup(kod).pack()
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
    colorList=["#00ffff","#85C1E9","#E5E7E9","#E6B0AA","#D2B4DE",
               "#A9DFBF","#F9E79F","#B2BABB","#16A085","#EB984E",
               "#8E44AD","#909497","#2ECC71","#424949","#0E6655",
               "#BB8FCE","#27AE60","#F7DC6F"]
    

    
    
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
    return

#%%

#----------arayüz

from tkinter import *
from tkinter import messagebox
root =Tk() #first thing
root.title("Ürün Yerleşim Ekranı")
root.geometry("270x580")


sipariskod=[] #entry object
siparisadet=[]



def startPack():
    sipariskod2=[] #values
    siparisadet2=[]
    for i in range (20):
        try:
            kod=int(sipariskod[i].get())
            sipariskod2.append(kod)
        except:
            continue
    for i in range (20):
        try:
            adet=int(siparisadet[i].get())
            siparisadet2.append(adet)
        except:
            continue
    
    siparisArray=np.column_stack((sipariskod2,siparisadet2))
        
    packMyItems(siparisArray)
    
    
def popup(kod):
    messagebox.showinfo("Kod Hatası!",
                        "{} nolu kod veri listesinde bulunmamaktadır!!".format(kod))    
    

# text box
for i in range(1,21):
    kodNo=Entry(root,width=12)
    kodNo.grid(row=i,column=0,padx=1,pady=3)
    sipariskod.append(kodNo)
    
for i in range(1,21):
    adet=Entry(root,width=12)
    adet.grid(row=i,column=1,padx=1,pady=3)
    siparisadet.append(adet)

# text box label
kodNo_label=Label(root,text="Kod No:",pady=1)
kodNo_label.grid(row=0,column=0)

adet_label=Label(root,text="Adet:",pady=1)
adet_label.grid(row=0,column=1)



# create buy button

pack=Button(root,text="yerleştir",command=startPack)
pack.grid(row=22,column=0, columnspan=2,pady=20,padx=20,ipadx=50)

#line
# my_canvas=Canvas(root,width=300,height=200)
# my_canvas.pack()
# my_canvas.crate_line(50,10,50,50,fill="black")

root.mainloop()








