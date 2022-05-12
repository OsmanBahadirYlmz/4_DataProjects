
file_reader = open("characters.txt", "r")

features=file_reader.readline().split(";")
for i in range(9):
    features[i]=features[i].lstrip()
content_reader = file_reader.readlines()

file_reader.close()


dict1={}
for line in content_reader:
    line_lst = line.split(";")
    name=line_lst[0]
    dict1[name]=[line_lst[1].lstrip()]
    for i in range(2,9):        
        dict1[name].append(line_lst[2])
    


file_reader = open("question1.txt", "r")
content_reader2= file_reader.readlines()

file_reader.close()

questions=[]
for line in content_reader2:
    line_lst = line.split(" = ")
    question=line_lst[0]
    answer=line_lst[1]
    questions.append([question,answer])
    
    
def print_characters(content):
    for name in sorted(content.keys()):
        print("\n")
        print (name, end=" - ")
        for i in range (8):
           
           print (features[i+1], end=": ")
           print (content[name][i], end=",")
    return
        
        
print_characters(dict1)      
    
    
    

    





















