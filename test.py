

# dict = {'key':'value'}

# dict['new'] = {"new":"newvalue"}

# # print(dict)

# # Database.json
# {"aim": {"aim": "433!fe(q"}, "lavanya": {"lavanya": "}j7t&51d"}}

# # task-1
# {
#     "username":{
#         "username":"lavanay",
#         "password":"password"

#     }
# }



# {
#   'username':{
#       'account no ':123,
#       'acctype': 'saving/current',
#       'is_active': 'True/False',
#       'balance':4566,
#       'transactions':[]
#   }
# }


# """
# 1. creating the account is user is logged in 

# """
# # simple yield genertor functions
# def generate_accountNo():
#     for i in range(1000,1011):
#         yield i 

# gen = generate_accountNo()

# username = input("enter your username")
# acctype = input("Enter your account type saving/current").lower().strip()
# balance = 0 
# transactions = []# deposite, withdrawn , check balance 

# account = {
#     username:{
#         'account no': f"ACCNO{next(gen)}",
#         'acctype':acctype,
#         'is_active':True,
#         'balance':0,
#         'transactions':[]

#     }
# }
import json 
from dotenv import load_dotenv
load_dotenv()
import os 
from config import DATABASE

def load_data(database):
    try:
        with open(database,"r") as file:
            data=json.load(file)
            return data
    except Exception as e:
        print(e)


def dump_data(user_data,database):
    try:
        data = load_data(database)
        if not data:
            {}
        data.update(user_data)
        with open(database,"w") as file:
            print(data)
            json.dump(data,file,indent=4)
        
    except Exception as e:
        print(e)
username="lav"
pswd=123
user_data = {username:{username:pswd}}
dump_data(user_data,database=DATABASE)