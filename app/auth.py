from flask import session, request

class Session(object):

    def is_valid(self):
        if 'username' in session:
            return True

        return False

    def authenticate(self, username, password)):
    
