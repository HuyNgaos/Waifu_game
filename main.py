import interface, user, sorting, cpu
import random
import sys


version_now = ["loli", "trap", "malewife", 'bom', 'shouta', 'test']


def main():
    print("Welcome to Waifu Simulator\nCreated by Huy_Ngaos\nVersion 3.8.0\n\n")
    Age = random.randint(5,10)
    sys.stdin = sys.__stdin__
    Username =input("What is your name? ")
    playing = "y"
    while (playing == "y"):
        preference = input("Tell us your taste: ")
        preference = interface.Interface.cleanup(preference)
        User = user.USER(Username, preference)
        if preference in version_now:
            name = input(f'Give your {preference} a name: ')
            personality = input(f"Tell us your {preference} personality: ")
            personality = interface.Interface.cleanup(personality)
            wife = sorting.Sort.give_de_wife(Age, name, personality, User)
            cpu.Final_interact.interact(wife, User)
        else:
            print('Sorry only loli, trap, malewife, Big Old Man (BOM), shouta is avalable now.')
        playing = input("Would you like to play again? y for yes\n")
    print("\nOk. Gameover then.\nYou can close now")

if __name__ == "__main__":
    main()