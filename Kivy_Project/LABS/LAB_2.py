from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
  def build(self):
    b = BoxLayout(orientation='vertical')
    t = TextInput(text='Hello',
                  font_size=150)
    l = Label(font_size=150)
    b.add_widget(t)
    b.add_widget(l)
    t.bind(text=l.setter('text'))
    return b
  
if __name__ == "__main__":
 TutorialApp().run()