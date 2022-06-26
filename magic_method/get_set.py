class BankRecord:
    def __init__(self,name) -> None:
        self.record = {
            "name":name,
            "balance":100,
            "transactions":[100]
        }
    
    def __getitem__(self,key):
        return self.record[key]
    
    def __setitem__(self,key,newvalue):
        if key=="balance" and newvalue != None and newvalue >= 100:
            self.record[key] += newvalue
        elif key == "transactions" and newvalue != None:
            self.record[key].append(newvalue)

    def get_balance(self):
        return self.__getitem__("balance")
    
    def update_balance(self,new_balance):
        self.__setitem__("balance",new_balance)
        self.__setitem__("transactions",new_balance)
    
    def get_transaction(self):
        return self.__getitem__("transactions")
    
    def num_of_transaction(self):
        return len(self.record["transactions"])


sam = BankRecord("Sam")
print("The balance is : "+str(sam.get_balance()))
  
sam.update_balance(200)
print("The new balance is : "+str(sam.get_balance()))
print("The no. of transactions are: "+str(sam.num_of_transaction()))
  
sam.update_balance(300)
print("The new balance is : "+str(sam.get_balance()))
print("The no. of transactions are: "+str(sam.num_of_transaction()))
print("The transaction history is: "+ str(sam.get_transaction()))