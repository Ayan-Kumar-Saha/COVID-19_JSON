from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from parsers.parser import controller


data = dict()

class InputWindow(Screen):
    date_to_fetch = ObjectProperty(None)
    state_code = ObjectProperty(None)

    def fetch_data(self):
        global data
        data = controller(self.date_to_fetch.text, self.state_code.text)
        self.reset()
        print(data)

    def reset(self):
        self.date_to_fetch.text = ''
        self.state_code.text = ''


class OutputWindow(Screen):
    confirmed = ObjectProperty(None)
    recovered = ObjectProperty(None)
    deceased = ObjectProperty(None)

    def on_enter(self, *args):
        global data
        self.confirmed.text = str(data['Confirmed'])
        self.recovered.text = str(data['Recovered'])
        self.deceased.text = str(data['Deceased'])


class WindowManager(ScreenManager):
    pass


class CovidApp(App):
    def build(self):
        return WindowManager()


if __name__ == "__main__":
    CovidApp().run()

