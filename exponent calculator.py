greeting = input("Hello this is an exponent calculator! Please press enter!")
calculate = input("Would you like to calculate the exponent of a number? Please enter Y/N").upper()
while True:
    if calculate == "Y":
        a = int(input("Please enter the base number:"))
        b = int(input("Please enter the integer:"))
        print("Answer:" + str(a**b))
        calculate = input("Would you like to calculate the exponent of a number? Please enter Y/N").upper()
    if calculate == "N":
        break
print("See you!")

