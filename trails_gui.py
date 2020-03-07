import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class TrailsApp(App):
    def build(self):
        return TrailsView()

# Has search bar, search button, and search results for anagrams
class TrailsView(BoxLayout):
    pass

# Each of the search results as an individual widget
class TrailsResult(Widget):
    pass

if __name__ == '__main__':
    TrailsApp().run()