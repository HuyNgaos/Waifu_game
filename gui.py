from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tecinical_logic as lg
import interaction as inter
import pygame
import sorting
import cpu
import sys

user_ = {'name': '', 'tatse': ''}
waifu_ = {'wname': '', 'wpersonality': ''}
ending = {}

class root_window():
    def __init__(self, master):
        master.title('Waifu Game')
        master.configure(background = '#c3e7f3')
        master.geometry('770x557+375+129')
        pygame.init()
        pygame.mixer.init()

        self.background_music = pygame.mixer.Sound('sounds/background/background1.mp3')
        self.style = ttk.Style()
        self.style.configure('startHeader.TLabel', font = ('Arial', 31, 'bold'))
        self.style.configure('Header.TLabel', font = ('Arial', 25))
        self.style.configure('Endin.TLabel', font = ('Arial', 13, 'bold'))
        self.ok_button = ttk.Button(master, text = 'OK')
        self.button_pressed = StringVar() #create a variable to check if the button is pressed
        self.ending = {}
    def play_bgm(self):
        self.background_music.play(-1)
        self.background_music.set_volume(0.5)
#------------------------------------------------------------
#the Fist window
class Start_up(root_window):
    def __init__(self, master, version_now):
        super().__init__(master)
        self.header = ttk.Label(master, text= 'Da Waifu game by Huy_Ngaos', style= 'startHeader.TLabel')
        self.name_frame = ttk.Frame(master)
        self.tatse_frame = ttk.Frame(master)
        self.name_entry = ttk.Entry(self.name_frame, width = 24, font = ('Arial', 10))
        self.name_label = ttk.Label(self.name_frame, text = 'Name:')
        self.taste_label = ttk.Label(self.tatse_frame, text = 'Taste:')
        self.tatse_holer = StringVar()
        self.taste_entry = ttk.Combobox(self.tatse_frame, width = 24, font = ('Arial', 10), 
                                        textvariable=self.tatse_holer, values=version_now)
    def name_display(self):
        self.name_label.pack()
        self.name_entry.insert(0, 'Please enter your name')
        self.name_entry.pack()
    def taste_display(self):
        self.taste_label.pack()
        self.taste_entry.set('Please select your taste')
        self.taste_entry.pack()
    def start_wind(self, master):
        self.play_bgm()
        self.header.pack()
        self.name_display()
        self.taste_display()
        self.name_frame.pack()
        self.tatse_frame.pack()
        self.ok_button.config(command = self.ok_butt)
        self.ok_button.pack()
        master.wait_variable(self.button_pressed)  #wait for the button to be pressed  
    def ok_butt(self):
        self.name_frame.pack_forget()
        self.tatse_frame.pack_forget()
        self.header.destroy()
        self.ok_button.pack_forget()
        global user_
        user_['name'] = lg.CleanStr.cleanup(self.name_entry.get())
        user_['tatse'] = lg.CleanStr.cleanup(self.tatse_holer.get())
        self.button_pressed.set('ok') #set the button_pressed to ok
    def data(self): #return user_ to main.py
        global user_
        return user_['name'], user_['tatse']
#------------------------------------------------------------
#the second window
class second_wind(root_window):
    def __init__(self, master):
        super().__init__(master)
        self.header = ttk.Label(master, text= 'Create your WAIFU', style= 'Header.TLabel')
        self.wname_frame = ttk.Frame(master)
        self.wpersonality_frame = ttk.Frame(master)
        self.wname_entry = ttk.Entry(self.wname_frame, width = 24, font = ('Arial', 10))
        self.wname_label = ttk.Label(self.wname_frame, text = 'Name your Waifu:')
        self.wpersonality_label = ttk.Label(self.wpersonality_frame, text = "What is yout Waifu's personality:")
        self.wpersonality_entry = ttk.Entry(self.wpersonality_frame, width = 24, font = ('Arial', 10))
        self.uwu_pic = PhotoImage(file = 'pictures/uwu.gif')
        self.uwu_display = ttk.Label(master, image = self.uwu_pic)
    def wname_display(self):
        self.wname_label.pack()
        self.wname_entry.insert(0, 'Enter your Waifu name')
        self.wname_entry.pack()
    def wpersonality_display(self):
        self.wpersonality_label.pack()
        self.wpersonality_entry.insert(0, 'Enter your Waifu personality')
        self.wpersonality_entry.pack()
    def sec_wind(self, master):
        self.header.pack()
        self.wname_display()
        self.wpersonality_display()
        self.wname_frame.pack()
        self.wpersonality_frame.pack()
        self.ok_button.config(command = self.ok_butt2)
        self.ok_button.pack()
        self.uwu_display.pack()
        master.wait_variable(self.button_pressed)
    def ok_butt2(self):
        self.wname_frame.pack_forget()
        self.wpersonality_frame.pack_forget()
        self.header.destroy()
        self.ok_button.pack_forget()
        self.uwu_display.destroy()
        global waifu_
        waifu_['wname'] = lg.CleanStr.cleanup(self.wname_entry.get())
        waifu_['wpersonality'] = lg.CleanStr.cleanup(self.wpersonality_entry.get())
        self.button_pressed.set('ok2')
    def data2(self):
        global waifu_
        return waifu_['wname'], waifu_['wpersonality']
#------------------------------------------------------------
#the third window
class third_wind(root_window):
    def __init__(self, master, wife):
        super().__init__(master)
        self.header = ttk.Label(master, text= 'Waifu UwU', style= 'Header.TLabel')
        self.waifu_info_frame = ttk.Frame(master)
        self.waifu_info_label = ttk.Label(self.waifu_info_frame, text = f'{wife.name} info:')
        self.waifu_info = Text(self.waifu_info_frame, width = 88, height = 13)
        self.ask_breed_frame = ttk.Frame(master)
        self.ask_breed_label = ttk.Label(self.ask_breed_frame, text = f'Do you want to breed your {wife.type}?')
        self.breed_desire = BooleanVar()
        self.yes_button = ttk.Checkbutton(self.ask_breed_frame, text = 'BREED?', variable=self.breed_desire, onvalue=True, offvalue=False)
        self.func_proto = f'inter.{wife.type}.'
        self.age_mod_frame = ttk.Frame(master)
        self.age_var = IntVar()
        self.age_mod_label = ttk.Label(self.age_mod_frame, text = f'You have the power to change your {wife.name} age:')
        self.age_entry = Spinbox(self.age_mod_frame, from_ = 0, to = 100, width = 13, textvariable = self.age_var)
    def waifu_info_display(self, wife):
        self.waifu_info_label.pack()
        info_func = self.func_proto + f'info_{wife.type}(wife)'
        info = eval(info_func)
        self.waifu_info.insert(1.0, info)
        self.waifu_info.config(state = 'disabled')
        self.waifu_info.pack()
    def ask_breed_display(self):
        self.ask_breed_label.pack()
        self.yes_button.pack()
    def age_mod_display(self, wife):
        self.age_mod_label.pack()
        self.age_var.set(wife.age)
        self.age_entry.pack()
    def trd_wind(self, master, wife):
        self.header.pack()
        self.waifu_info_display(wife)
        self.ask_breed_display()
        self.age_mod_display(wife)
        self.waifu_info_frame.pack()
        self.age_mod_frame.pack()
        self.ask_breed_frame.pack()
        self.ok_button.config(command = self.ok_butt3)
        self.ok_button.pack()
        master.wait_variable(self.button_pressed)
    def ok_butt3(self):
        self.waifu_info_frame.pack_forget()
        self.ask_breed_frame.pack_forget()
        self.age_mod_frame.pack_forget()
        self.header.destroy()
        self.ok_button.pack_forget()
        self.button_pressed.set('ok3')
    def data3(self, admin):
        try:
            age = self.age_var.get()
        except:
            lg.invalid_age()
        if admin:
            lg.admin_log.log(breed_desire = self.breed_desire.get(), age = self.age_var.get())
        return self.breed_desire.get(), age
#------------------------------------------------------------
#the fourth window
class fourth_wind(root_window):
    def __init__(self, master):
        super().__init__(master)
        self.header = ttk.Label(master, text= 'BREED ( ͡° ͜ʖ ͡°)', style= 'Header.TLabel')
        self.img_frame = ttk.Frame(master)
        self.img_label = ttk.Label(self.img_frame)
        self.talk_frame = ttk.Frame(master)
        self.talk_text = Text(self.talk_frame, width = 88, height = 10)
        self.button_frame = ttk.Frame(master)
        self.yes_button = ttk.Button(self.button_frame, text = 'Yes')
        self.no_button = ttk.Button(self.button_frame, text = 'No')
        self.vanila = False
        self.narrator = 'Narrator: NONE'
        self.talk = 'Waifu: NONE'
        self.force_loop = False
        self.bonk_sound = pygame.mixer.Sound('sounds/bonk.mp3')
    def img_display(self, wife, admin):
        path_ = sorting.img_file.img_file(wife)
        img = PhotoImage(file = path_)
        self.img_label.config(image = img)
        self.img_label.image = img
        self.img_label.pack()
        if admin:
            lg.admin_log.log(path_ = path_)
    def talk_display(self, wife, breed_status, admin):
        global ending
        self.talk, self.vanila, self.narrator, ending = cpu.breeding_waifu.interact_breed(wife, breed_status, admin, self.bonk_sound)
        self.talk_text.insert('1.0', self.narrator)
        self.talk_text.insert('1.end', f'\n{self.talk}')
        self.talk_text.config(state = 'disabled')
        self.talk_text.pack()
        if admin:
            lg.admin_log.log(talk = self.talk, vanila = self.vanila)
    def button_display(self, wife, breed_status, admin):
        self.yes_button.config(command = lambda: self.yes_butt(wife, breed_status, admin))
        self.no_button.config(command = lambda: self.no_butt(wife, admin))
        if self.vanila:
            self.yes_button.config(state = 'disabled')
            self.no_button.config(text= 'Next')
            self.no_button.config(command = self.next_butt)
        self.yes_button.pack(side = LEFT)
        self.no_button.pack(side = RIGHT)
    def frt_wind(self, master, wife, admin, breed_status):
        self.header.pack()
        self.img_display(wife, admin)
        self.talk_display(wife, breed_status, admin)
        self.button_display(wife, breed_status, admin)
        self.img_frame.pack()
        self.talk_frame.pack()
        self.button_frame.pack()
        master.wait_variable(self.button_pressed)
    def yes_butt(self, wife, breed_status, admin):
        self.talk, v, self.narrator, e = cpu.breeding_waifu.interact_breed(wife, breed_status, admin, self.bonk_sound)
        self.talk_text.config(state = 'normal')
        self.talk_text.insert('1.0', f"{self.talk}\n")
        self.talk_text.config(state = 'disabled')
    def next_butt(self):
        self.header.destroy()
        self.img_frame.pack_forget()
        self.talk_frame.pack_forget()
        self.button_frame.pack_forget()
        self.button_pressed.set('ok4')
    def no_butt(self, wife, admin):
        result, self.force_loop = cpu.breeding_waifu.interact_result(wife, admin)
        self.talk_text.config(state = 'normal')
        self.talk_text.insert('1.0', f"{result}\n")
        self.talk_text.config(state = 'disabled')
        self.yes_button.config(state = 'disabled')
        self.no_button.config(text= 'Next')
        self.no_button.config(command = self.next_butt)
#------------------------------------------------------------
#the fifth window
class fifth_wind(root_window):
    def __init__(self, master):
        super().__init__(master)
        self.header = ttk.Label(master, text= 'GameOver', style= 'Header.TLabel')
        self.ending_frame = ttk.Frame(master)
        self.img_label = ttk.Label(self.ending_frame)
        self.ending_label = ttk.Label(self.ending_frame)
        self.play_again_frame = ttk.Frame(master)
        self.play_again_label = ttk.Label(self.play_again_frame, text = 'Do you want to play again?')
        self.again_yes_button = ttk.Button(self.play_again_frame, text = 'Yes')
        self.again_no_button = ttk.Button(self.play_again_frame, text = 'No')
        self.play_again_choice = 1
    def ending_display(self, wife, admin):
        ending_ = lg.dict_to_str.dict_to_str(ending)
        if admin:
            lg.admin_log.log(ending_ = ending_)
        self.ending_label.config(text = ending_, style = 'Endin.TLabel')
        path_ = sorting.ending_pic_file.end_file(wife)
        img = PhotoImage(file = path_)
        self.img_label.config(image = img)
        self.img_label.image = img
        self.img_label.pack()
        self.ending_label.pack()
    def play_again_display(self):
        self.play_again_label.pack()
        self.again_yes_button.pack(side = LEFT)
        self.again_no_button.pack(side = RIGHT)
    def fif_wind(self, master, wife, admin):
        self.header.pack()
        self.ending_display(wife, admin)
        self.play_again_display()
        self.ending_frame.pack()
        self.play_again_frame.pack()
        self.again_yes_button.config(command = self.again_yes_butt)
        self.again_no_button.config(command = self.again_no_butt)
        master.wait_variable(self.button_pressed)
    def unpack(self):
        self.header.destroy()
        self.ending_frame.pack_forget()
        self.play_again_frame.pack_forget()
        self.button_pressed.set('ok5')
    def again_yes_butt(self):
        self.unpack()
        self.play_again_choice = 2
    def again_no_butt(self):
        self.unpack()
        self.play_again_choice = 0
    def data5(self, admin):
        if admin:
            lg.admin_log.log(play_again = self.play_again_choice)
        return self.play_again_choice
#------------------------------------------------------------
#the sixth window
class looped_first(Start_up):
    def __init__(self, master, version_now):
        super().__init__(master, version_now)
        self.header = ttk.Label(master, text= 'The Next Round', style= 'Header.TLabel')
    def sixth_wind(self, master):
        self.header.pack()
        self.taste_display()
        self.tatse_frame.pack()
        self.ok_button.config(command = self.ok_butt6)
        self.ok_button.pack()
        master.wait_variable(self.button_pressed)
    def ok_butt6(self):
        self.tatse_frame.pack_forget()
        self.header.destroy()
        self.ok_button.pack_forget()
        global user_
        user_['tatse'] = lg.CleanStr.cleanup(self.tatse_holer.get())
        self.button_pressed.set('ok6')
    def data6(self):
        global user_
        return user_['tatse']