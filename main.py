from kivymd.app import MDApp
from kivymd.theming import ThemeManager
import random

from FrontEnd import *
# from BackEnd import *


class Reminder(MDApp):
    def build(self):
        color_list = ['Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'BlueGray']
        self.theme_cls.primary_palette = random.choice(color_list)
        self.theme_cls.accent_palette = "Red"
        return RootWindow()


if __name__ == "__main__":
    Reminder().run()
