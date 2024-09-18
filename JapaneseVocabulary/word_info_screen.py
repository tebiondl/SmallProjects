from kivy.uix.screenmanager import Screen
from utilities import load_words, save_words

class WordDetailsScreen(Screen):
    def show_details(self, word):
        self.current_word = word
        words = load_words()
        for w in words:
            if w['word'] == word:
                self.ids.input_word.text = w['word']
                self.ids.input_romaji.text = w['romaji']
                self.ids.input_hiragana_katakana.text = w['hiragana_katakana']
                self.ids.input_kanji.text = w['kanji']
                break

    def save_changes(self):
        word = self.ids.input_word.text
        romaji = self.ids.input_romaji.text
        hiragana_katakana = self.ids.input_hiragana_katakana.text
        kanji = self.ids.input_kanji.text

        if word:
            words = load_words()
            for i, w in enumerate(words):
                if w['word'] == self.current_word:
                    words[i] = {
                        'word': word,
                        'romaji': romaji,
                        'hiragana_katakana': hiragana_katakana,
                        'kanji': kanji
                    }
                    break
            save_words(words)
            self.manager.current = 'word_list'

    def delete_word(self):
        words = load_words()
        words = [w for w in words if w['word'] != self.current_word]
        save_words(words)
        self.manager.current = 'word_list'
