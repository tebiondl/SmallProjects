from kivymd.uix.screen import Screen
from dataHandler import *
from extras import DeleteListItem

class OfflineStart(Screen):
    def on_enter(self, *args):
        self.ids.gamelist.clear_widgets()
        games = load_data(0)["games"]
        for game in games:
            item = DeleteListItem(text=game["name"], delete_callback=self.remove_item)
            item.bind(on_release=self.item_clicked)
            item.actualGame = game
            self.ids.gamelist.add_widget(item)

    def remove_item(self, instance):
        ## Make a dialog to ask if you are sure
        list_item = instance.parent
        self.ids.gamelist.remove_widget(list_item)
        #Remove from json also
        games = load_data(0)
        games["games"].remove(list_item.actualGame)
        save_data(0, games)
        
            
    def item_clicked(self, instance):
        actual_game = instance.actualGame
        game_details_screen = self.manager.get_screen("activeGame")
        game_details_screen.load_game_details(actual_game)
        self.manager.current = "activeGame"