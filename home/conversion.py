from kivy.properties import ObjectProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.label import MDLabel


class Content(BoxLayout):
    item = ObjectProperty()
    dialog = ObjectProperty()


class Conversion(ThemableBehavior, Screen):
    dialog = None

    def __init__(self, **kwargs):
        super(Conversion, self).__init__(**kwargs)

    def conversion(self, data, datatype="Binary"):
        if datatype == "Binary":
            decimal = int(data, 2)
            self.ids["octal"].text = str(oct(decimal))[2:]
            self.ids["hexadecimal"].text = str(hex(decimal))[2:]
            self.ids["decimal"].text = str(decimal)
            self.ids["binary"].text = data

        elif datatype == "Octal":
            decimal = int(data, 8)
            self.ids["octal"].text = str(data)
            self.ids["hexadecimal"].text = str(hex(decimal))[2:]
            self.ids["binary"].text = bin(decimal)[2:]
            self.ids["decimal"].text = str(decimal)

        elif datatype == "Hexadecimal":
            decimal = int(data, 16)
            self.ids["octal"].text = str(oct(decimal))[2:]
            self.ids["hexadecimal"].text = str(data)
            self.ids["binary"].text = bin(decimal)[2:]
            self.ids["decimal"].text = str(decimal)

        elif datatype == "Decimal":
            self.ids["octal"].text = str(oct(int(data)))[2:]
            self.ids["hexadecimal"].text = str(hex(int(data)))[2:]
            self.ids["binary"].text = bin(int(data))[2:]
            self.ids["decimal"].text = str(data)
