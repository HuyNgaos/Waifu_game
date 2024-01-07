import string
from tkinter import messagebox
import sys

class YesNo():
    def TrueFlase(yesno):
        if yesno == "yes":
            return True
        else:
            return False
        
class CleanStr():
    def cleanup(teststr):
       cleaningtable1 = str.maketrans('','',string.punctuation) #remove puctuation
       cleanpuc = teststr.translate(cleaningtable1)
       cleaningtable2 = str.maketrans('','',' ') #remove space
       cleanspc = cleanpuc.translate(cleaningtable2)
       cleanstr = cleanspc.lower() #convert to lowercase
       return cleanstr
    
class admin_log():
    def log(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

class legal():
    def legal_age(wife):
        if wife.age >= 18:
            return True
        else:
            return False
        
class dict_to_str():
    def dict_to_str(dict):
        str = ''
        for key, value in dict.items():
            str += f"{key}: {value}    "
        return str
    
def check_invalid_waifu(usertatse, version_plus, version_now):
    if usertatse not in version_plus:
        print('Invaild')
        messagebox.showerror(title='Invaid Waifu', message=f'''Sorry. This version only support:\n{version_now}''')
        sys.exit()

def invalid_age():
    print('Invaild')
    messagebox.showerror(title='Invaid Age', message=f'''Sorry. Age must be an integer number''')
    sys.exit()

def thankyou():
    print('Thank you for playing')
    messagebox.showinfo(title='Thank you', message=f'''Thank you for playing this game\nCreated by Huy_Ngaos''')
    sys.exit()