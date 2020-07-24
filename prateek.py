
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainApp(App):
    
    def build(self):
      

        button=Button(text='add Button',font_size='10sp',size_hint=(.1,.1),pos=(300,250))
        return button


        

if __name__=='__main__':
    MainApp().run()
