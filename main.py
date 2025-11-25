import maskpass
from validators import valid
from auth import authen
import os 
from dotenv import load_dotenv
load_dotenv()
from bank import option
from utils import util
from config import con
class Main:
    def main_class(self):
        self.is_login = False 
        flag = True
        hiddencode = 540
        while flag:            
            user_input = int(input("1.register \n2.login \n3.createaccount \n4.operations "))
            if user_input == hiddencode:
                break

            match user_input:
                case 1:
                    username = input("Enter Username: ").lower().strip()
                    password = maskpass.askpass("Enter Password: ")
                    confirm_password = input("Confirm Password")
                #1. validate user 
                    if not valid.validate_user(username=username,password=password,confirm_password=confirm_password):
                        print(f"User Registration:{username}") 
                    else:
                        print("user register Successfull!") 
                case 2:
                    username = input("Enter Username: ").lower().strip()
                    password = maskpass.askpass("Enter Password: ") 
                    if not authen.login(username=username,password=password):
                        print(f"Authentication failed!")
                    
                    else:
                        print("login successfull!")
                        self.is_login=True
                case 3: 
                    print("creating account") # username 
                    username = input("enter username: ").lower().strip()
                    if username in util.load_data(database=con.DATABASE):
                        if username in util.load_data(database=con.BANK):
                            print(f"Account already exists with {username}")
                        print("user is not valid!")

                    acctype = input("Enter your account type saving/current: ").lower().strip()
                    if not option.create_account(username,acctype=acctype):
                        print("Error while creating account")
                    
                    else:
                        print(f"Account Successfully Created for {username}")
                case 4: 
                    print("perform operations..")
                    username = input("Enter your username: ")
                    operations = int(input("1.deposite \n2.withdrawn \n3.checkbalance \n4.transactionhistory"))

                    match operations:
                        case 1:
                            amount = int(input("Enter amount to deposite: "))
                            if not option.deposite(username=username,amount=amount):
                                print("error while deposite..")
                        case 2:
                            amount = int(input("Enter amount to withdraw: "))
                            if not option.withdraw(username=username,amount=amount):
                                print("error while withdraw..")
                        case 3:
                            balance = option.check_balance(username=username)
                            print(f"current balance:{balance}")
                            
                        case 4: 
                            transaction_history = option.transaction(username=username,operation="transaction history")
                            history = {
                                "history" : transaction_history
                            }
                            print(history)
                                
                        case _:
                            print("Invalid Input!")
main=Main()
main.main_class()