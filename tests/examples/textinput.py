from kivy.uix.behaviors import ButtonBehavior
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.label import Label
kv = '''
#:import hex kivy.utils.get_color_from_hex
BoxLayout:
    SelectableText:
        text: "Hello world"
        haligh: "center"
        canvas.before:
            Color:
            rgba: app.theme_cls.primary_color
'''

class SelectableText(Label, ButtonBehavior):
    pass


class Test(MDApp):
    def build(self):
        root = Builder.load_string(kv)
        return root


Test().run()
