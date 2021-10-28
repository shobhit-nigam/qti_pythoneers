listx = ['e', 'a', 'r', 't', 'h', ' ', 'i', 's', ' ', 'h', 'o', 'm', 'e']

def only_vowels(ch):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ch in vowels

listy = list(filter(only_vowels, listx))

print(listy)
