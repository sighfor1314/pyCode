import keyboard
import time
import random
class PathFinder:
        
    def setStele(self):
        keyboard.press_and_release('=, =')


    def setAttack():
        for i in range(random.randint(2,6)):
            time.sleep(random.uniform(0.05, 0.3))
            keyboard.press_and_release('ctrl,ctrl')
        time.sleep(0.1)



    def setRight():
        keyboard.press('right')
        time.sleep(0.1)
        keyboard.release('right')


    def setLeft():
        keyboard.press('left')
        time.sleep(0.1)
        keyboard.release('left')


    def setTransferRight():
        time.sleep(0.3)
        keyboard.press('right')
        time.sleep(0.3)
        keyboard.press_and_release('a', 'a')
        time.sleep(0.1)
        keyboard.release('right')
        time.sleep(0.1)


    def setTransferLeft():
        time.sleep(0.3)
        keyboard.press('left')
        time.sleep(0.3)
        keyboard.press_and_release('a', 'a')
        time.sleep(0.1)
        keyboard.release('left')
        time.sleep(0.1)


    def setTransferUp():
        time.sleep(0.3)
        keyboard.press('up')
        time.sleep(0.3)
        keyboard.press_and_release('a', 'a')
        time.sleep(0.1)
        keyboard.release('up')
        time.sleep(0.1)



    def setDoubleJumpRight():
        time.sleep(0.2)
        keyboard.press('right')
        time.sleep(0.3)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.release('right')
        time.sleep(0.1)




    def setDoubleJumpLeft():
        time.sleep(0.2)
        keyboard.press('left')
        time.sleep(0.3)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.release('left')
        time.sleep(0.1)


    def setJumpRight():
        time.sleep(0.1)
        keyboard.press('right')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        keyboard.release('right')
        time.sleep(0.05)

    def setJumpLeft():
        time.sleep(0.1)
        keyboard.press('left')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        keyboard.release('left')
        time.sleep(0.05)


    def setJumpDown():
        time.sleep(0.1)
        keyboard.press('down')
        time.sleep(0.1)
        keyboard.press_and_release('alt', 'alt')
        time.sleep(0.1)
        keyboard.release('down')


    def setCrowStorm():
        time.sleep(0.3)
        keyboard.press_and_release('1', '1')
        time.sleep(1)
        keyboard.press_and_release('n', 'n')


    def setEmancipation():
        time.sleep(0.3)
        keyboard.press('a')
        time.sleep(0.3)
        keyboard.press_and_release('m', 'm')
        time.sleep(0.1)
        keyboard.release('a')



    def setObsidian():
        time.sleep(0.3)
        keyboard.press_and_release('shift', 'shift')
        time.sleep(0.8)
        keyboard.press_and_release('f', 'f')

