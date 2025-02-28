import re
def func(sentence):
    x = re.findall("ab*", sentence)
    print(x)
sentence = input("Enter a sentence:")
func(sentence)    
