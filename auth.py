from utils import util
from config import con

# util.load_data()
# util.dump_data()
class Auth: 
    def register(self,username,password):
        try:
            data = util.load_data(database=con.DATABASE)
            if username in data:
                print(f"User with {username} already exists!")
            else:
                user_data = {username:{username:password}}
                util.dump_data(user_data,database=con.DATABASE)
                print("User Register Successfully!")
        
        except Exception as e:
            print(e)      
    # login 
    # creds should match in db

    
    def login(self,username,password):
        db = util.load_data(database=con.DATABASE)

        if db[username]:
            return password == db[username][username]
        else:
            print(f"No user found with: {username}")
            return False 
authen=Auth()