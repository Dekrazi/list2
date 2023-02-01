


def list_print(nameList):
    for name in nameList:
        print(name)
    

def list_add(nameList, name):
    if name not in nameList:
        nameList.append(name)
        print(name + " added to the list.\n")
        

def list_del(nameList, name):
    if name in nameList:
        nameList.remove(name)
        print(name + " removed from list.\n")
    else:
        print("Name not on the list.\n")

def list_search(nameList):
    name = input("What name are you looking for? ")
    if name in nameList:
        print(name, " is on the list.\n")
    else:
        print(name, " not on the list.\n")

def secret_input():
    print("Congratulations. This is a duck:  \_o- ")





