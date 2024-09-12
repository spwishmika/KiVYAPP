from kivymd.uix.anchorlayout import MDAnchorLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder
from kivymd.uix.screen import MDScreen
import datetime

Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect

<CreateScreen>:
    md_bg_color:app.theme_cls.bg_normal
    MDAnchorLayout:
        MDBoxLayout:
            orientation:"vertical"
            size_hint:None,None
            height:self.parent.height - dp(20)
            width:self.parent.width - dp(20)
            MDBoxLayout:
                size_hint:1,None
                #height:dp(68)
                adaptive_height:True
                MDRaisedButton:
                    elevation:0
                    text:"Subject"
                    
                    
                MDBoxLayout:
                MDRaisedButton:
                    elevation:0
                    text:"Category"
                    
                    
            MDAnchorLayout:
                size_hint:1,None
                height:dp(68)
                MDTextField:
                    hint_text: "Title"
                    max_length_text_color: "red"
                    max_text_length: 24
                    mode: "rectangle"
                    focus:True
                    
            MDAnchorLayout:
                size_hint:1,None
                height:dp(120)
                MDTextField:
                    hint_text: "Description"
                    size: self.height, dp(100)
                    mode: "rectangle"
                    multiline: True
                    max_height: "100dp"
            MDTextField:
                hint_text: "Task End Date"
                helper_text: "Enter a valid dd/mm/yyyy date"
                validator: "date"
                mode: "rectangle"
                date_format: "dd/mm/yyyy"
                date_interval: None, "01/01/2100"
            
            MDAnchorLayout:
                MDAnchorLayout:
                    #md_bg_color:app.theme_cls.primary_color
                    size_hint:None,None
                    height:self.parent.height - dp(60)
                    width:self.parent.width - dp(10)
                    anchor_x:"left"
                    anchor_y:"top"
                    MDLabel:
                        text:"Fill All Information"
                        adaptive_size:True
                        font_size:sp(24)
                        color:app.theme_cls.accent_color
                        bold:True
                        
                        
    
    
    MDRelativeLayout:
        MDAnchorLayout:
            anchor_x:'right'
            anchor_y:'bottom'
            MDAnchorLayout:
                size_hint:None,None
                size:100,120
                MDFloatingActionButton:
                    icon: "check-bold"
                    on_press:
                        root.submit()
        MDAnchorLayout:
            anchor_x:'left'
            anchor_y:'bottom'
            MDAnchorLayout:
                size_hint:None,None
                size:100,120
                MDFloatingActionButton:
                    icon: "close-thick"
                    on_press:
                        root.parent.current = "task"
                        root.cansel()
                        
                        
    
""")


class CreateScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super(CreateScreen, self).__init__(*args, **kwargs)
        self.today = datetime.date
        self.task = {
            "title": "",
            "subject": "",
            "category": "",
            "description": "",
            "start_date": [self.today.year, self.today.month, self.today.day],
            "end_date": [0, 0, 0]
        }

    def create_a_task(self, id_, obj):
        self.task[id_] = obj

    def cansel(self):
        del self.today
        del self.task
        print("deleted")

    def submit(self):
        template = {
            "title": "",
            "subject": "",
            "category": "",
            "description": "",
            "start_date": [self.today.year, self.today.month, self.today.day],
            "end_date": [0, 0, 0]
        }
        if self.task["title"] == template["title"]:
            return
        elif self.task["subject"] == template["subject"]:
            return
        elif self.task["category"] == template["category"]:
            return
        elif self.task["description"] == template["description"]:
            return
        elif self.task["end_date"] == template["end_date"]:
            return
        else:
            # TODO: creaate json data base
            self.parent.current = "task"
