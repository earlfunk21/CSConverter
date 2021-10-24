import os

from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.theming import ThemableBehavior
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import OneLineListItem, MDList

_path = os.path.dirname(__file__)
for kv in os.listdir(_path):
    if kv.endswith(".kv"):
        Builder.load_file(os.path.join(_path, kv))


class ItemDrawer(OneLineListItem):
    pass


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class HomeScreen(ThemableBehavior, Screen):
    toolBarLeftItem = StringProperty("menu")
    toolBarConfig = {
        "Home": "menu"
    }
    app = ObjectProperty()

    def on_pre_enter(self, *args):
        self.load()

    def load(self):
        self.ids["drawer_list"].clear_widgets()
        for text in self.app.sm.screen_names:
            self.ids["drawer_list"].add_widget(
                ItemDrawer(text=text, on_release=lambda x: self.app.switch_screen(x.text, "left"))
            )

    def switch_screen(self, screen):
        self.name = screen
        self.toolBarLeftItem = self.toolBarConfig[screen]
        self.ids["home_manager"].current = screen

    def change_icon(self):
        if self.name == "Home":
            print("Home")
        else:
            self.switch_screen(self.ids["home_manager"].previous())

    def open_nav_drawer(self, instance):
        self.load()
        instance.set_state("open")
