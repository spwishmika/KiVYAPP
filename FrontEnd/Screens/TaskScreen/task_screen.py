from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout

from FrontEnd.Components.Task.Task import Task
from FrontEnd.Screens.CreateScreen.create_screen import CreateScreen
from BackEnd.data_base import DATA

Builder.load_string("""
#:import ScrollEffect kivy.effects.scroll.ScrollEffect
#:import NoTransition kivy.uix.screenmanager.NoTransition

<TaskScreen>:
    orientation:"vertical"
    md_bg_color:app.theme_cls.bg_normal
    ScreenManager:
        id:task_screen_manager
        transition:NoTransition()
        MDScreen:
            name:"task"
            MDScrollView:
                orientation:"vertical"
                effect_cls:ScrollEffect
                MDBoxLayout:
                    id:task_list
                    size_hint:1,None
                    adaptive_height:True
                    orientation:"vertical"

            MDRelativeLayout:
                MDAnchorLayout:
                    anchor_x:'right'
                    anchor_y:'bottom'
                    MDAnchorLayout:
                        size_hint:None,None
                        size:100,120
                        MDFloatingActionButton:
                            icon: "pen"
                            on_press:root.create_screen()

""")


class TaskScreen(MDBoxLayout):

    def on_kv_post(self, base_widget):
        task = DATA.get_task_data()
        if len(task["tasks"]) == 0:
            self.ids.task_list.add_widget(Task())
        self.add_task()

    def add_task(self):
        task = DATA.get_task_data()
        for tasks in task["tasks"]:
            create_task_obj = Task(
                title=tasks["title"],
                category=tasks["category"],
                subject=tasks["subject"],
                description=tasks["description"]
            )
            self.ids.task_list.add_widget(create_task_obj)

    def create_screen(self):
        screen_manager: ScreenManager = self.ids.task_screen_manager
        if screen_manager.has_screen("create"):
            screen_manager.remove_widget(screen_manager.get_screen("create"))
        create_screen = CreateScreen(name="create")
        screen_manager.add_widget(create_screen)
        screen_manager.current = "create"
