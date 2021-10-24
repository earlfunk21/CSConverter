from kivy.core.window import Window
import os

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from home.home_screen import HomeScreen
from settings.settings_screen import SettingsScreen
from home.conversion import Content


class MyApp(MDApp):
    sm = ScreenManager()
    dialog = None

    def build(self):
        self.sm.add_widget(HomeScreen(name="Home", app=self))
        self.sm.add_widget(SettingsScreen(name="Settings"))
        return self.sm

    def switch_screen(self, screen, transition):
        self.sm.transition.direction = transition
        self.sm.current = screen

    def show_dialog(self, item):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Data Types",
                type="custom",
                content_cls=Content(item=item, dialog=self.dialog),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color, on_release=self.close
                    ),
                ],
                auto_dismiss=False
            )
        self.dialog.open()

    def change_dataType(self, obj, item):
        item.text = obj
        self.dialog.dismiss()

    def close(self, *args):
        self.dialog.dismiss(force=True)


if __name__ == '__main__':
    if os.name == 'nt':
        Window.top = 40
        Window.left = 1500
        Window.size = (400, 800)
    MyApp().run()
