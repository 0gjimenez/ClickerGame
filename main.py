from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
formatting = """
<MyScreenManager>:
    StartScreen:
    CreateNewCharacterScreen
    MainGameScreen:
    
<StartScreen>:
    name: 'start'
    BoxLayout:
        orientation: 'vertical'
        Label:
            color: [1,0,0,1]
            text: root.instructions
            font_size: 40
        TextInput:
            id: save_code
            font_size: 28
        Button:
            Text: 'Press me to go to the Game Screen'
            on_press: root.load_or_start_new(save_code.text)

<CreateNewCharacterScreen>:
    name: 'character'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: instr
            size: self.texture_size
            text: root.instructions
        TextInput:
            id: name
            font_size: 28
        Button:
            text: 'Enter a nam for your character'
            on_press: root.create_character(name.text)
<MainGameScreen>:
    name: 'game'
    BoxLayout:
        orientation: 'vertical'
        Label:
            id: display
            text: root.display
        BoxLayout:
            Button:
                text: 'blank'
                on_press: root.blank()
                on_press: root.add_time()
            Button:
                Text: 'blank'
                on_press: root.blank()
                on_press: root.add_time()                        
"""
Builder.load_string(formatting)

class PlayerStatistics:
    def __init__(self, blank=0, blank=0, time=0):
        self.time: int = time
        self.name: str = ""
        self.blank: int = blank
        self.blank: int = blank
        self.attributeDict = {"BLK": self.blank , "BLA": self.blank}
    def create_from_save(self):
        pass
    def __set_name__(self, username):
        self.name = username
    def increment_blank(self, amount=1):
        self.blank = self.blank + amount
    def increment(self, parameter,amount=1):
        if self.attributeDict.__contains__(parameter):
            self.attributeDict[parameter] = self.attributeDict[parameter] + amount
        else:
            print("That Parameter does not exist")
    def increment_blank(self, amount=1):
        self.blank = self.blank + amount
        pass
    def __str__(self):
        return str("Name:" +self.name + "" + "|" + "time" + str(self.time) + "\n" + "blank: " + str(self.blank) +
                   "\n" + "blank2: " + str(self.blank))
    def increment_time(self, amount=1):
        self.time = self.time + amount
        pass
#Create the screen manager = sm
class MyScreenManager(ScreenManager, Widget):
    data = ObjectProperty(PlayerStatistics)

class StartScreen(Screen):
    instructions = StringProperty(str('''
    Welcome to this fun game!
    If you're new to the game or you want to start from the beginning just press the button!
    Otherwise, first paste in your save code, and then press the button to load the game.
    '''))
    def load_or_start_new(self, savedata=''):
        # For now we always start a new game
        if savedata != '':
            self.load_game(savedata)
        else: self.start_new_game()
        pass
#Right now load and now do the same thing, but that might change in the future
    def load_game(self, data):
        self.manager.current = 'character'
        pass
    pass
class CreateNewCharacterScreen(Screen):
    instructions =  StringProperty(str('''
    This world is unlike any world you've known before. Great Things await. But first you'll need a name...
    '''))
    fail_instructions = StringProperty(str('''
    This world is unlike any world you've known before. Great Things await. But first you'll need a name...
    FOOLISH MORTAL!!! ENTER A NAME FIRST BEFORE YOU CLICK THE BUTTON. 
    '''))
    data_stats: PlayerStatistics = ObjectProperty(PlayerStatistics)
    def create_character(self, username):
        if username != '':
            self.data_stats = PlayerStatistics()
            self.data_stats.set_name(username)
            self.manager.get_screen('game').display = str(self.data_stats)
            self.manager.current = 'game'
        else:
            self.instructions = self.fail_instructions
        pass
    pass

class MainGameScreen(Screen):
    def get_data(self) -> PlayerStatistics:
        return self.manager.get_screen('character').data_stats
    display = StringProperty("IF THIS IS SHOWING SOMETHING WENT WRONG")
    #StringProperty("Name: " + "Dummy" + "\n" + "blank: " + str(blank))
    def blank(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_blank(1)
        self.display = str(stats)
    def blank(self):
        stats: PlayerStatistics = self.get_data()
        stats.increment_blank(1)
        self.display = str(stats)
    def add_time(self, amount):
        stats: PlayerStatistics = self.get_data()
        stats.increment_Time(amount)
        self.display = str(stats)
class GUIApp(App):

    def build(self):
        return MyScreenManager()

# Entry point into the game
if __name__ == '__main__':
    GUIApp().run()
