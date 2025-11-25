import os 
from dotenv import load_dotenv
load_dotenv()
class Data:
    def __init__(self):
        self.DATABASE = os.environ.get("DATABASE","database.json")
        self.BANK = os.environ.get("BANK","accounts.json")
con=Data()