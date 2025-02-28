import re
a = input("Enter:")
x = re.sub(r"[ ,.]", ":", a)
print(x)