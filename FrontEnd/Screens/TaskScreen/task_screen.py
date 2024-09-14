from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout

from FrontEnd.Components.Task.Task import Task
from FrontEnd.Screens.CreateScreen.create_screen import CreateScreen

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
                    Task:

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

    def on_enter(self, *args):
        # TODO: on enter read all json task and make object and add all to the screen.
        # TODO: fist remove all elements. and add
        pass

    def add_task(self, widget):
        if isinstance(widget, Task):
            self.ids.task_list.add_widget(widget)

    def create_screen(self):
        screen_manager: ScreenManager = self.ids.task_screen_manager
        if screen_manager.has_screen("create"):
            screen_manager.remove_widget(screen_manager.get_screen("create"))
        create_screen = CreateScreen(name="create")
        screen_manager.add_widget(create_screen)
        screen_manager.current = "create"

