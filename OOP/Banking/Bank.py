class Bank:
    accounts = {}

    def __repr__(self):
        return str(Bank.accounts) 
    
print(Bank.accounts)