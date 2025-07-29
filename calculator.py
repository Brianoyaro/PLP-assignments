def user_number(type_: str) -> int:
    '''
    Helper function for obtaining a user's number input
    '''
    while True:
        try:
            num = int(input(f"Select {type_} number: "))
            break
        except ValueError:
            print("invalid number. Try again")
            continue
    return num
def user_sign() -> str:
    '''
    Helper function for receiving mathematical operation sign
    '''
    while True:
        sign = input("Select mathematical operator: ")
        if sign[0] in '*/+-':
            break
        else:
            print('You have selected an invalid operator')
    return sign
print("Hello, I am your friendly associate calculator.\nAllowed operators:\n\t* for multiplication.\n\t/ for division.\n\t- for subtraction.\n\t+ for addition\n")
while True:
    print('_____________________________________________________________________________')
    off = input("Press 'q' or 'quit' if you'd like to quit or press Enter to continue.")
    if off.startswith('q'):
        break
    a = user_number('first')
    sign = user_sign()
    b = user_number('second')

    if sign.startswith('-'):
        operation = f'{a} - {b}'
        res = a - b
    elif sign.startswith('+'):
        operation = f'{a} + {b}'
        res = a + b
    elif sign.startswith('*'):
        # handle exponential
        if len(sign) > 1 and sign[1] == '*':
            operation = f'{a} ** {b}'
            res = a ** b
        else:
            operation = f'{a} * {b}'
            res = a * b
    elif sign.startswith('/'):
        # handle floor division
        if len(sign) > 1 and sign[1] == '/':
            operation = f'{a} // {b}'
            res = a // b
        else:
            if a != 0:
                operation = f'{a} / {b}'
                res = a / b
            else:
                print('\nMATHEMATICAL ERROR! You can not divide 0 with a nnumber')
                continue
    # handle unknown operator
    else:
        continue
    print(f"\nYour calculation is {operation} = {res}.")
    # print("\nAnswer is: ", res)
print('Exiting....')
