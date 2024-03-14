# game main window build with tkinter package

from pong import Game
from PIL import ImageTk
import tkinter as Tk

class GameWindow(Tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.window_size = '800x510'
        self.game_size=(800,500)
        self.title('Raw_Pong.py')
        self.geometry(self.window_size)
        self.resizable(width=False, height=False)
        
        self.my_game = Game(screen_size=self.game_size, ball_speed=8)
        self.game_image = self.my_game.game_draw()
        
        self.imgtk = ImageTk.PhotoImage(image=self.game_image)
        self.lmain = Tk.Label(master=self, 
                              height=self.game_size[0], 
                              width=self.game_size[1])
        self.lmain.pack(side=Tk.TOP, fill='both')
        self.lmain.configure(image=self.imgtk)
        self.game_loop()
    
    def game_loop(self):
        if self.focus_displayof() != None:
            self.my_game.pause_game()
        self.my_game.loop()
        self.game_image = self.my_game.game_draw()
        self.imgtk = ImageTk.PhotoImage(image=self.game_image)
        self.lmain.imgtk = self.imgtk
        self.lmain.configure(image=self.imgtk)
        self.after(1, self.game_loop)