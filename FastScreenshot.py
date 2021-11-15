import pyautogui as pag
from pynput import keyboard
import win32clipboard
from io import BytesIO

isCtrlPressed = False
isALtPressed = False
isGetFirstPosition = False

mouseX = 0
mouseY = 0
width = 0
height = 0

def on_press(key):
    global isCtrlPressed
    global isALtPressed
    if key == keyboard.Key.ctrl_l:
        isCtrlPressed = True
    elif key == keyboard.Key.alt_l:
        isALtPressed = True

def on_release(key):
    global isCtrlPressed
    global isALtPressed
    if key == keyboard.Key.ctrl_l:
        isCtrlPressed = False
    elif key == keyboard.Key.alt_l:
        isALtPressed = False

# Collect events until released
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()




if __name__ == "__main__":
    while(True):
        #print(isCtrlPressed)
        if isALtPressed and isCtrlPressed and not isGetFirstPosition:
            mouseX, mouseY = pag.position()
            isGetFirstPosition = True
            print('Get first position')

        elif isGetFirstPosition and (not isCtrlPressed or not isALtPressed):
            mouseLastX, mouseLastY = pag.position()

            if mouseLastX < mouseX:
                mouseLastX, mouseX = mouseX, mouseLastX
            if mouseLastY < mouseY:
                mouseLastY, mouseY = mouseY, mouseLastY

            width = mouseLastX - mouseX
            height = mouseLastY - mouseY

            if width == 0 or height == 0:
                isGetFirstPosition = False
                continue

            screenshot = pag.screenshot(region=(mouseX, mouseY, width, height))

            output = BytesIO()
            screenshot.convert("RGB").save(output, "BMP")
            data = output.getvalue()[14:]
            output.close()

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
            win32clipboard.CloseClipboard()

            print('Make screenshot')

            isGetFirstPosition = False
