from atm import atm 
from atm import get_user

def main(user):

    
    checklist = ['check balance','deposit','withdraw','transactions','stop']
    
    print('Welcome to Louizos Finacial!')
    
    while True:

        check = input('check balance/deposit/withdraw/transactions/stop: ').lower()

        if check not in checklist:
            print('invalid response')

        if check == 'check balance':
            print(f'${user.balance}')

        elif check == 'deposit':
            amount = input('How much will you deposit today: ')
            amount = int(amount)
            user.deposit(amount)

        elif check == 'withdraw':
            amount = input('How much would you like to withdraw: ')
            amount = int(amount)
            user.withdraw(amount)

        elif check == 'transactions':
            user.print_transactions()

        elif check == 'stop':
            user.print_transactions()
            print('Have a nice day!')
            break

        check = input('would you like to make another transaction y/n:')

        if check == 'no' or check == 'stop' or check == 'n':
            user.print_transactions()
            print('Have a nice day!')
            break

def authenticate():  

    check = input('Are you a new or existing user: ').lower()
    
    while True:
        
        if check == 'new' or check == 'existing':
            break
        else:
            print('invalid input')
            check = input('Are you a new or existing user?').lower()
    

    # adding user requires testing but should be good until saving feat added

    if check == 'new':
        
        username = input("what is your name: ")
        
        user = atm(username)
        
        print(f'your account number is {user.account_number}')

        main(user)

        user.save_user()

        #  existing has not been touched start with get_user
    elif check == 'existing':
        
        while True:

            account_number = input('account number: ')

            user = get_user(account_number)
            
            pin = input('pin: ')
            
            if pin == user.pin:
                break
            else:
                print('That is an invalid combination\nplease check your pin and account number.')
        
        main(user)

        user.save_user()

authenticate()