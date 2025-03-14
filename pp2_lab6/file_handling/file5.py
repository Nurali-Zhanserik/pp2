f = open("some.txt", "w")
f.write("Hello world")
f.close()

f = open("some.txt", "r")
print(f.read())
f.close()