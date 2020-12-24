# This project will be about a timer counting down from a set amount of time and the person is required to enter a password
# before the timer reaches 0.00 or the timer will reset until correct password is entered.

import time


def countDown(arg):
    t = 20
    stat = True
    if arg != 'Jerry':
        while stat:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            countDown(answer)
    else:
        stat = False
        print("Yezzir buddy")


answer = input("Enter the Answer NOW!!!")

countDown(answer)


