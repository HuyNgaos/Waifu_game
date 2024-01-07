import waifus as wf
import tecinical_logic as lg
from os import path

class Sort():
    def __init__(self, username, usertaste):
        self.username = username
        self.usertaste = usertaste
    def namE(self):
        match self.username:
            case 'admin':
                return True
            case _:
                return False
    def check_ad(self,user_status):
        if user_status == True and self.usertaste == 'test':
            return True
        else:
            return False
        
class waifu_sort(Sort):
    def __init__(self, username, usertatse, Age, name, personality):
        super().__init__(username, usertatse)
        self.w_name = name
        self.w_age = Age
        self.w_personality = personality
    def tastE(self, admin):
        match self.usertaste:
            case 'loli':
                name = self.w_name + '-chan'
                wife = wf.Loli(self.w_age, name, self.w_personality)
            case 'test':
                wife = wf.test(self.w_age, self.w_name, self.w_personality)
            case 'trap':
                age = 18
                wife = wf.Trap(age, self.w_name, self.w_personality)
            case 'malewife':
                age = 20
                wife = wf.Malewife(age, self.w_name, self.w_personality)
            case 'bom':
                age =60
                wife = wf.BOM(age, self.w_name, self.w_personality)
            case 'shouta':
                wife = wf.shouta(self.w_age, self.w_name, self.w_personality)
            case _:
                wife = wf.nonewife(self.w_age, self.w_name, self.w_personality)
        if (admin):
            lg.admin_log.log(wife_name = wife.name, wife_age = wife.age, wife_personality = wife.personality, wife_type = wife.type)
        return wife
    
class img_file():
    def img_file(wife):
        proto_path = 'pictures/'
        if wife.type == 'loli' and wife.age < 18:
            path_= proto_path + wife.type +'_under_age_ending.gif'
        else:
            path_ = proto_path + wife.type + '_ending.gif'
        if (path.exists(path_)):
            return path_
        else:
            return 'pictures/unknown.gif'
        
class ending_pic_file():
    def end_file(wife):
        proto_path = 'pictures/ending/'
        if wife.type == 'loli' and wife.age < 18:
            path_ = proto_path + wife.type + "_under_age.gif"
        else:
            path_ = proto_path + wife.type + '_ending.gif'
        if (path.exists(path_)):
            return path_
        else:
            return proto_path + 'unknown_ending.gif'