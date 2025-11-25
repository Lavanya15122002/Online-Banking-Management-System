import json,os
from dotenv import load_dotenv
load_dotenv()
from config import con
class Utils:
    def load_data(self,database):
        try:
            with open(database,"r") as file:
                data = json.load(file)
                return data
        except Exception as e:
            print(e)

    def dump_data(self,user_data,database):
        try:
            data = self.load_data(database)
            if not data:
                data={}
            data.update(user_data)
            with open(database,"w") as file:
                json.dump(data,file,indent=4)
            
        except Exception as e:
            print(e)
util=Utils()