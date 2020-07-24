from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang.builder import Builder
from kivymd.uix.button import MDRectangleFlatButton,MDFlatButton
from kivymd.uix.dialog import MDDialog

username_help =""" 
MDTextField: 
    hint_text:"Enetr Your Username"
    helper_text:"or Click this if you forgot details"
    helper_text_mode:"on_focus"
    icon_right:"google"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:300


"""
class DemoApp(MDApp):
    

    def build(self):
        screen=Screen()
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.primary_hue='A400'
        self.theme_cls.theme_style='Dark'
        self.username= Builder.load_string(username_help)
        btt=MDRectangleFlatButton(text='Enter',pos_hint={'center_x':0.5,'center_y':0.4},on_release=self.showdata)
        screen.add_widget(self.username)
        screen.add_widget(btt)
        return screen

    def showdata(self, obj):

        if self.username.text is "":
            check_string="Please Enter The Username"
        else:
            check_string=self.username.text

        close_button=MDFlatButton(text="Close",on_release= self.close_d)

        more=MDFlatButton(text="More")

        self.dialog = MDDialog(text=check_string,title="UserName",buttons=[close_button,more],size_hint_x=0.5,width=0.5)
        
        self.dialog.open()

    def close_d(self,obj):
        self.dialog.dismiss()

        
DemoApp().run()



    