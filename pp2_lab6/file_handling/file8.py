import os
def deleter():
    if os.path.exists("temp.py"):
        os.remove("temp.py")
    else:
        print("The file does not exist")    