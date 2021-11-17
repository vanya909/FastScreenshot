import os
from screenshot_maker import ScreenshotMaker

path = ''

if __name__ == '__main__':
    while True:
        path = input('Enter a directory:\n')
        if os.path.isdir(path):
            break
        print('Not a directory!')

    sm = ScreenshotMaker(path)
    sm.start()
