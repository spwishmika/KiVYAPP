from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder

Builder.load_string("""
<SubjectChip>:
    height:dp(20)
    radius:self.height/2
    MDLabel:
        text:root.subject

""")


class SubjectChip(MDCard):
    subject = StringProperty("Subject")
