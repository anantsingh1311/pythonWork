# Polymorphism:Many forms
from abc import ABC,abstractmethod

class ControlUI(ABC):

    @abstractmethod
    def draw(self):
        pass

class Dropdown(ControlUI):
    def draw(self):
        print("Draw Dropdown")

class TextBox(ControlUI):
    def draw(self):
        print("Draw Textbox")


def draw(controls):
    # for control in controls:
    controls.draw()

textBox = TextBox()

# ddl.draw()

ddl = Dropdown();

# ddl2.draw()

# draw([ddl,textBox])

# draw([ddl,textBox])