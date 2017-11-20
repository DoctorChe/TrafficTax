import kivy

kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class TrafGridLayout(GridLayout):
    # Function called when equals is pressed
    def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"


class TrafficTaxApp(App):
    def build(self):
        return TrafGridLayout()


trafApp = TrafficTaxApp()
trafApp.run()
