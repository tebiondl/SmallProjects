from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from word_list_screen import WordListScreen
from add_word_screen import AddWordScreen
from word_info_screen import WordDetailsScreen

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        # Main screen (List of words)
        word_list_screen = WordListScreen(name='word_list')
        sm.add_widget(word_list_screen)

        # Add word screen
        add_word_screen = AddWordScreen(name='add_word')
        sm.add_widget(add_word_screen)

        # Word details screen
        word_details_screen = WordDetailsScreen(name='word_details')
        sm.add_widget(word_details_screen)

        return sm

if __name__ == '__main__':
    MainApp().run()
