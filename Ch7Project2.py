#! python3
import re


def password_check():
    pw = input('Input a password: >>>   ')

    flag = 0

    while True:
        if (len(pw)<8):
            flag = -1
            break
        elif not re.search(r'[a-z]', pw):
            flag = -1
            break
        elif not re.search(r'[A-Z]', pw):
            flag = -1
            break
        elif not re.search(r'[0-9]', pw):
            flag = -1
            break
        else:
            print('This is a valid password.')
            break

    if flag == -1:
        print('This is not a valid password')
        password_check()

password_check()
