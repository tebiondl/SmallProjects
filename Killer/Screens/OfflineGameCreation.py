from kivymd.uix.screen import Screen
from dataHandler import *
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from extras import DeleteListItem

class OfflineGameCreation(Screen):
    newPlayers = []
    newWeapons = []
    newPlaces = []
    gameName = "GameX"
    
    def on_enter(self, *args):
        self.newPlayers = []
        self.newWeapons = []
        self.newPlaces = []
        self.gameName = "GameX"
        
        #Create examples
        for i in range(5):
            p_item = DeleteListItem(text=f"Persona: Player{str(i)}", delete_callback=self.remove_item)
            p_item.actualText = f"Player{str(i)}"
            p_item.typeName = "Player"
            self.ids.playerList.add_widget(p_item)
            self.newPlayers.append(f"Player{str(i)}")
            p_item = DeleteListItem(text=f"Arma: Weapon{str(i)}", delete_callback=self.remove_item)
            p_item.actualText = f"Weapon{str(i)}"
            p_item.typeName = "Weapon"
            self.ids.weaponList.add_widget(p_item)
            self.newWeapons.append(f"Weapon{str(i)}")
            p_item = DeleteListItem(text=f"Lugar: Place{str(i)}", delete_callback=self.remove_item)
            p_item.actualText = f"Place{str(i)}"
            p_item.typeName = "Place"
            self.ids.placeList.add_widget(p_item)
            self.newPlaces.append(f"Place{str(i)}")
        
    def open_next_dialog(self):
        self.dialog = MDDialog(
            title=f"Enter a name for the Game",
            type="custom",
            content_cls=MDTextField(),
            buttons=[
                MDRectangleFlatButton(
                    text="Cancel",
                    on_release=self.close_dialog
                ),
                MDRectangleFlatButton(
                    text="Continue",
                    on_release=self.get_input_text_next
                )
            ]
        )
        
        self.dialog.open()
    
    def open_dialog(self, name):
        self.saveName = name
        self.dialog = MDDialog(
            title=f"Add {name}",
            type="custom",
            content_cls=MDTextField(),
            buttons=[
                MDRectangleFlatButton(
                    text="Cancel",
                    on_release=self.close_dialog
                ),
                MDRectangleFlatButton(
                    text="Continue",
                    on_release=self.get_input_text
                )
            ]
        )
        
        self.dialog.open()
    
    def close_dialog(self, *args):
        self.dialog.dismiss()
    
    def get_input_text_next(self, *args):
        text = self.dialog.content_cls.text
        self.gameName = text
        self.dialog.dismiss()
        #Move to shuffle screen
        self.manager.current = "startGame"
        
    def get_input_text(self, *args):
        text = self.dialog.content_cls.text
        self.add_element(text)
        self.dialog.dismiss()
        
    def add_element(self, text):
        item = DeleteListItem(text=f"{self.saveName}: "+text, delete_callback=self.remove_item)
        item.typeName = self.saveName
        item.actualText = text.strip()
        if self.saveName == "Player":
            self.newPlayers.append(text.strip())
            self.ids.playerList.add_widget(item)
        elif self.saveName == "Weapon":
            self.newWeapons.append(text.strip())
            self.ids.weaponList.add_widget(item)
        elif self.saveName == "Place":
            self.newPlaces.append(text.strip())
            self.ids.placeList.add_widget(item)
    
    def remove_item(self, instance):
        ## Make a dialog to ask if you are sure
        list_item = instance.parent
        list_parent = list_item.parent
        
        if list_item.typeName == "Player":
            self.newPlayers.remove(list_item.actualText)
        elif list_item.typeName == "Weapon":
            self.newWeapons.append(list_item.actualText)
        elif list_item.typeName == "Place":
            self.newPlaces.append(list_item.actualText)
            
        list_parent.remove_widget(list_item)