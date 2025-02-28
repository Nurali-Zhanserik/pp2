import re
def one_upper_lowerletters(a):
    x = re.findall("[A-Z][a-z]+", a)
    print(x)
a = input("Enter:")
one_upper_lowerletters(a)    