print("Hi this is a vowel counter")
string = input("Please input characters:")
vowels = 'aeiou'
count = 0


for letter in string:
    if letter in vowels:
        count += 1

print("Total vowels:" + str(count))