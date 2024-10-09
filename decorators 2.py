name = input("Enter your name:")
password = input("Enter your password:")

def logged_in(function):
    def inner():
        if name == "omar" and password == "0551263328":
            function()
        else:
            print("your username or your password is not correct.")
            return
    return inner

@logged_in
def get_account():
    print("you are logged in successfully")

get_account()
