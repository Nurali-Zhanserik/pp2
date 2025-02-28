import re
def underscore(sentence):
    x = re.findall(r"\b[a-z]+_[a-z]+\b", sentence)
    print(x)
sentence = input("Enter:")
underscore(sentence)    
