
class waifu_interact():
    def breed(wife):
        noises = f'Ahhhh!!!! Ahh!!!'
        return noises
    def brutal_breed(wife):
        noises = 'AHHHHHHH!!!!, AHHHH!!!!, AHHHH!!!'
        return noises
    def after_breed_goodend(wife):
        result = 'You had a good time with your '
        return result
    def after_breed_badend(wife):
        result = f"You clean up your self after bang the {wife.personality} brat\nand see far away the FBI squad is approaching you.\n"
        return result
#------------------------------------------
class test(waifu_interact):
    def info_test(wife):
        info = f"Debug mode\nHere is your {wife.name} status\n{wife.name} age: {wife.age}\n{wife.name} personality: {wife.personality}\n{wife.name} breedable status: {wife.breedable}"
        return info
#------------------------------------------
class loli(waifu_interact):
    def info_loli(wife):
        info = f"Here is your {wife.name} status\n{wife.name} age: {wife.age}\n{wife.name} personality: {wife.personality}\n{wife.name} breedable status: {wife.breedable}"
        return info
    def legal_breed(wife):
        noises = loli.breed(wife)
        return f"{wife.name}: {noises}"
    def correction(wife):
        noises = loli.brutal_breed(wife)
        return f"{wife.name}: {noises}"
    def legal_finished(wife):
        result = loli.after_breed_goodend(wife) + f'legal {wife.name}'
        return result
    def illegal_finished(wife):
        result = loli.after_breed_badend(wife) + 'You are going to spend the rest of your life in jail.'
        return result
#------------------------------------------ 
class trap(waifu_interact):
    def info_trap(wife):
        info = f"You have good taste.\nHere is your boy status:\nGender: {wife.gender}\nCuteness level: {wife.cuteness}\nBreedable status: {wife.breedable}"
        return info
    def breed_trap(wife):
        noises = trap.breed(wife)
        return f"{wife.name}: {noises}"
    def trap_finished(wife):
        result = trap.after_breed_goodend(wife) + f'best girl(?), {wife.name}'
        return result
#------------------------------------------
class malewife(waifu_interact):
    def info_malewife(wife):
        info = f"You have good taste.\nHere is your boy status:\nGender: {wife.gender} \nBreedable status: {wife.breedable}"
        return info
    def breed_mw(wife):
        noises = trap.breed(wife)
        return f"{wife.name}: {noises}"
    def malewife_finished(wife):
        result = malewife.after_breed_goodend(wife) + f'best wife(?), {wife.name}'
        return result
#------------------------------------------
class bom(waifu_interact):
    def info_bom(wife):
        info = f"Here is your {wife.name}-san status\n{wife.name}-san age: {wife.age}\n{wife.name}-san personality: {wife.personality}\n{wife.name}-san breedable status: {wife.breedable}"
        return info
    def breed_bom(wife):
        noises = trap.breed(wife)
        return f"{wife.name}: {noises}"
    def bom_finished(wife):
        result = bom.after_breed_goodend(wife) + f'{wife.name}-san'
        return result
#------------------------------------------
class shouta(loli):
    def info_shouta(wife):
        info = loli.info_loli(wife)
        return info
    def breed_shouta(wife):
        noises = trap.breed(wife)
        return f"{wife.name}: {noises}"
#------------------------------------------