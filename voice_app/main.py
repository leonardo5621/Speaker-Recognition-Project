from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.graphics import Rectangle, Color
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget

class Manager(ScreenManager):
    pass

class Menu(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class About(Screen):
    def on_pre_enter(self):
        self.ids.box.add_widget(Description())

class Description(Widget):
    pass

class Register(Screen):
    pass

class Login(Screen):
    pass

class Voice(App):
    def build(self):
        return Manager()

if __name__=='__main__':
    Voice().run()

