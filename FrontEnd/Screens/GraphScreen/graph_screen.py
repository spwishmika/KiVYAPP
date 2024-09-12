from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen

Builder.load_string("""
<GraphScreen>:
    md_bg_color:1,0,0,0.2

""")


class GraphScreen(MDScreen):
    pass
