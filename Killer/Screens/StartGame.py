from kivymd.uix.screen import Screen
from kivymd.uix.label import MDLabel
from dataHandler import *
import random
import uuid

class StartGame(Screen):
    def on_enter(self):
        offline_screen = self.manager.get_screen('offlineGameCreation')
        self.players = offline_screen.newPlayers
        self.weapons = offline_screen.newWeapons
        self.places = offline_screen.newPlaces
        self.gameName = offline_screen.gameName
        
        if len(self.players) == 0:
            self.players.append("El Épico")
        if len(self.weapons) == 0:
            self.weapons.append("Hat")
        if len(self.places) == 0:
            self.places.append("Kitchen")
        
    def shuffle(self):
        #shuffle and save the game
        print("Shuffled started")
        random.shuffle(self.players)
        random.shuffle(self.weapons)
        random.shuffle(self.places)
        
        jsonToSave = {
            "name": self.gameName,
            "players" : []
        }
        
        weaponCounter = 0
        placeCounter = 0
        for i in range(len(self.players)):
            if placeCounter == len(self.places):
                placeCounter = 0
            if weaponCounter == len(self.weapons):
                weaponCounter = 0
            
            player = {
                "name": self.players[i],
                "weapon": self.weapons[weaponCounter],
                "place": self.places[placeCounter]
            }
            
            if i < len(self.players) - 1:
                player["victim"] = self.players[i+1]
            else:
                player["victim"] = self.players[0]
            
            placeCounter += 1
            weaponCounter += 1
            jsonToSave["players"].append(player)
        
        self.actualPlayers = jsonToSave["players"]
        print(self.actualPlayers)
        
        jsonToSave["id"] = "1"+str(uuid.uuid4())
        games = load_data(0)
        games["games"].append(jsonToSave)
        save_data(0, games)
        
        self.ids.shuffleBtn.opacity = 0
        self.ids.shuffleBtn.disabled = True
        self.ids.showInfoBtn.opacity = 1
        self.ids.showInfoBtn.disabled = False
        self.ids.playerMessage.opacity = 1
        self.ids.hideInfoBtn.disabled = False
        
        self.ids.playerMessage.text = self.ids.playerMessage.text + self.actualPlayers[0]["name"]
        
        container = self.ids.infoContainer
        self.playerLabel = MDLabel(text='[PLAYER]', pos_hint={'center_x': 1, 'center_y': 0.5}, theme_text_color='Secondary')
        container.add_widget(self.playerLabel)
        self.victimLabel = MDLabel(text='[VICTIM]', pos_hint={'center_x': 1, 'center_y': 0.4}, theme_text_color='Secondary')
        container.add_widget(self.victimLabel)
        self.weaponLabel = MDLabel(text='[WEAPON]', pos_hint={'center_x': 1, 'center_y': 0.3}, theme_text_color='Secondary')
        container.add_widget(self.weaponLabel)
        self.placeLabel = MDLabel(text='[PLACE]', pos_hint={'center_x': 1, 'center_y': 0.2}, theme_text_color='Secondary')
        container.add_widget(self.placeLabel)
        
        
    def show_victims(self):
        
        if len(self.actualPlayers) > 0:
            self.playerLabel.text = "You are: " + self.actualPlayers[0]["name"]
            self.victimLabel.text = "You kill: " + self.actualPlayers[0]["victim"]
            self.weaponLabel.text = "With: " + self.actualPlayers[0]["weapon"]
            self.placeLabel.text = "In: " + self.actualPlayers[0]["place"]
            
            self.actualPlayers.pop(0)
            if len(self.actualPlayers) > 0:
                self.ids.playerMessage.text = "Hide the info and give the phone to: " + self.actualPlayers[0]["name"]
                self.ids.hideInfoBtn.opacity = 1
                self.ids.hideInfoBtn.disabled = False
                self.ids.showInfoBtn.opacity = 0
                self.ids.showInfoBtn.disabled = True
                print(self.ids.showInfoBtn.disabled)
                print(self.ids.hideInfoBtn.disabled)
            else:
                self.ids.playerMessage.text = "End the shuffle"
                self.ids.showInfoBtn.text = "Finish"
        else:
            container = self.ids.infoContainer
            container.remove_widget(self.playerLabel)
            container.remove_widget(self.victimLabel)
            container.remove_widget(self.weaponLabel)
            container.remove_widget(self.placeLabel)
            
            self.ids.playerMessage.text = ""
            self.ids.showInfoBtn.opacity = 0
            self.ids.showInfoBtn.disabled = True
            self.ids.showInfoBtn.text = "Show Information"
            self.ids.hideInfoBtn.opacity = 0
            self.ids.hideInfoBtn.disabled = True
            self.ids.playerMessage.opacity = 0
            self.ids.shuffleBtn.opacity = 1
            self.ids.shuffleBtn.disabled = False
            self.manager.current = "offline"
    
    def hide_victims(self):
        self.playerLabel.text = "[PLAYER]"
        self.victimLabel.text = "[VICTIM]"
        self.weaponLabel.text = "[WEAPON]"
        self.placeLabel.text = "[PLACE]"
        
        self.ids.hideInfoBtn.opacity = 0
        self.ids.hideInfoBtn.disabled = True
        self.ids.showInfoBtn.opacity = 1
        self.ids.showInfoBtn.disabled = False