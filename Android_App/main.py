from kivymd.app import MDApp
from kivy.lang import Builder
import paho.mqtt.client as mqtt
from kivymd.uix.screen import MDScreen

client = mqtt.Client()
client.connect("test.mosquitto.org")

class Home(MDScreen):
    def toggel_led(self, btn):
        # This function is called when a button is pressed
        btn = btn.text.replace(" ", "_").lower()
        client.publish("fromPhone", f"toggle{btn}")

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
