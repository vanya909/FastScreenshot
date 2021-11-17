from pynput import keyboard

class Listener():
    """Класс, который проверяет нажатие нужных клавиш"""

    def __init__(self):
        self.isCtrlPressed = False
        self.isALtPressed = False

        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()

    def on_press(self, key):
        if key == keyboard.Key.ctrl_r:
            self.isCtrlPressed = True
        elif key == keyboard.Key.alt_r or key == keyboard.Key.alt_gr:
            self.isALtPressed = True

    def on_release(self, key):
        if key == keyboard.Key.ctrl_r:
            self.isCtrlPressed = False
        elif key == keyboard.Key.alt_r or key == keyboard.Key.alt_gr:
            self.isALtPressed = False
