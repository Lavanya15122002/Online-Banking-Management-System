from config import con
from utils import util
from datetime import datetime

# util.dump_data()
# util.load_data()

def generate_accountNo():
    for i in range(1000,1011):
        yield i 

gen = generate_accountNo()
class Create:
    def create_account(self,username,acctype):
        try:
            account_details = {
                username:{
                    'account no': f"ACCNO{next(gen)}",
                    'acctype':acctype,
                    'is_active':True,
                    'balance':0,
                    'transactions':[]
                }
            }
            if util.dump_data(database=con.BANK,user_data=account_details):
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False
class Option(Create):
# deposite
    def deposite(self,username,amount:int):
        try:
            data = util.load_data(database=con.BANK)
            transaction_history = self.transaction(username=username,operation="deposite",amount=amount)
            if not data[username]:
                print(f"No account found with {username}")
                return False
            else:
                current_balance = data[username]['balance']
                data[username]['balance'] = current_balance + amount 
                data[username]['transactions'] = transaction_history
                util.dump_data(database=con.BANK,user_data=data)
                return True
        except Exception as e:
            print(e)

    # check balance 
    def check_balance(self,username):
        try:
            data = util.load_data(database=con.BANK)
            if not data[username]:
                return False
            balance = data[username]['balance']
            return balance
        except Exception as e:
            print(e)

    # withdraw amount
    def withdraw(self,username,amount:int):
        try:
            data = util.load_data(database=con.BANK)
            transaction_history = self.transaction(username=username,operation="withdrawn",amount=amount)
            if not data[username]:
                return False
            current_balance = data[username]['balance']
            if amount > current_balance:
                print(f"Insufficient balance \n balance:{current_balance} asked for:{amount}")
                return False
            remaining_balance = current_balance - amount
            data[username]['balance'] = remaining_balance
            data[username]['transactions'] = transaction_history
            util.dump_data(database=con.BANK,user_data=data)
            return True
        except Exception as e:
            print(e)

    # Transaction history 
    def transaction(self,username,operation,amount=None):
        data = util.load_data(database=con.BANK)
        transactions = data[username]['transactions']
        if amount is not None:
            format = f"{operation} : Rs{amount}-{datetime.now()}"
            transactions.append(format)
            return transactions
        else:
            return transactions
option=Option()