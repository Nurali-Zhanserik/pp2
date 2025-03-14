def mytuple():
    size = int(input("Enter a size:"))
    tupler = [True for x in range(size)]
    check = all(tupler)
    print(check)
mytuple()        