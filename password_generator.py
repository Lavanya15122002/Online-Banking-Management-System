import random

class Generate:
    letters_seq="abcdefghijklmnopqrstuvwxyz"
    numbers_seq="0123456789"
    symbols_seq="!@#$%^&*(){?/|}"

    # 8 letters 
    # 3 int, 3 num , 2 symbols 
    def generate_password(self,integers=3,numbers=3,symbols=2):
            
        password_letters = [random.choice(self.letters_seq) for _ in range(integers)]
        password_numbers = [random.choice(self.numbers_seq) for _ in range(numbers)]
        password_symbols = [random.choice(self.symbols_seq) for _ in range(symbols)]

        
        password_list = password_letters + password_numbers + password_symbols
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password
gen=Generate()




