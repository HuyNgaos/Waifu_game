class USER():
    def __init__(self, username, preference):
        self.username = username
        self.preference = preference
        self.admin = False
        if username == 'Admin' and preference == 'test':
            self.admin = True
        else:
            self.admin = False