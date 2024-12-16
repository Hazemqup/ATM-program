#here I define the user accounts that i waill have
accounts = {
    "123": { "balance": 500.0, "transactions": [],"type_of_account": "checking" },
 #PIN for the user, the cash insid the sccount, a list to store transaction history, the type of the account.
    "321": {"balance": 10000.0,"transactions": [],"type_of_account": "saving"}
 #PIN for the user, the cash insid the sccount, a list to store transaction history, the type of the account.

}
#this function is job is to authenticate the user has inter a valid PIN
#ask the user to inter his PIN and then verifies to the one stored in accouns
def authenticate():
    pin = input("please enter your PIN number: ")#here is where i ask the user to put the PIN
    if pin in accounts:#here is where the program will take the input and see if it's match the PIN that i stored
        return pin#it will return the authenticated PIN
    else:# here in case the user put a worng PIN
        print("Please try again, the PIN is Invalid.")#here a text will inform the user that the PIN in invalid
        return None #return none if the authentication fails
    


def menu_option(account):
    while True:
        print("\n--- Main Menu Option---")
        print("1. check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. view your transaction history")
        print("5. for Exit")


        choice_opton = input("plese choice a number: ")

        if choice_opton == "1":
            check_balance(account)
        elif choice_opton == "2":
            deposit(account)
        elif choice_opton =="3":
            withdraw(account)
        elif choice_opton =="4":
            transactions_history(account)
        elif choice_opton =="5":
            print("I hope liked my program thanks. goodbye")
            break
        else:
            print("plese choice from 1 to 5, your selection is invalid.")


def main():
    print("Hi and welcome to my lovle program!")
    authenticate_for_user = None

    while not authenticate_for_user: authenticate_for_user = authenticate()

    account = accounts[authenticate_for_user]
    menu_option(account)





#i made this function if the user want to check for his balance
#it will display the current balance from the account 
def check_balance(account):
    print(f"Your current balance is: £{account['balance']:.2f}")
#here i used the string f"" so the pro

def deposit(account):
     try:
        quantity = float(input("How much you want deposit: "))
        if quantity > 0:
            account['balance'] += quantity
            account['transactions'].append(f"Depositedd £{quantity:.2f}")
            print(f"Successfully deposited £{quantity:.2f}")
        else:
            print("Please deposit must be in positive.")
     except ValueError:
        print("Please enter a valid value.")


def withdraw(account):
     try:
         quantity = float(input("How much you want to withdraw from your account: "))
         if quantity > 0:
             if quantity <= account['balance']:
                account['balance'] -= quantity
                account['transactions'].append(f"Withdrew £{quantity:.2f}")
                print(f"Successfully withdrew £{quantity:.2f}")
             else:
                print("you don't have enough money.")
         else:
            print("the amount for withdrawal most positive.")
     except ValueError:
          print("Please enter a valid value.")



def transactions_history(account):
    print("Transaction History:")
    if account['transactions']:
        for transaction in account['transactions']:
            print(transaction)
    else:
        print("theres no transaction yet.")




main()