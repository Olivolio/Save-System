import pickle


class isAClass:
    def __init__(self, name, height):
        self.name = name
        self.height = height


def load():
    global myClass, myClass2
    with open("save.bin", "rb") as save_file:
        [myClass, myClass2] = pickle.load(save_file)


def create_new():
    global myClass, myClass2
    n = input("What would you like the name to be? ")
    h = int(input("What would you like the height to be?  "))
    myClass = isAClass(n, h)
    myClass2 = isAClass(n, h + 20)

def save():
    with open("save.bin", "wb") as file:
        # in here the file is open
        pickle.dump([myClass, myClass2], file)

    # the file is closed now

if __name__ == '__main__':
    myClass = None
    myClass2 = None
    try:
        open("save.bin", 'x')
        create_new()
    except:
        print(" We are in the except statement")
        print("This means the file already exists")
        load()

    print("Name " + myClass.name)
    print("Height ", myClass.height)

    print("Name ", myClass2.name)
    print("Height ", myClass2.height)

    save()

