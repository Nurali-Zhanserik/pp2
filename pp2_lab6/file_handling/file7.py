with open("some.txt", "r") as task:
    with open("default.txt", "w") as task1: #default is empty
        task1.write(task.read())
with open("default.txt", "r") as f:
    print(f.read())        