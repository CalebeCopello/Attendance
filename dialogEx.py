#kivy imports
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

import main

kivy.require('2.1.0') # replace with your current kivy version !

class Grid(GridLayout):
    #Initialize infinite keywords: **kwargs
    def __init__(self, **kwargs):
        #Calling the grid constructor
        super(Grid, self).__init__(**kwargs)
        #Setting collums
        self.cols = 1
        #Creating Grids
        self.headerGrid = GridLayout()
        self.headerGrid.cols = 4
        self.mainGrid = GridLayout()
        self.mainGrid.cols = 4
        self.footerGrid = GridLayout()
        self.footerGrid.cols = 3
        #Adding widgets
        #header
        self.mainGrid.add_widget(Label(text="ID"))
        self.mainGrid.add_widget(Label(text="Sobrenome"))
        self.mainGrid.add_widget(Label(text="Nome"))
        self.mainGrid.add_widget(Label(text="Presença"))
        #main
        main.sqlOpen()
        global member 
        member = main.listAllMembers()
        c = 0
        while c < len(member):
            self.mainGrid.add_widget(Label(text=f"{member[c][0]}"))
            self.mainGrid.add_widget(Label(text=f"{member[c][1]}"))
            self.mainGrid.add_widget(Label(text=f"{member[c][2]}"))
            self.mainGrid.add_widget(Label(text=f"{member[c][3]}"))
            c += 1
        #footer
        self.footerGrid.add_widget(Button(text="Voltar"))
        self.footerGrid.add_widget(Button(text="Confirmar"))
        #self.add_widget(self.headerGrid)
        self.add_widget(self.mainGrid)
        self.add_widget(self.footerGrid)
        
class SacramentalAttendance(App):
        def build(self):
            return Grid()

    
    
if __name__ == '__main__':
    SacramentalAttendance().run()