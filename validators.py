from auth import authen
from password_generator import gen
# authen.register()
# authen.login()
# gen.generate_password()

class Valid:
    def validate_password(self,password):
        return len(password) >= 8
            
    def check_password(self,password,confirm_password):
        return password == confirm_password
# valid=Valid()   


class Validate(Valid):
    def validate_user(self,username,password,confirm_password):
        if self.check_password(password,confirm_password):
            if self.validate_password(password=password):
                # register the user 
                authen.register(username,password)
            else:
                print("length of password should be atleast 8 digits?")
                password_generate=input("Wants to generate password? yes/no").lower().strip()
                if password_generate == "yes":
                    password = gen.generate_password()
                    # register the user 
                    # print(pswd)
                    authen.register(username,password)
        else:
            print("Password and Confirm Password does'nt match!")
valid=Validate()
