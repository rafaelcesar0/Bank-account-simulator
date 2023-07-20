from datetime import datetime


def input_int(text:str)->int:
    while True:
        try:
            return int(input(text))
        except ValueError as e:
            print("\033[33m"+"⚠️  Enter only numbers  ⚠️"+"\033[0m")
            
def input_floar(text:str)->int:
    while True:
        try:
            return float(input(text))
        except ValueError as e:
            print("\033[33m"+"⚠️  Enter only numbers  ⚠️"+"\033[0m")

def input_date(text_day:str, text_month:str, text_year:str)->str:
    while True:
        day = input_int(text_day)
        if (day>=1 and day<=31): 
            break
        print("\033[33m"+"⚠️  Invalid day  ⚠️"+"\033[0m")
    while True:
        month = input_int(text_month)
        if month>=1 and month<=12:
            break
        print("\033[33m"+"⚠️  Invalid month  ⚠️"+"\033[0m")
    while True:
        year = input_int(text_year)   
        if year>1899 and year<datetime.now().year:
            break
        print("\033[33m"+"⚠️  Invalid year  ⚠️"+"\033[0m")
    return f"{day:02}/{month:02}/{year}" 
                
def input_cpf(text:str)->str:
    while True:
        cpf = input(text)

        cpf=''.join(char for char in cpf if char.isdigit())
        
        if len(cpf) == 11:
            return cpf
        print("\033[33m"+"⚠️  The CPF must have 11 digits  ⚠️"+"\033[0m")

def input_state_initials(text:str)->str:
    STATES = ('AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO')
    while True:
        state = input(text).upper()
        if state in STATES:
            return state
        print("\033[33m"+"⚠️  Invalid state initials  ⚠️"+"\033[0m")
         