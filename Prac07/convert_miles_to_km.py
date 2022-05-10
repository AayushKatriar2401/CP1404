"""
CP1404

GUI to convert miles to kilometers
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_T0_KM = 1.60934


class MilesConverterApp(App):
    """Kivy App for converting miles to kilometers."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle Calculations."""
        print("Handle Calculations")
        miles = self.convert_to_number(text)
        self.update_result(miles)

    def handle_increment(self, text, change):
        print("Handle Increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.txt = str(miles)

    def update_result(self, miles):
        print("update")
        self.output_km = str(miles * MILES_T0_KM)

    @staticmethod
    def convert_to_number(text):
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()
