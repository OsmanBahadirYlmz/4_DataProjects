
import hashlib

class EggCoinBlock:
    
    def __init__(self, previous_hash, transaction_list):

        self.previous_hash = previous_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

   

# # some examples
# message = "Python is great"

# h1 = hashlib.sha256(message.encode())
# print(h1)

# print(h1.hexdigest())


# t1 = "Noah sends 5 GC to Mark"
# t2 = "Mark sends 2.3 GC to James"
# t3 = "James sends 4.2 GC to Alisson"
# t4 = "Alisson sends 1.1 GC to Noah"


# block1 = EggCoinBlock('firstblock', [t1, t2])

# print(f"Block 1 data: {block1.block_data}")
# print(f"Block 1 hash: {block1.block_hash}")



# block2 = EggCoinBlock(block1.block_hash, [t3, t4])

# print(f"Block 2 data: {block2.block_data}")
# print(f"Block 2 hash: {block2.block_hash}")


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(EggCoinBlock("5", ['egg Genesis']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_hash = self.last_block.block_hash
        self.chain.append(EggCoinBlock(previous_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]
    
müsteri1=1111
müsteri2=1112
müsteri3=1113
müsteri4=1114

satici1=2001
satici2=2002
satici3=2003
satici4=2004

t1= f"{satici1} {müsteri1}\'ye {500} yumurta gönderdi"
t2= f"{satici2} {müsteri3}\'ye {300} yumurta gönderdi"
t3= f"{satici4} {müsteri2}\'ye {300} yumurta gönderdi"
t4= f"{satici3} {müsteri1}\'ye {350} yumurta gönderdi"
t5= f"{satici2} {müsteri4}\'ye {150} yumurta gönderdi"
t6= f"{satici3} {müsteri3}\'ye {5000} yumurta gönderdi"
t7= f"{satici2} {müsteri2}\'ye {280} yumurta gönderdi"
t8= f"{satici3} {müsteri4}\'ye {330} yumurta gönderdi"
t9= f"{satici1} {müsteri3}\'ye {1000} yumurta gönderdi"
t10= f"{satici1} {müsteri2}\'ye {450} yumurta gönderdi"
t11= f"{satici3} {müsteri1}\'ye {50} yumurta gönderdi"
t12= f"{satici4} {müsteri1}\'ye {1250} yumurta gönderdi"



        



eggBlockChain = Blockchain()

eggBlockChain.create_block_from_transaction([t1, t2])
eggBlockChain.create_block_from_transaction([t3, t4])
eggBlockChain.create_block_from_transaction([t5, t6])
eggBlockChain.create_block_from_transaction([t7, t8])
eggBlockChain.create_block_from_transaction([t9, t10])
eggBlockChain.create_block_from_transaction([t11, t12])



eggBlockChain.display_chain()


































