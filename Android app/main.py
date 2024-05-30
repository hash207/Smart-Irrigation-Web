from requests import get, ConnectTimeout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

main_server = "http://192.168.0.111:5000"

class Home(MDScreen):
    def toggel_led(self, btn):
        ip = self.ids.ip.text
        try:
            rout = btn.text.replace(" ", "").upper()
            get(f"{main_server}/room1/{rout}")
            #self.ids.resp.text = url
        except ConnectTimeout:
            self.ids.resp.text = "Connection Timeout"

class main_app(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file("design.kv")

if __name__ == "__main__":
    main_app().run()
