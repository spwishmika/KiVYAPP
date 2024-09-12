from kivy.properties import StringProperty
from kivymd.uix.anchorlayout import MDAnchorLayout
from kivy.uix.button import ButtonBehavior
from kivy.lang.builder import Builder

Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect

<Task>:
    padding:10
    size_hint:1,None
    height:dp(260)
    MDCard:
        radius:10
        style :"outlined"
        line_color:(0.2, 0.2, 0.2, 0.8)
        on_press: root.on_press(root)
        MDAnchorLayout:
            MDRelativeLayout:
                MDAnchorLayout:
                    anchor_x:"right"
                    anchor_y:"top"
                    MDAnchorLayout:
                        size_hint:None,None
                        height:dp(40)
                        width:dp(100)
                        CategoryChip:
                            category:root.category
            MDBoxLayout:
                orientation:"vertical"
                size_hint:None,None
                height:self.parent.height - dp(20)
                width:self.parent.width - dp(20)
                MDRelativeLayout:
                    size_hint:1,None
                    height:dp(24)
                    MDAnchorLayout:
                        anchor_x:'left'
                        anchor_y:'bottom'
                        MDLabel:
                            text:root.title
                            adaptive_size:True
                            font_size:sp(18)
                            bold:True
                                
                MDBoxLayout:
                    size_hint:1,None
                    height:dp(24)
                    MDLabel:
                        halign:"left"
                        text:root.subject
                        font_size:sp(16)
                        color:0,0,0,0.4
                        
                MDBoxLayout:
                    MDAnchorLayout:
                        md_bg_color:app.theme_cls.primary_light
                        radius:10
                        MDAnchorLayout:
                            size_hint:None,None
                            height:self.parent.height - dp(8)
                            width:self.parent.width - dp(8)
                            MDScrollView:
                                do_scroll_x: False
                                do_scroll_y: True
                                effect_cls:ScrollEffect
                                MDLabel:
                                    multiline: True
                                    halign: 'left'
                                    adaptive_height:True
                                    markup:True
                                    text:root.description
                
""")


class Task(MDAnchorLayout):
    title = StringProperty("Create a Task!")
    category = StringProperty("none")
    subject = StringProperty("subject")
    description = StringProperty("Press the create button to create a task. explore the app for more features.")

    def on_press(self, widget):
        print("Pressed")
