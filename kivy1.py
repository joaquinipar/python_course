import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
	def build(self):
		return Label (text="Hola")

if __name__ == "  main  ":
	MyApp().run()
