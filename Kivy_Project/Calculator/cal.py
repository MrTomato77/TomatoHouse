# https://github.com/Ghosteon/kivy-calculator
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Calculator(BoxLayout):
    label = ''
    
    def delete(self, instance):
        self.display.text = instance[:0]
    
    def del1(self, instance):
        self.display.text = instance[:-1]
    
    def calc(self, instance):
        try:
            self.display.text = str(eval(instance))
            self.result.text = str(eval(instance))
        except Exception:
            self.display.text = '0'
            self.result.text = 'ERROR'
        
class CalculatorApp(App):
    trigger = False
    triggerC = False
    triggerD = False
    
    def build(self):
        return Calculator()
        
if __name__ == '__main__':
    CalculatorApp().run()
