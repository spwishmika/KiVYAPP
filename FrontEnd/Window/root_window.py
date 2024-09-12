from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
from kivy.lang.builder import Builder

Builder.load_string("""
#:import NoTransition kivy.uix.screenmanager.NoTransition

<RootWindow>:
    orientation:"vertical"
    MDTopAppBar:
        title: "Reminder"
        #right_action_items: [["menu", lambda x: print("hello")]]
        elevation:0
        
    MDBottomNavigation:
        transition: NoTransition
        MDBottomNavigationItem:
            name: "home"
            text: 'Task'
            text_color_active: 0, 0, 0, 1
            icon: 'notebook'
            badge_icon: root.badge_icon #"alert-circle-outline" "numeric-10"
            TaskScreen:
                name:"task_screen"
                
                
        MDBottomNavigationItem:
            name: "graph"
            text: 'Graph'
            text_color_active: 0, 0, 0, 1
            icon: 'chart-line'
            GraphScreen:
                name:"graph_screen"


        MDBottomNavigationItem:
            name: "gpa"
            text: 'gpa'
            text_color_active: 0, 0, 0, 1
            icon: 'school'
            GPAScreen:
                name:"gpa_screen"
                
""")


class RootWindow(MDBoxLayout):
    badge_icon = StringProperty("numeric-0")

    def get_numeric_value(self):
        # TODO: if task > 10 : "alert-circle-outline" else: f"numeric-{value}"
        pass

