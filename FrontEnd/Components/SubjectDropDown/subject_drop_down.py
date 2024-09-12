from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.lang.builder import Builder

Builder.load_string("""
<SubjectDropDown>:
    text: 'Subject'


""")


class SubjectDropDown(MDDropDownItem):
    pass
