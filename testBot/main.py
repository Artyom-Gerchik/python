import pyautogui

screenWidth, screenHeight = pyautogui.size()

print(screenWidth)
print(screenHeight)

screenCenterX = screenWidth / 2
screenCenterY = screenHeight / 2
oneStep = 25

animDuration = 0.1


# pyautogui.screenshot()

def searchForItem():
    itemLocation = pyautogui.locateCenterOnScreen('/Users/lnxd/Desktop/pinIcon.png')
    # locateCenter returns only center x and y

    if itemLocation:
        print('Found!')
        print('x is: ' + str(itemLocation.x))
        print('y is: ' + str(itemLocation.y))
        pyautogui.moveTo(itemLocation.x / 2, itemLocation.y / 2, 1)
        # pyautogui.click()
        pyautogui.sleep(5)
    else:
        print('Not Found!')


# pyautogui.moveTo(screenCenterX, screenCenterY)


def circleFunc():
    pyautogui.moveTo(screenCenterX, screenCenterY + oneStep, animDuration)

    pyautogui.moveTo(screenCenterX + oneStep, screenCenterY + (oneStep * 2), animDuration)

    pyautogui.moveTo(screenCenterX + (oneStep * 2), screenCenterY + (oneStep * 2), animDuration)

    pyautogui.moveTo(screenCenterX + (oneStep * 3), screenCenterY + oneStep, animDuration)

    pyautogui.moveTo(screenCenterX + (oneStep * 3), screenCenterY, animDuration)

    pyautogui.moveTo(screenCenterX + (oneStep * 2), screenCenterY - oneStep, animDuration)

    pyautogui.moveTo(screenCenterX + oneStep, screenCenterY - oneStep, animDuration)

    pyautogui.moveTo(screenCenterX, screenCenterY, animDuration)


def mainFunc():
    while True:
        #searchForItem()
        circleFunc()


mainFunc()
