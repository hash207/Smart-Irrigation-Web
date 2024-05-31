from requests import get, ConnectTimeout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

class Home(MDScreen):
    def toggel_led(self, btn):
        tunnles = "starfish-regular-lightly.ngrok-free.app"
        try:
            rout = btn.text.replace(" ", "").upper()
            get(f"http://{tunnles}/room1/{rout}")
        except ConnectTimeout:
            self.ids.resp.text = "Connection Timeout"

class main_app(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        return Builder.load_file("design.kv")

    def toggle_theme_style(self, instance):
        if self.theme_cls.theme_style == "Dark":
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.theme_style = "Dark"

if __name__ == "__main__":
    main_app().run()
