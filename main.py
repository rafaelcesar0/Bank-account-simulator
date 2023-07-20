from os import path, system, name
import json

from time import sleep
from datetime import datetime

from user_object import User
from inputs import input_int,input_floar, input_date, input_cpf, input_state_initials


# Pasta e arquivos
FILE_JSON = 'database.json'
WITHDRAWAL_VALUE_LIMIT = 500.00
list_users = []
online_user = None


def download_data(file_json:str)->None:
    """Check if the database exists if not create the database"""
    global list_users
    # Verifica se o arquivo database.json existe
    if  path.isfile(FILE_JSON):
        
        with open(FILE_JSON, 'r') as f:
            data = json.load(f)
            for registry in data:
                nome = registry['name']
                cpf = registry['cpf']
                date_birth = registry['date_birth']
                road = registry['road']
                num_house = registry['num_house']
                neighborhood = registry['neighborhood']
                city = registry['city']
                state = registry['state']
                account = registry['account']
                list_users.append(User(nome, cpf, date_birth, road, num_house, neighborhood, city, state, account))

def login_user()->User|None:
    name = input("Name: ").title()
    cpf = input_cpf("CPF: ")
    for user in list_users:
        if user.name == name and user.cpf == cpf:
            return user
    return None
         
def new_user()->User:
    name = input("Name: ")
    cpf = input_cpf("CPF: ")
    birth = input_date("The day of your birthday: ",
                       "The month of your birthday: ",
                       "The year of your birthday: ")
    road = input("Road: ")
    num_house = input_int("Nº house: ")
    neighborhood = input("Neighborhood: ")
    city = input("City: ")
    state = input_state_initials("States initials: ")
    
    return User(name, cpf, birth, road, num_house, neighborhood, city, state)
                      
def menu1()->None:
    global list_users
    global online_user
    menu = """ 
=============== MENU ===============
[1]\tLogin user
[2]\tNew user
[0]\tExit

>>> """
    match input(menu):
        case "1":
            online_user = login_user()
            if online_user is None:
                print("\033[33m"+"⚠️  User not found  ⚠️"+"\033[0m")
                sleep(1.5)
        case "2":
            list_users.append(new_user())
            online_user = list_users[-1]
        case "0":
            list_users_online = [user.__dict__ for user in list_users]
            with open('database.json', 'w') as f:
                json.dump(list_users_online, f, indent=4)
            exit()
        case _:
            print("\033[33m"+"⚠️  Invalid option.  ⚠️"+"\033[0m")
            sleep(1.5)

def menu2()->None:
    global online_user
    global count_withdrawals
            
    menu = f"""
Username: {online_user.name}          CPF: {online_user.cpf[:5]}...
Agency: {online_user.agency}          Account: {online_user.connected_account}

=============== MENU ===============
[1]\tDeposit
[2]\tTo withdraw
[3]\tExtract
[4]\tNew account
[5]\tChange account
[0]\tLogout

>>> """
    match input(menu):
        case "1":
            online_user.deposit(input_floar("Amount to deposit: "))
        case "2":
            withdrawal=input_floar("Amount to withdraw: ")
            if withdrawal <= WITHDRAWAL_VALUE_LIMIT:
                if online_user.to_withdraw(withdrawal) != None:
                    print("\033[32m"+f"✅ Withdrawal successful ✅"+"\033[0m")
                    sleep(1)
            else:
                print("\033[33m"+f"⚠️  You cannot withdraw more than {WITHDRAWAL_VALUE_LIMIT} dollars  ⚠️"+"\033[0m")
                sleep(2)
        case "3":
            print(online_user.extract())
            system('pause' if name == 'nt' else 'read')
        case "4":
            online_user.new_account()
            sleep(1.5)
        case "5":
            online_user.change_account()
        case "0":
            online_user = None
        case _:
            print('Opção inválida.')
            
def main()->None:
    download_data(FILE_JSON)
    while True:
        system('cls' if name == 'nt' else 'clear')
        menu1()
        while True:
            if online_user is None:
                break
            system('cls' if name == 'nt' else 'clear')
            menu2()
    
            
main()