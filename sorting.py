import waifus

class Sort():
    def give_de_wife(Age, name, personality, User):
        wife = 0
        if User.preference == "loli":
            wife = waifus.Loli(Age, name, personality)
        elif User.preference == 'trap':
            wife = waifus.Trap(Age, name, personality)
        elif User.preference == 'malewife':
            wife = waifus.Malewife(Age, name, personality)
        elif User.preference == 'test':
            wife = waifus.test(Age, name, personality)
        elif User.preference == 'bom':
            Age = int(input('How old do you want your man be: '))
            if Age < 60:
                Age = 60
            wife = waifus.BOM(Age, name, personality)
        elif User.preference == 'shouta':
            wife = waifus.shouta(Age, name, personality)
        return wife