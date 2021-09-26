from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root


class ButtonEventDemo(App):
    def handle_greet(self):
        self.title = "Greet"
        self.root.ids.output_label.text = " Hello " + self.root.ids.input_name.text
        return self.root


class ButtonEventDemo(App):
    def output_label(self):
        self.title = ''
        self.root = Builder.load_file('box_layout.kv')
        return self.root


class ButtonEventDemo(App):
    def reset_label(self):
        self.tile = "Clear text and output"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

        def press_button(self):
        print("Greet")

    BoxLayoutDemo().run()
