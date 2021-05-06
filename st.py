"""
A simple timer that takes an integer in milliseconds and then displays a countdown timer. Displays a windows notification when finished.
"""

import sys
import time
from win10toast import ToastNotifier


def main():
    t = sys.argv[1]
    try:
        t = int(t)
    except ValueError:
        print("Argument not an integer, exiting...")
        exit()

    countdown(t)  # 1500 is 25min


def countdown(t):
    toaster = ToastNotifier()
    print("\n --- Study session started ---\n")
    while t:
        mins, secs = divmod(t, 60)
        timer = "    {:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("+++ Study session finished +++")

    toaster.show_toast(
        "End of study session!",
        "Relax and recollect.",
        icon_path="clock.ico",
        duration=10,
    )
    while toaster.notification_active():
        time.sleep(0.1)


if __name__ == "__main__":
    main()
