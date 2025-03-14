def ulken_arip(sentence):
    count = 0
    for word in sentence:
        for letter in word:
            if letter.isupper():
                count += 1
    return count
def kishi_arip(sentence):
    count_kishi = 0
    for word in sentence:
        for letter in word:
            if letter.islower():
                count_kishi += 1
    return count_kishi            
sentence = input("Enter:")
a = ulken_arip(sentence)
b = kishi_arip(sentence)
print(f"there is {a} uppercase and {b} lowercase letters")
       

