import getpass
import cryptocode


def get(pin: str = ""):
    try:
        with open("../token/token", "r+", encoding="UTF-8") as file:
            _token = file.read()
    except Exception as a:
        print(a)
        return create()[0]
    if not pin:
        pin = getpass.getpass("Enter pincode\n> ")
    while not cryptocode.decrypt(_token, pin):
        pin = getpass.getpass("Wrong pincode! Try again\n> ")
    return cryptocode.decrypt(_token, pin)


def create(token: str = ""):
    print("Enter bot token to continue, or press CTRL+C to exit")
    while not len(token) == 72:
        print("It's must be 72 characters")
        token = getpass.getpass("> ").lstrip().rstrip()
    print("Ok! Now create a PIN-CODE to protect your token.\n"
          "You need to enter it each time you start this bot")
    pin = ""
    while not len(pin) >= 4:
        print("It's must be more than 4 characters")
        pin = getpass.getpass("> ")
    with open("../token/token", "w+", encoding="UTF-8") as file:
        file.write(cryptocode.encrypt(token, pin))
    return token, pin


if __name__ == "__main__":
    print(get())
    ...
