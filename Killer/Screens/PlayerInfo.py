from kivymd.uix.screen import Screen
from dataHandler import *

class PlayerInfo(Screen):
    actual_player = {}
    actual_game = {}
    
    def load_game_details(self, actual_player, actual_game):
        self.actual_player = actual_player
        self.actual_game = actual_game
        print(actual_player)
        
    def show_info(self):
        self.ids.playerInfoName.text = self.actual_player["name"]
        self.ids.playerInfoVictim.text = self.actual_player["victim"]
        self.ids.playerInfoWeapon.text = self.actual_player["weapon"]
        self.ids.playerInfoPlace.text = self.actual_player["place"]
    
    def back(self):
        self.ids.playerInfoName.text = "[NAME HIDDEN]"
        self.ids.playerInfoVictim.text = "[VICTIM HIDDEN]"
        self.ids.playerInfoWeapon.text = "[WEAPON HIDDEN]"
        self.ids.playerInfoPlace.text = "[PLACE HIDDEN]"
        self.manager.current = "activeGame"