
def process_books(book_titles):
    book_counts=[0,0,0,0,0]
    for i in range( len(book_titles)):
        book_titles[i]
        if book_titles[i][0]=="A":
            book_counts[0]+=1
            
        if book_titles[i][0]=="B":
            book_counts[1]+=1      
            
        if book_titles[i][0]=="C":
            book_counts[2]+=1        

        if book_titles[i][0]=="D":
            book_counts[3]+=1

        if book_titles[i][0]=="E":
            book_counts[4]+=1
    
    return book_counts



