from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

miles_to_km = 1.60934


class MilesToKilometers(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


def handle_calculate(self, text):
    miles = self.convert_number(text)
    self.update_result(miles)
    print("Calculate")


def new_result(self, miles):
    self.output_km = str(miles * miles_to_km)
    print('Update result')


def invalid_input(self,):
    pass


MilesToKilometers().run()
