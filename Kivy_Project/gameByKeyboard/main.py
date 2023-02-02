from kivy.app import App

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

def collides(rect1, rect2): 
  rect1x = rect1[0][0] ; rect2x = rect2[0][0]
  rect1y = rect1[0][1] ; rect2y = rect2[0][1]
  
  rect1w = rect1[1][0] ; rect2w = rect2[1][0]
  rect1h = rect1[1][1] ; rect2h = rect2[1][1]
  
  if (
    rect1x < rect2x + rect2w and
    rect1x + rect1w > rect2x and
    rect1y < rect2y + rect2h and
    rect1y + rect1h > rect2y
  ):
    return True
  else: 
    return False
  

class GameWidget(Widget):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    
    
    self.sound = SoundLoader.load('JaiGaeRay.mp3')
    self.sound.play()
    self.sound.loop = True

    
    self._keyboard = Window.request_keyboard(
      self._on_keyboard_closed, self
    )
    self._keyboard.bind(on_key_down=self._on_key_down)
    self._keyboard.bind(on_key_up=self._on_key_up)
    
    
    self.pressed_keys = set()
    Clock.schedule_interval(self.move_step, 0)
    
    
    with self.canvas:
      self.hero = Rectangle(
        source='PeeToo.png', pos=(250, 250), size=(100, 100)
      )
      self.enemy = Rectangle(
        source='PeeLarm.png', pos=(450, 250), size=(100, 100)
      )
        
        
  def _on_keyboard_closed(self):
    self._keyboard.unbind(on_key_down=self._on_key_down)
    self._keyboard.unbind(on_key_up=self._on_key_up)
    self._keyboard = None
      
      
  def _on_key_down(self, keyboard, keycode, text, modifiers):
    print('down', text)
    self.pressed_keys.add(text)
 
 
  def _on_key_up(self, keyboard, keycode):
    text = keycode[1]
    print('up', text)

    if text in self.pressed_keys:
      self.pressed_keys.remove(text)
      
      
  def move_step(self, dt):
    h_cur_x = self.hero.pos[0] ; e_cur_x = self.enemy.pos[0]
    h_cur_y = self.hero.pos[1] ; e_cur_y = self.enemy.pos[1]
    
    step = 500 * dt
    
    if 'w' in self.pressed_keys:
      h_cur_y += step
    if 's' in self.pressed_keys:
      h_cur_y -= step
    if 'a' in self.pressed_keys:
      h_cur_x -= step
    if 'd' in self.pressed_keys:
      h_cur_x += step
      
    if 'o' in self.pressed_keys:
      e_cur_y += step
    if 'l' in self.pressed_keys:
      e_cur_y -= step
    if 'k' in self.pressed_keys:
      e_cur_x -= step
    if ';' in self.pressed_keys:
      e_cur_x += step

    self.hero.pos = (h_cur_x, h_cur_y)
    self.enemy.pos = (e_cur_x, e_cur_y)
    
    if collides(
      (self.hero.pos, self.hero.size),
      (self.enemy.pos, self.enemy.size)
    ):
      print("colliding!")
    else:
      print("not colliding!")

      
class MyApp(App):
  def build(self):
    return GameWidget()

if __name__ == '__main__':
  app = MyApp()
  app.run()
