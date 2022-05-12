# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 21:51:18 2022

@author: oby_pc
"""
from rectpack import newPacker
from itertools import repeat

rectangles = []
# rectangles.extend(repeat((472,378),3))
# rectangles.extend(repeat((525,420),3))
# rectangles.extend(repeat((577,493),3))
# rectangles.extend(repeat((420,477),3))
rectangles.extend(repeat((246.75,1060.5),6))
rectangles.extend(repeat((490.35,561.75),1))
rectangles.extend(repeat((1071,519.75),6))
rectangles.extend(repeat((183.75,624.75),6))
rectangles.extend(repeat((168,630),8))




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

output = []
for index, abin in enumerate(packer):
  bw, bh  = abin.width, abin.height
  print('bin', bw, bh, "nr of rectangles in bin", len(abin))
  fig = plt.figure()
  ax = fig.add_subplot(111, aspect='equal')
  for rect in abin:
    x, y, w, h = rect.x, rect.y, rect.width, rect.height
    output.append([x,y,w,h])
    plt.axis([0,bw,0,bh])
    print('rectangle', w,h)
    ax.add_patch(
        patches.Rectangle(
            (x, y),  # (x,y)
            w,          # width
            h,          # height
            facecolor="#00ffff",
            edgecolor="black",
            linewidth=3,
            
        )
   
    )
    plt.text(x, y,"%d, %d" %(w,h),color="red", fontsize=5)

  fig.savefig("rect_%(index)s.png" % locals(), dpi=144, bbox_inches='tight')

# printing the rectangle coordinates to plot them in P5JS
print(output)
print("---------")
print(packer.rect_list())





