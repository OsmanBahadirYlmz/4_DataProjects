#%%
import hashlib
import pickle

file_name = "data.pkl" #file which contains chain

class EggCoinBlock:
    
    def __init__(self, previous_hash, transaction_list):

        self.previous_hash = previous_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

   



class Blockchain:
    def __init__(self):
        self.chain = []
        
        file_name = "data.pkl"
        try:
            #read chain from local if avaible.
            open_file = open(file_name, "rb")
            self.chain = pickle.load(open_file)
            open_file.close()
        except:
            self.chain = []
            
        if (len(self.chain)==0):
            self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(EggCoinBlock("5", ['egg Genesis']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_hash = self.last_block.block_hash
        self.chain.append(EggCoinBlock(previous_hash, transaction_list))
        
        #save chain to local
        open_file = open(file_name, "wb")
        pickle.dump(self.chain, open_file)
        open_file.close()


    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")
            
            
            # print("-----")
            # print(last_data)
            # print(last_hash)
            # print("-----")
    def get_last_data(self):
        last_data=self.chain[len(self.chain)-1].block_data
       
        return last_data  
    def get_last_hash(self):
        
        last_hash=self.chain[len(self.chain)-1].block_hash
        return last_hash         
            
    @property
    def last_block(self):
        return self.chain[-1]
    
# müsteri1=1111
# # müsteri2=1112
# # müsteri3=1113
# # müsteri4=1114

# satici1=2001
# satici2=2002
# satici3=2003
# satici4=2004

# t1= f"{satici1} {müsteri1}\'ye {500} yumurta gönderdi"
# t2= f"{satici2} {müsteri3}\'ye {300} yumurta gönderdi"
# t3= f"{satici4} {müsteri2}\'ye {300} yumurta gönderdi"
# t4= f"{satici3} {müsteri1}\'ye {350} yumurta gönderdi"
# t5= f"{satici2} {müsteri4}\'ye {150} yumurta gönderdi"
# t6= f"{satici3} {müsteri3}\'ye {5000} yumurta gönderdi"
# t7= f"{satici2} {müsteri2}\'ye {280} yumurta gönderdi"
# t8= f"{satici3} {müsteri4}\'ye {330} yumurta gönderdi"
# t9= f"{satici1} {müsteri3}\'ye {1000} yumurta gönderdi"
# t10= f"{satici1} {müsteri2}\'ye {450} yumurta gönderdi"
# t11= f"{satici3} {müsteri1}\'ye {50} yumurta gönderdi"
# t12= f"{satici4} {müsteri1}\'ye {1250} yumurta gönderdi"



        



eggBlockChain = Blockchain()

# # eggBlockChain.create_block_from_transaction([t1, t2])
# # eggBlockChain.create_block_from_transaction([t3, t4])
# # eggBlockChain.create_block_from_transaction([t5, t6])
# # eggBlockChain.create_block_from_transaction([t7, t8])
# # eggBlockChain.create_block_from_transaction([t9, t10])
# # eggBlockChain.create_block_from_transaction([t11, t12])

# eggBlockChain.create_block_from_transaction([t1])
# eggBlockChain.create_block_from_transaction([t2])
# eggBlockChain.create_block_from_transaction([t3])


# eggBlockChain.display_chain()

# c=eggBlockChain.get_last_data()
# d=eggBlockChain.get_last_hash()
#%%


"""
tkinter
"""

from tkinter import *
root =Tk() #first thing
root.title("Ham Madde Üretici Arayüzü")
root.geometry("480x320")

def blokekle():
    musteri=musteri_id.get()
    satici=satici_id.get()
    yumurta=yumurta_sayisi.get()
    transaction= f"\"{musteri}\" id numaralı üretici, \
\"{satici}\" id numaralı satıcıya {yumurta} verildi."
    eggBlockChain.create_block_from_transaction([transaction])
    eggBlockChain.display_chain()
    
    # get last data and hash codes
    lastdata=eggBlockChain.get_last_data()
    lasthash=eggBlockChain.get_last_hash()
    
    # print hash code to text
    blok.delete("1.0",END)
    blok.insert(INSERT,lastdata)
    
    hashcode.delete("1.0",END)
    hashcode.insert(INSERT,lasthash)
    
    
    
    # clear all entries    
    musteri_id.delete(0,END)
    satici_id.delete(0,END)
    yumurta_sayisi.delete(0,END)
    return


# text box
musteri_id=Entry(root,width=30)
musteri_id.grid(row=0,column=1,padx=10 )

satici_id=Entry(root,width=30)
satici_id.grid(row=1,column=1,padx=10 )
 
yumurta_sayisi=Entry(root,width=30)
yumurta_sayisi.grid(row=2,column=1,padx=0 )

blok=Text(root,height=5, width=40,padx=5)
blok.grid(row=5,column=1,padx=1,pady=5,columnspan=3 )

hashcode=Text(root,height=2, width=40,padx=5)
hashcode.grid(row=6,column=1,padx=1,pady=5,columnspan=4 )

# text box label

musteri_id_label=Label(root,text="Ham Madde Üretici ID:",pady=10)
musteri_id_label.grid(row=0,column=0)

satici_id_label=Label(root,text="Satıcı ID:",pady=10)
satici_id_label.grid(row=1,column=0)

yumurta_sayisi_label=Label(root,text="Yapılan İşlem:",pady=10)
yumurta_sayisi_label.grid(row=2,column=0)

blok_label=Label(root,text="Blok verisi",pady=1)
blok_label.grid(row=5,column=0)

hashcode_label=Label(root,text="Hash Kodu",pady=1)
hashcode_label.grid(row=6,column=0)


# create buy button

satınal=Button(root,text="Gönder",command=blokekle)
satınal.grid(row=4,column=0, columnspan=2,pady=10,padx=10,ipadx=100)


root.mainloop()
  















