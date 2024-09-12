from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.lang.builder import Builder

Builder.load_string("""
<CategoryDropDown>:
    text: 'Category'
    MDLabel:
        text:"hello"

""")

class CategoryDropDown(MDDropDownItem):
    pass
