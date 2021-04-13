import string
import random

letters = string.ascii_letters
numbers = string.digits
punctuation = string.punctuation

chars = letters + numbers + punctuation

print (chars)

state = True

while state:
    length = int(input("How long do you want your password? : "))
    count = int(input("How many passwords do you want to generate? :"))

    for x in range(count):
        x +=1
        i = str(x)
        password = ""
        for x in range(length):
            password_char = random.choice(chars)
            password = password + password_char
        print ("Password " + i + ": " + password)