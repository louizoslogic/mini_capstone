import pickle
from datetime import datetime

class atm:

    def __init__(self, user):
        self.transaction = ''
        self.user = user
        self.balance = 0
        self.pin = input('Create a 4 digit pin: ')
        with open('user_data.txt', 'r') as file:
            account_number = file.read()
            account_number = int(account_number)
            account_number = account_number + 1
            account_number = str(account_number)
            self.account_number = account_number

        with open('user_data.txt', 'w') as file:
            file.write(self.account_number)

    def deposit(self, amount):

        self.balance = self.balance + amount
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M")
        newtransaction = f'{dt_string}: {self.user} deposited ${amount}: Total ${self.balance}'
        self.transaction = self.transaction + newtransaction + '\n'
        return newtransaction
    
    def check_withdraw(self, amount):

        if self.balance - amount < 0:
            print("Invalid amount\nYou're broke")
        
        else:
            return True

    def withdraw(self, amount):

        if self.check_withdraw(amount) ==  True:
            self.balance = self.balance - amount
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M")
            newtransaction = f'{dt_string}: {self.user} withdrew ${amount}: Total ${self.balance}'
            self.transaction = self.transaction + newtransaction + '\n'
            newtransaction
    
    def print_transactions(self):
    
        print(self.transaction)
    
    def save_user(self):

        with open(self.account_number + '.txt', 'wb') as file:
            pickle.dump(self, file, pickle.HIGHEST_PROTOCOL)

def get_user(account_number):

    account_number = str(account_number)
    user = None

    with open(account_number + '.txt', 'rb') as file:
        user = pickle.load(file)  
    return user  
