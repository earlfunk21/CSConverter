import os

from kivymd.theming import ThemableBehavior
from kivy.uix.screenmanager import Screen
from kivy.lang.builder import Builder

_path = os.path.dirname(__file__)
for kv in os.listdir(_path):
    if kv.endswith(".kv"):
        Builder.load_file(os.path.join(_path, kv))


class SettingsScreen(ThemableBehavior, Screen):
    def darkMode(self):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"
