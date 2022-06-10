import mss
from time import time, sleep
import numpy as np
import cv2
from pyautogui import position
import mouse
from keyboard import is_pressed


def bot_for_m():
    """
    the bot starts and displays a window of what the bot sees.
    This window must be pointed at the float and the bot will
    start to catch fish by itself. It works based on the red
                    color on the float.
    """

    # 800x600 windowed mode
    CurrentMouseX, CurrentMouseY = position()
    mon = {"top": CurrentMouseY-50, "left": CurrentMouseX-50, "width": 200, "height": 200}

    title = "BOT MINECRAFT"
    fps = 0
    sct = mss.mss()
    last_time = time()


    while time() - last_time < 1:
        img = np.asarray(sct.grab(mon))
        fps += 1
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # convert photo to hsv

        # lower mask (0-10)
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

        # join my masks
        mask = mask0 + mask1
        hes_red = np.sum(mask)

        if hes_red > 0:
            print('i found a float')
        else:
            mouse.right_click()
            mouse.right_click()
            sleep(2)
            print("i didn't find the float")
        cv2.imshow(title, img)  # show picture
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

    return fps


def main():
    while 1:
        bot_for_m()

if __name__ == "__main__":
    main()
