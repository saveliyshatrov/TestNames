# функция суммирования
def LetterSum(string):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    string = string.lower()
    Counter = 0
    for i in range(len(string)):
        Counter += ALPHABET.index(string[i]) + 1
    return Counter


f = open('names.txt', 'r').read()
ArrayOfNames = f.replace('"', '').split(',')
ArrayOfNames.sort()  # Лексикографический порядок имен
Counter = 0
for i in range(len(ArrayOfNames)):
    Counter += (i+1)*LetterSum(ArrayOfNames[i])

print(Counter)
