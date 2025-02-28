import re
a = input("Enter:").strip()
x = re.findall(r"a.*b$", a)
print(x)