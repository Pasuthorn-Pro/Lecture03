inchar = input("Input one character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("You in put Upper case letter ", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You in put Lower case letter ", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You input number ", inchar)
else :
    print("It's not a letter or number.", inchar)