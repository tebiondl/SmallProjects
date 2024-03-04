from kivymd.uix.screen import Screen
from dataHandler import *
from kivymd.uix.list import OneLineListItem

class ActiveGame(Screen):
    
    actual_game = {}
    
    def load_game_details(self, actual_game):
        self.actual_game = actual_game
        self.ids.actualPlayerList.clear_widgets()
        
        for player in self.actual_game["players"]:
            item = OneLineListItem(text=player["name"])
            item.actualPlayer = player
            item.bind(on_release=self.item_clicked)
            self.ids.actualPlayerList.add_widget(item)   
            
    def item_clicked(self, instance):
        actual_player = instance.actualPlayer
        game_details_screen = self.manager.get_screen("playerInfo")
        game_details_screen.load_game_details(actual_player, self.actual_game)
        self.manager.current = "playerInfo"