from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.lang import Builder
import helpers as MyHelpers
from dataHandler import *

from Screens.MenuScreen import MenuScreen
from Screens.OfflineStart import OfflineStart
from Screens.OfflineGameCreation import OfflineGameCreation
from Screens.StartGame import StartGame
from Screens.ActiveGame import ActiveGame
from Screens.PlayerInfo import PlayerInfo

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(OfflineStart(name='offline'))
sm.add_widget(OfflineGameCreation(name='offlineGameCreation'))
sm.add_widget(StartGame(name='startGame'))
sm.add_widget(ActiveGame(name='activeGame'))
sm.add_widget(PlayerInfo(name='playeInfo'))

class DemoApp(MDApp):
    
    def build(self):
        screen = Builder.load_string(MyHelpers.screen_helper)
        return screen
    
    def on_start(self):
        print("Started")
    
DemoApp().run()