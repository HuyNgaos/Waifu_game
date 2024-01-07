import gui, sorting
import tecinical_logic as lg
import random
from tkinter import *

version_now = ["loli", "trap", "malewife", 'bom', 'shouta']
version_plus = version_now + ['test']

def main():
    print("Welcome to Waifu Simulator\nCreated by Huy_Ngaos\nVersion 4.0.0\n\n")
    play_again = 1
    admin_status = False
    root = Tk()
    window1 = gui.Start_up(root, version_now)
    window1.start_wind(root)
    username, usertatse = window1.data()
    lg.check_invalid_waifu(usertatse, version_plus, version_now)
    while (play_again > 0):
        Age = random.randint(5,10)
        window2 = gui.second_wind(root)
        window2.sec_wind(root)
        waifuname, waifupersonality = window2.data2()
        usersorter = sorting.Sort(username, usertatse)
        if play_again == 1:
            user_status = usersorter.namE()
            admin_status = usersorter.check_ad(user_status)
        wife = sorting.waifu_sort(username, usertatse ,Age, waifuname, waifupersonality).tastE(admin_status)
        window3 = gui.third_wind(root, wife)
        window3.trd_wind(root, wife)
        breed_status, Age = window3.data3(admin_status)
        wife.age = Age
        window4 = gui.fourth_wind(root)
        window4.frt_wind(root, wife, admin_status, breed_status)
        window5 = gui.fifth_wind(root)
        window5.fif_wind(root, wife, admin_status)
        play_again = window5.data5(admin_status)
        if play_again:
            window1_ = gui.looped_first(root, version_now)
            window1_.sixth_wind(root)
            usertatse = window1_.data6()
            lg.check_invalid_waifu(usertatse, version_plus, version_now)

    root.destroy()
    lg.thankyou()
    root.mainloop()

if __name__ == "__main__":
    main()