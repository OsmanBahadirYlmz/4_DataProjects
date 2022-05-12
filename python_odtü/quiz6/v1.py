def find_student(studentdict,coursecredit,mode):
    result_gpa=0
    result_student="a"
    first_gpa=True
    
    for key in studentdict:
        gpa=0
        totalcredit=0
        

        
        for i in range (0,len(studentdict[key]),2):
            course=studentdict[key][i]
            grade=studentdict[key][i+1]
            if grade=="A":
                grade=4
            if grade=="B":
                grade=3
            if grade=="C":
                grade=2
            if grade=="D":
                grade=1
                
             
                
            coursecredit_val=coursecredit[course]
            gpa+=coursecredit_val*grade
            totalcredit+=coursecredit_val
    
        gpa=gpa/totalcredit
        if first_gpa:
            result_gpa=gpa
            result_student=key
            first_gpa=False
            
        
        if mode=="most":
            if gpa>result_gpa:
                result_gpa=gpa
                result_student=key
            
        if mode=="least":
            if gpa<result_gpa:
                result_gpa=gpa
                result_student=key
                
    return [result_student,result_gpa]
            
            
