from pong import Game
from PIL import Image, ImageTk
import tkinter as Tk
import keyboard
import time

game_size=(800,500)
numpy_execution = True

window_size = '800x510'
root = Tk.Tk()
root.geometry(window_size)
root.resizable(width=False, height=False)
root.wm_title('Raw Pong')

my_game = Game(screen_size=game_size, ball_speed=8)
game_image = my_game.game_draw()


paused = False
n=0

def game_loop():
    if root.focus_displayof() != None:
        my_game.pause_game()
    if my_game.paused == False:
        my_game.player_one_move()
        my_game.player_two_move()
        my_game.collision_check()
        # my_game.computer()
        my_game.ball_move()
        # my_game.steps_counter += 1
    game_image = my_game.game_draw()
    imgtk = ImageTk.PhotoImage(image=game_image)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    root.after(1, game_loop)

imgtk = ImageTk.PhotoImage(image=game_image)
lmain = Tk.Label(master=root, height=game_size[0], width=game_size[1])
lmain.pack(side=Tk.TOP, fill='both')
lmain.imgtk = imgtk
lmain.configure(image=imgtk)

game_loop()


root.mainloop()

