import interface, tecinical_logic
import user
import sorting, libary_of_quiz
#--------------------------------------------------------------#
class waifu_interaction():
    def breed(wife):
        print(f"{wife.name}: \"ahhhh!!!, ahh!!!\"")
    def brutal_breed(wife):
        brutal = True
        while (brutal):
            print(f"{wife.name}: \"AHHHHH!!!, AHHH!!!\"")
            Continue = input('Do you like to stop? (No to continue):')
            Continue = interface.Interface.cleanup(Continue)
            if Continue == 'no':
                brutal = True
            else:
                brutal = False
    def breed_til_kho(wife, hiep):
        Continue = True
        Bred = 1
        waifu_interaction.breed(wife)
        while (Continue):
            Breed = input("Would you like to breed more? ")
            Breed = interface.Interface.cleanup(Breed)
            if Breed == "yes":
                waifu_interaction.breed(wife)
                Bred += 1
            elif (Breed != 'yes') and (Bred < hiep):
                print(f"No. You can't escape, you haven't complete all of {hiep} rounds yet")
            else:
                Continue = False
                print('Ok good job')
    def setage(wife, age):
        wife.age = age
        if age >= 18:
            wife.breedable = True
        else:
            wife.breedable = False
    def smash_or_pass(wife):
        breed = input(f'You you like to breed your {wife.type} (Yes/No):')
        breed = interface.Interface.cleanup(breed)
        breed = tecinical_logic.YesNo.TrueFlase(breed)
        return breed
#--------------------------------------------------------------#
class Loli(waifu_interaction):
    def info_loli(wife):
        print(f"Here is your {wife.name} status\n{wife.name}-chan age: {wife.age}\n{wife.name}-chan personality: {wife.personality}\n{wife.name}-chan breedable status: {wife.breedable}")
    def godpow(wife):
        try:
            Age2 = int(input("Use your godly power to change age to: "))
            Loli.setage(wife, Age2)
            print( f"{wife.name}-chan age:" , wife.age)
            print( f"Here is your {wife.name}-chan breedable status: ", wife.breedable)
        except:
            print(f"You stupid, {wife.name}\'s age can only be an interger")
    def breed_loli(wife):
        Breed = Loli.smash_or_pass(wife)
        if (Breed):
            Loli.breed(wife)
        else:
            print('Ok')
    def correction(wife):
            correct = input("Would you like to correct that brat? ")
            correct = interface.Interface.cleanup(correct)
            if correct == "yes":
                Loli.brutal_breed(wife)
                print(f"You clean up your self after bang the {wife.personality} brat\nand see far away the FBI squad is approaching you.\nYou are going to spend the rest of your life in jail.")
            else:
                print("Good choice (unload gun)")
#--------------------------------------------------------------#
class Trap(waifu_interaction):
    def trap_info(wife):
        print(f"You have good taste.\nHere is your boy status:\nGender: {wife.gender}\nCuteness level: {wife.cuteness}\nBreedable status: {wife.breedable}")
    def breed_trap(wife):
        print('Sometime, it takes the real man to become the best girl')
        Breed = Trap.smash_or_pass(wife)
        if (Breed):
            Trap.breed(wife)
            print(':))')
        else:
            print('ok')
#--------------------------------------------------------------#
class Malewife(waifu_interaction):
    def info_malewife(wife):
        print(f"You have good taste.\nHere is your boy status:\nGender: {wife.gender} \nBreedable status: {wife.breedable}")
    def breed_malewife(wife):
        print('Sometime, it takes the real man to become the best wife')
        Breed = Malewife.smash_or_pass(wife)
        if (Breed):
            Malewife.breed(wife)
            print('Lmao lol')
        else:
            print('ok')
#--------------------------------------------------------------#
class ttm(Malewife):
    def info_ttm():
        print("Congratuation! You find out Tran Tuan Minh ester egg!!")
    def breed_ttm(wife):
        breed = input('You you like to breed your Tran Tuan Minh (Yes/No):')
        breed = interface.Interface.cleanup(breed)
        if breed == 'yes':
            ttm.breed_til_kho(wife, 10)
            print('You are exhaust but you have a good time')
        else:
            print("Tran Tuan Minh is way too hot. You lost control and breed anyway")
            ttm.breed_til_kho(wife, 13)
            print('You dried your balls and now is decending to heaven')
#--------------------------------------------------------------#
class BOM(waifu_interaction):
    def info_bom(wife):
        print(f"Here is your {wife.name}-san status\n{wife.name}-san age: {wife.age}\n{wife.name}-san personality: {wife.personality}\n{wife.name}-san breedable status: {wife.breedable}")
    def breed_bom(wife):
        Breed = BOM.smash_or_pass(wife)
        if (Breed):
            BOM.breed(wife)
        else:
            print(f'Ok. Poor the big old man, he got rejected at such an old age of {wife.age}')
#--------------------------------------------------------------#
class pnm(BOM):
    def pmn_info():
        print("Congratuation! You find out Pham Nhat Minh ester egg!!")
    def breed_pnm(wife):
        breed = input('You you like to breed Pham Nhat Minh (Yes/No):')
        breed = interface.Interface.cleanup(breed)
        if breed == 'yes':
            pnm.brutal_breed(wife)
            print('You had a good time')
        else:
            print("Pham Nhat Minh breed you instead. You can't escape.")
            pnm.breed_til_kho(wife, 10)
            print('Your balls are dried and now you are decending to heaven')
    def breed_as_ttm(wife):
        breed = pnm.smash_or_pass(wife)
        if (breed):
            print('You decided to play with Pham Nhat Minh and breed at the same time with torture kinky')
            pnm.brutal_breed(wife)
            print('You had a good time\nIt seems PNM still have some energy left')
            pnm.breed_til_kho(wife, 3)
            print('Your balls are dried and now you are decending to heaven')
        else:
            print('What happened? You are losing control of the game.\nERROR\nERROR\nERROR\nERROR\nERROR\nERROR\nERROR\nERROR\nERROR\nERR\nSystem reload.\n')
            #insert Phan Nhat Minh into the game
            Username = 'Pham Nhat Minh'
            preference = 'malewife'
            User = user.USER(Username, preference)
            name = 'Tran Tuan Minh'
            personality = 'shy'
            Age = 19
            wife = sorting.Sort.give_de_wife(Age, name, personality, User)
            print(f'Player: {User.username}\nWaifu: {wife.name}')
            ttm.breed_ttm(wife)
#--------------------------------------------------------------#
class laura(Loli):
    def laura_info():
        print('Congratuation! You find out Nguyen Minh Trang ester egg!!')
    def send_help():
        print('Laura the Clara is having a hard time with her homework. Now you have to save her.\nComplete these 3 questions')
        libary_of_quiz.cum_to_ask.cum_to_ask()
#--------------------------------------------------------------#
class lmu(Loli):
    def lmu_info():
        print('What?! That\'s not a loli. That\'s a Nguyen Vo Bao Lien ester egg!!\n')
    def zo_tu():
        print("Lmu's imediately call the police. She know karate. You have no chance againt her.\nYou are now spending your time in jail and see a fammiliar figure. You can felt the dangerous aura in the here.")
        making_friend = input('Would you like to approach that person? ')
        making_friend = interface.Interface.cleanup(making_friend)
        if (tecinical_logic.YesNo.TrueFlase(making_friend)):
            print('That person said that his name is Phan Nhat Minh\nHe was sent here for violating 69+21i crimes. You felt lucky that you only spend a real number of time (16 years) in jail.\nIt seems that only you are braved enough to approach this guy. Everyonelse of terrified of you and Minh.')
        else:
            print('You decided to let that person alone. You spend your time (16 years) in jail and being a come dumper for others.\nPeople hated you. You are treated worse than garbage.')
    def no_horny():
        print("Lmu ignored you and continue play LOL sqrt(-1) -- Print ERROR\nLmu ignored you and continue play LOL")
    def fake_breed(wife):
        breed = lmu.smash_or_pass(wife)
        lmu.lmu_info()
        if (breed):
            lmu.zo_tu()
        else:
            lmu.no_horny()
#--------------------------------------------------------------#
class shouta(Loli):
    def no_nothing():
        return
#--------------------------------------------------------------#
class shouta_ttm(shouta):
    def ttm_info():
        print("Congratuation! You find out Tran Tuan Minh ester egg 2!!")
    def ttm_correction():
         return
