class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self, entered_password):
        return self.password == self.entered_password
