

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class ListNames (App):
    status_text = StringProperty

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.list_of_names = []

    def build(self):
        self.title = "Dynamic labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        self.status_text = ''
        """
        Create buttons from list of objects and add them to the GUI.
        :return: None
        """