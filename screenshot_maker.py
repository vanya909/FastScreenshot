import os
import pyautogui as pag
from io import BytesIO
from listener import Listener


class ScreenshotMaker():
    """Класс, который делает скриншоты"""

    def __init__(self, path):

        self.path = path
        self.lis = Listener()
        self.isGetFirstPosition = False

        self.mouseX = 0
        self.mouseY = 0
        self.width = 0
        self.height = 0

    def start(self):
        while(True):
            if (self.lis.isALtPressed and
                    self.lis.isCtrlPressed and not
                        self.isGetFirstPosition):
                mouseX, mouseY = pag.position()
                self.isGetFirstPosition = True

            elif (self.isGetFirstPosition and not
                    (self.lis.isCtrlPressed and self.lis.isALtPressed)):
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

                screenshot = pag.screenshot(region=(mouseX,
                                                    mouseY,
                                                    width,
                                                    height))
                self.save_screenshot(screenshot, self.path)

                # output = BytesIO()
                # screenshot.convert("RGB").save(output, "BMP")
                # data = output.getvalue()[14:]
                # output.close()
                #
                # win32clipboard.OpenClipboard()
                # win32clipboard.EmptyClipboard()
                # win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
                # win32clipboard.CloseClipboard()

                self.isGetFirstPosition = False

    def save_screenshot(self, screenshot, path):
        files = os.listdir(path)
        pictures_numbers = []

        for file in files:
            name, extension = os.path.splitext(file)
            if extension.lower() == '.png':
                if name.isnumeric():
                    pictures_numbers.append(int(name))

        if pictures_numbers:
            screenshot_name = f"{max(pictures_numbers) + 1}.PNG"
        else:
            screenshot_name = '1.PNG'

        screenshot_path = os.path.join(path, screenshot_name)
        screenshot.save(screenshot_path, dpi=(120, 120))
        print(f'Screenshot was saved at {os.path.join(path, screenshot_name)}')
