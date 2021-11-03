#!/usr/bin/python3

try:
    import random
    import string
except Exception as e:
    print("Some modules are not installed" + e)

password = []

def pass_generator(digits, upper=0, num=0, special=0):

    while digits > 0:
        while special > 0:
            password.append(random.choice(string.punctuation))
            special -= 1
            digits -= 1
        while num > 0:
            password.append(random.choice(string.digits))
            num -= 1
            digits -= 1
        while upper > 0:
            password.append(random.choice(string.ascii_uppercase))
            upper -= 1
            digits -= 1
        if digits > 0:
            password.append(random.choice(string.ascii_lowercase))
            digits -= 1

    return(random.shuffle(password))

def custom():
    f_custom = 1
    while f_custom == 1:
        try:
            first = int(input("Number of digits: "))
            second = int(input("Number of uppercase: "))
            third = int(input("Number of numeric: "))
            fourth = int(input("Number of special: "))
            f_custom = 0
            if first < 0 or second < 0 or third < 0 or fourth < 0 or first < (second + third + fourth):
                f_custom = 1
                print("Specify valid arguments")
        except:
            f_custom = 1
            print("Specify valid arguments")
    return (first, second, third, fourth)

print("\n* * * Welcome to password generator * * * \n")
print("1 - weak (8 digits, 2 upper, num)")
print("2 - medium (10 digits, 2 upper, num, special)")
print("3 - strong (12 digits, 3 upper, num, special)")
print("4 - recomended (16 digits, 4 upper, num, special")
print("5 - custom")
print("6 - custom, multiple")

f_opt = 1
while f_opt == 1:
    try:
        choice = int(input("\nHow strong password you want?"))
    except:
        choice = None
    if choice == 1:
        f_opt = 0
        print("You choose weak password")
        pass_generator(8, 2, 2)
        print('\n', *password, '\n', sep='')

    elif choice == 2:
        f_opt = 0
        print("You choose medium password")
        pass_generator(10, 2, 2, 2)
        print('\n', *password, '\n', sep='')

    elif choice == 3:
        f_opt = 0
        print("You choose strong password")
        pass_generator(12, 3, 3, 3)
        print('\n', *password, '\n', sep='')

    elif choice == 4:
        f_opt = 0
        print("You choose recomended password")
        pass_generator(16, 4, 4, 4)
        print('\n', *password, '\n', sep='')

    elif choice == 5:
        f_opt = 0
        print("You choose custom password")
        first, second, third, fourth = custom()
        pass_generator(first, second, third, fourth)
        print('\n', *password, '\n', sep='')
        
    elif choice == 6:
        f_opt = 0
        print("You choose multiple password")
        f_multiply = 1
        while f_multiply == 1:
            try:
                multiply = int(input("Number of passwords: "))
                f_multiply = 0
                if multiply < 0:
                    f_multiply = 1
                    print("Specify valid number")
            except:
                f_multiply = 1
                print("Specify valid number")
        first, second, third, fourth = custom()
        while multiply > 0:
            pass_generator(first, second, third, fourth)
            print('\n', *password, sep='')
            password = []
            multiply -= 1
        print('', sep='')

    else:
        print("Please specify correct option")
