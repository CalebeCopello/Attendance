import kivy
import main

kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

class MyWindowApp(App):
    
    def build(self):
        str = 'Hello, World!'
        return Label(text=f"""{str}\nHey, There!""")
    
    
if __name__ == '__main__':
    MyWindowApp().run()