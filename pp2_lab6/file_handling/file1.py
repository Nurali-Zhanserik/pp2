import os

def listing(path=os.getcwd()):  
    if not os.path.exists(path):
        print("The specified path does not exist.")
        return

    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print("\nDirectories:")
    for d in directories:
        print(d)

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print("\nFiles:")
    for f in files:
        print(f)

    # List everything
    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)


listing()  
