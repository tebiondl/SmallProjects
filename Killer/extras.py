
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.button import MDIconButton

class DeleteListItem(OneLineIconListItem):
    def __init__(self, text, delete_callback, **kwargs):
        super(DeleteListItem, self).__init__(**kwargs)
        self.text = text
        self.delete_button = MDIconButton(icon="trash-can-outline", pos_hint={'center_x': 0.9, 'center_y': 0.5})
        self.delete_button.bind(on_release=delete_callback)
        self.add_widget(self.delete_button)