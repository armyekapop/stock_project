# The Other Imports
import kivy
from kivy.uix.widget import Widget
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.text import Label, LabelBase
# Make Sure This Is Always the last import
from kivy import Config
Config.set('graphics', 'multisamples', '0')
LabelBase.register(name = "Mitr-Medium" ,fn_regular = 'Mitr-Medium.ttf')


class MyLayout(Widget):
    pass
class SecondWindow(Widget):
    pass
# Main Code
class MyApp(App):
    def build(self):
        return MyLayout()


# Run This Thing
if __name__ == "__main__":
    MyApp().run()