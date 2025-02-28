import re

def camel_to_snake(s):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', s).lower()


s = input("Enter a camelCase string: ")
print("Snake case:", camel_to_snake(s))
