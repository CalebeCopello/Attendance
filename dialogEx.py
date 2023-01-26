#kivy imports
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import main

kivy.require('2.1.0') # replace with your current kivy version !

class MainGrid(GridLayout):
    #Initialize infinite keywords: **kwargs
    def __init__(self, **kwargs):
        #Calling the grid constructor
        super(MainGrid, self).__init__(**kwargs)
        #Setting collums
        self.cols = 4
        #Adding widgets
        main.sqlOpen()
        global member 
        member = main.listAllMembers()
        c = 0
        
        while c < len(member):
            #Button
            self.id = Button(text=f"{member[c][0]}")
            self.id.bind(on_press=self.press)
            self.add_widget(self.id)
            #self.add_widget(Label(text=f"{member[c][1]}"))
            self.lastName = TextInput(text=f"{member[c][1]}", multiline=False)
            self.add_widget(self.lastName)
            self.name = TextInput(text=f"{member[c][2]}", multiline=False)
            self.add_widget(self.name)
            self.add_widget(Label(text=f"{member[c][3]}"))
            c += 1
    def press(self,instance):
        id = instance.text
        print(f"rowId = {id}")
        
class SacramentalAttendance(App):
        def build(self):
            return MainGrid()

    
    
if __name__ == '__main__':
    SacramentalAttendance().run()