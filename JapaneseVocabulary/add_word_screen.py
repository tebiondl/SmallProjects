from kivy.uix.screenmanager import Screen
from utilities import save_words, load_words

class AddWordScreen(Screen):
    def save_word(self):
        word = self.ids.input_word.text
        romaji = self.ids.input_romaji.text
        hiragana_katakana = self.ids.input_hiragana_katakana.text
        kanji = self.ids.input_kanji.text

        if word:  # Only 'word' field is required
            # Load existing words
            words = load_words()
            # Add the new word
            new_word = {
                'word': word,
                'romaji': romaji,
                'hiragana_katakana': hiragana_katakana,
                'kanji': kanji
            }
            # Empty fields are saved as ''
            words.append(new_word)
            # Save the updated file
            save_words(words)
            # Clear input fields
            self.ids.input_word.text = ''
            self.ids.input_romaji.text = ''
            self.ids.input_hiragana_katakana.text = ''
            self.ids.input_kanji.text = ''
            # Return to the main screen
            self.manager.current = 'word_list'
