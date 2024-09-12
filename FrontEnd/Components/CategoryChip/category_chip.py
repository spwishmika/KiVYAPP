from kivy.properties import StringProperty ,ListProperty
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder

Builder.load_string("""
<CategoryChip>:
    height:dp(24)
    width:dp(80)
    radius:self.height/2
    size_hint:None,None
    md_bg_color:app.theme_cls.primary_color
    MDLabel:
        id:text
        halign: "center"
        font_size:16
        color:1,1,1,1
        bold:True
        text:root.category
""")


class CategoryChip(MDCard):
    category = StringProperty("Category")
