import re
def func(sentence):
    x = re.findall("ab*", sentence)
    if x:
        print("Match found!")
        print(x)
    else:
        print("Match not found!")    
sentence = input("Enter a sentence:")
func(sentence)    
