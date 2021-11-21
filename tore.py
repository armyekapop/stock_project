import kivy
from typing import Text
from kivy.app import App
from kivy.core import text
from kivy.uix.behaviors import button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

from kivy.config import Config
Config.set('graphics', 'resizable', False)

class MygridLaout(GridLayout):
    def __init__(self, **kwargs):
        super(MygridLaout,self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='Name : '))
        self.name = TextInput(multiline = True)
        self.add_widget(self.name)

        self.add_widget(Label(text='Fav food : '))
        self.favFood = TextInput(multiline = False)
        self.add_widget(self.favFood)

        #creat button
        self.submit = Button(text='Submit')
        #bind the button
        self.submit.bind(on_press = self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        favFood = self.favFood.text

        #print to screen
        self.add_widget(Label(text = f'name : {name} , fav : {favFood}'))

        #clear then  input
        self.name.text = ''
        self.favFood.text = ''

class Myapp(App):
    def build(self):
        return MygridLaout()

if __name__=='__main__':
    Myapp().run()