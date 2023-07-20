import json
from datetime import datetime
from time import sleep

# from inputs import input_int

class User:
    def __init__(self, name:str,
                 cpf:str,
                 date_birth:str,
                 road:str,
                 num_house:int,
                 neighborhood:str,
                 city:str,
                 state:str,
                 account:dict= {
                     '1': {
                        'extract': [],
                        'balance': [
                            {'value': 0,'date': datetime.now().strftime("%d/%m/%Y")}
                        ]
                    }
                 }):
        self.name = name.title()
        self.cpf = cpf
        self.date_birth = date_birth
        self.road = road.title()
        self.num_house = num_house
        self.neighborhood = neighborhood.title()
        self.city = city.title()
        self.state = state.upper()
        self.agency = '0001'
        self.account = account
        self.connected_account = "1"
        
    def change_account(self)->str:
        print("Number of accounts:", len(self.account))
        accont_number = input("Account number: ")
        if accont_number in list(self.account.keys()):
            self.connected_account = accont_number
            return self.connected_account
        print("\033[33m"+"⚠️  This account does not exist  ⚠️"+"\033[0m")
    
    def new_account(self)->str|None:
        if len(self.account)>=5:
            print("\033[33m"+"⚠️  This account is full  ⚠️"+"\033[0m")
            return None
        self.account[str(len(self.account)+1)] = {
                        'extract': [],
                        'balance': [
                            {'value': 0,'date': datetime.now().strftime("%d/%m/%Y")}
                        ]
                    }
        self.connected_account = str(len(self.account))
        print("✅ New account created. ✅")
        return self.connected_account
                
    def to_withdraw(self, withdrawal_value:float)->None:
        withdrawal_value = abs(round(withdrawal_value,2))
        if withdrawal_value == 0:
            print("\033[33m"+"⚠️  You cannot withdraw 0 dollars  ⚠️"+"\033[0m")
            sleep(1.5)
            return None
        if withdrawal_value <= self.account[self.connected_account]['balance'][-1]['value']:
            self.account[self.connected_account]['extract'].append({'value':-withdrawal_value, 'date': datetime.now().strftime("%d/%m/%Y")})
            
            self.account[self.connected_account]['balance'].append({'value': self.account[self.connected_account]['balance'][-1]['value']-withdrawal_value, 'date': datetime.now().strftime("%d/%m/%Y")})
            
            return self.account[self.connected_account]['balance'][-1]
        print("\033[33m"+"⚠️  Insufficient balance  ⚠️"+"\033[0m")
        sleep(1.5)
                                           
    def deposit(self, deposit_value:float)->None:
        if deposit_value == 0:
            print("\033[33m"+"⚠️  you cannot deposit zero dollars  ⚠️"+"\033[0m")
            sleep(1.5)
            return None
        deposit_value = abs(round(deposit_value,2))
        
        self.account[self.connected_account]['extract'].append({'value': +deposit_value, 'date': datetime.now().strftime("%d/%m/%Y")})
        
        self.account[self.connected_account]['balance'].append({'value': self.account[self.connected_account]['balance'][-1]['value']+deposit_value, 'date': datetime.now().strftime("%d/%m/%Y")})
        print("\033[32m"+f"✅ Deposit successful ✅"+"\033[0m")
        sleep(1)
        return self.account[self.connected_account]['balance'][-1]
    
    def extract(self)->str:
        
        def text_colored(text, color):
            colors = {
                "red": "\033[31m",
                "green": "\033[32m",
                "yellow": "\033[33m"
            }
            reset = "\033[0m"
            return f"{colors[color]}{text}{reset}"
        
        extract_str = f" Agency: {self.agency}\tUsername: {self.name}\nAccount: {self.connected_account}\tCPF: {self.cpf[:5]}...\n=============== EXTRATO ===============\n"

        for entry in self.account[self.connected_account]['extract']:
            value = entry['value']
            date = entry['date']
            color = "green" if value >= 0 else "red"
            
            line = f"US$:+{value:.2f}".ljust(29,'_')+date if value >= 0 else f"US$:{value:.2f}".ljust(29,'_')+date
            
            extract_str += text_colored(line, color)+"\n"
        
        extract_str += 39*'_'+f"\nSALDO R$: {self.account[self.connected_account]['balance'][-1]['value']:.2f}".ljust(30, '_')+self.account[self.connected_account]['balance'][-1]['date']
        
        return extract_str
