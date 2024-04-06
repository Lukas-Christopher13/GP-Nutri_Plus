from . import auth

@auth("/login")
def login():
    return "login"