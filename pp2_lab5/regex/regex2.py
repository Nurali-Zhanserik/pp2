import re
def func(sentence):
    x = re.findall("ab{2}" or "ab{3}", sentence)
    print(x)
sentence = input("Enter a sentence:")
func(sentence)    