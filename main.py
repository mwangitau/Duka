from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        self.email = TextInput(hint_text='Email', multiline=False)
        self.password = TextInput(hint_text='Password', multiline=False, password=True)
        self.login_btn = Button(text='Login', on_press=self.login)
        layout.add_widget(self.email)
        layout.add_widget(self.password)
        layout.add_widget(self.login_btn)
        self.add_widget(layout)
    
    def login(self, instance):
        print(f'Logging in with {self.email.text} and {self.password.text}')

class StoreListScreen(Screen):
    def __init__(self, **kwargs):
        super(StoreListScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Stores Near You'))
        store_list = ['Store 1', 'Store 2', 'Store 3']
        rv = RecycleView()
        rv.data = [{'text': store} for store in store_list]
        layout.add_widget(rv)
        self.add_widget(layout)

class Duka(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(StoreListScreen(name='store_list'))
        return sm

if __name__ == '__main__':
    Duka().run()

