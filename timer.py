# This project will be about a timer counting down from a set amount of time and the person is required to enter a password
# before the timer reaches 0.00 or the timer will reset until correct password is entered.

import time

def stopWatch():
    t = 20

    while True:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


def countDown():

    t = 20
    stat = True

    while stat:
        answer = input("Enter the Answer NOW!!!")
        if answer == "jerry":
            print("yessjerr")
            stat = False
        else:
            print("Keep trying")




stopWatch()
countDown()

# while True:
#
#     a = input('enter name')
#
#     if a == "b":
#         break

