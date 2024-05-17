from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        # Create a button instance
        btn = Button(text='Click me')

        # Bind the button's on_press event to the callback function
        btn.bind(on_press=self.on_button_click)

        return btn

    def on_button_click(self, instance):
        print("clicked")

if __name__ == '__main__':
    MyApp().run()