#for types of waifus
class waifu():
    def __init__(self, age, name, personality):
        self.age = age
        self.name = name
        self.personality = personality
        self.cuteness = "Super adorable"

class nonewife(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.type = 'DNE'

class test(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.gender = 'yes'
        self.breedable = True
        self.type = 'test'

class Loli(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.gender = 'female'
        self.breedable = False
        self.type = 'loli'

class Trap(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.gender = 'male?'
        self.breedable = 'True?, False?'
        self.type = 'trap'

class Malewife(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.gender = 'male'
        self.breedable = 'Hmmmmmmm'
        self.type = 'malewife'

class BOM(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.cuteness = 'No'
        self.gender = 'male'
        self.breedable = True
        self.type = 'bom'

class shouta(waifu):
    def __init__(self, age, name, personality):
        super().__init__(age, name, personality)
        self.gender = 'male'
        self.breedable = False
        self.type = 'shouta'