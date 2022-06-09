#import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy_garden.contextmenu

kv = Builder.load_file("application_menu.kv")

class MyApp(App):
    def build(self):
        self.title = 'comercio'
        return kv

    # def say_hello(self, text):
    #     print(text)
    #     self.root.ids['app_menu'].close_all()

if __name__ == '__main__':
    MyApp().run()