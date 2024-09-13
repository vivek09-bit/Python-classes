def VowelsCount(text):
    Vowels = 'aeiouAEIOU'
    count = 0
    for i in text:
        if i in Vowels:
            count +=1
    return count
    

text = 'work in ok works is done. addidass'
print(VowelsCount(text))