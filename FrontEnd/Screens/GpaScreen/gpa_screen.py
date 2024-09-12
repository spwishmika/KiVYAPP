from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<GPAScreen>:
    md_bg_color:1,0,0,0.2

""")


class GPAScreen(MDScreen):
    pass
