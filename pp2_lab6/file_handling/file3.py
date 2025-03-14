import os 
path = os.getcwd()
if os.path.exists(path):
    print(os.path.dirname(path))
    print(os.path.basename(path))
else:
    print("It doesn't exist")    
