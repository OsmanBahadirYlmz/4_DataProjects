

weights=eval(input())
grades=eval(input())
total=0 #sum of grade x weight
gradeCounter=0 #in order to find related weight i put this variable

for grade in grades: #i itarate every grade
    if grade==-1:   #this line terminates loop if studens grade equals -1
        break
    multiplication=grade*weights[gradeCounter] #calculation of each week grade
    total+=multiplication       #sum of each week's grades
    gradeCounter+=1     #make an increment to find related weights
    

print("%.2f"%total)





# [0.1,0.05,0.05,0.4,0.2,0.2]
# [55,100,0,66.6,21.4,78]

# [0.12,0.45,0.14,0.24,0.05]
# [28.8,-1,77.7,-1,0]

# [0.22,0.23,0.05,0.24,0.26]

# [-1,55.8,47,99,21.1]




















