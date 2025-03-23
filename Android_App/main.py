from requests import get
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

def responce(status_code, btn):
    if status_code == 200:
        return f"Toggle {btn}"
    elif status_code == 404:
        return f"Server is down"

class Home(MDScreen):
    def toggel_led(self, btn):
        tunnles = "starfish-regular-lightly.ngrok-free.app"
        rout = btn.text.replace(" ", "_").lower()
        resp = get(f"http://{tunnles}/room1/{rout}")
        self.ids.resp.text = f"{responce(resp.status_code, btn.text)}"

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
