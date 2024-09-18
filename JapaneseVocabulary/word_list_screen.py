from kivy.uix.screenmanager import Screen
from utilities import load_words

class WordListScreen(Screen):
    def on_pre_enter(self):
        # Clear the list before reloading it
        self.ids.rv_list.data = []
        words = load_words()
        for word in words:
            self.ids.rv_list.data.append({
                'text': word['word'] + " / " + word['hiragana_katakana'],
                'on_press': lambda word=word['word']: self.view_word_details(word)
            })

    def view_word_details(self, word):
        self.manager.get_screen('word_details').show_details(word)
        self.manager.current = 'word_details'
