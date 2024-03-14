# Game class with game control, collision mechanics, game drawing methodes

from PIL import Image, ImageDraw, ImageFont
import random
import keyboard
import time


PLAYER_SIZE = (10, 100)
BALL_SIZE = 12
PLAYER_SPEED = 8
DIRECTION = [-1, 1]

class Game:
    def __init__(self, screen_size = (800, 500), ball_speed=10, max_ball_speed = 16):
        self.screen_size = screen_size
        self.player_one_x = PLAYER_SIZE[0] // 2
        self.player_one_y = self.screen_size[1] // 2
        self.player_two_x = self.screen_size[0] - PLAYER_SIZE[0] // 2
        self.player_two_y = self.screen_size[1] // 2
        self.ball_possition_x = self.screen_size[0] // 2
        self.ball_possition_y = random.randint(0, self.screen_size[1])
        self.player_one_score = 0
        self.player_two_score = 0
        self.ball_speed = ball_speed
        self.ball_move_x = random.choice(DIRECTION) * self.ball_speed
        self.ball_move_y = random.choice(DIRECTION) * self.ball_speed
        self.max_ball_speed = max_ball_speed
        self.paused = True
        self.computer_control = True
        self.number_of_games = 0
        self.hits_counter = 0
        self.steps_counter = 0
              
    def player_one_move(self):
        if (keyboard.is_pressed('z') and self.player_one_y + 
            PLAYER_SIZE[1] // 2 < self.screen_size[1]):
            self.player_one_y += PLAYER_SPEED
        if keyboard.is_pressed('a') and self.player_one_y - PLAYER_SIZE[1] // 2 > 0:
            self.player_one_y -= PLAYER_SPEED
        
    def player_two_move(self):
        if (keyboard.is_pressed('down') and self.player_two_y + 
            PLAYER_SIZE[1] // 2 < self.screen_size[1]):
            self.player_two_y += PLAYER_SPEED
        if keyboard.is_pressed('up') and self.player_two_y - PLAYER_SIZE[1] // 2 > 0:
            self.player_two_y -= PLAYER_SPEED
    
    def ball_move(self):
        self.ball_possition_x += self.ball_move_x
        self.ball_possition_y += self.ball_move_y
        
    # primitive computer control of player two - follow a ball
    def computer(self):
        dist_player_two_ball = abs(self.player_one_y - self.ball_possition_y)           
        if (dist_player_two_ball > 4 and self.player_two_y > self.ball_possition_y and
            self.player_two_y - PLAYER_SIZE[1] // 2 > 0):
            self.player_two_y -= PLAYER_SPEED
        if (dist_player_two_ball > 4 and self.player_two_y < self.ball_possition_y and
            self.player_two_y + PLAYER_SIZE[1] // 2 < self.screen_size[1]):
            self.player_two_y += PLAYER_SPEED
    
    def game_draw(self):
        img = Image.new(mode='RGB', size=self.screen_size, color=(50, 50, 50))
        self.draw = ImageDraw.Draw(img)
        self.draw.line((self.screen_size[0] // 2,
                        0,
                        self.screen_size[0] // 2,
                        self.screen_size[1]),
                       fill=(70, 70, 70))
        self.draw.rectangle((self.player_one_x - PLAYER_SIZE[0] // 2,
                             self.player_one_y - PLAYER_SIZE[1] // 2, 
                             self.player_one_x + PLAYER_SIZE[0] // 2, 
                             self.player_one_y + PLAYER_SIZE[1] // 2), 
                            fill=(255, 0, 0)) # player_one
        self.draw.rectangle((self.player_two_x - PLAYER_SIZE[0] // 2, 
                             self.player_two_y - PLAYER_SIZE[1] // 2, 
                             self.player_two_x + PLAYER_SIZE[0] // 2, 
                             self.player_two_y + PLAYER_SIZE[1] // 2), 
                            fill=(0, 0, 255)) # player_two
        self.draw.ellipse([self.ball_possition_x - BALL_SIZE // 2, 
                           self.ball_possition_y - BALL_SIZE // 2, 
                           self.ball_possition_x + BALL_SIZE // 2, 
                           self.ball_possition_y + BALL_SIZE //2], 
                          fill=(255, 255, 255)) # ball
        draw_legend = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 15)
        legend = (f'Number of games: {self.number_of_games}\n'
        f'Number of hits: {self.hits_counter}\n'
        f'Steps: {self.steps_counter}\n'
        f'Ball possition {int(self.ball_possition_x), int(self.ball_possition_y)}\n'
        f'Player one score: {self.player_one_score}, Player two score: {self.player_two_score}')
        self.draw.text((10, 20),
                       text=str(legend),
                       font=draw_legend,
                       fill=(100, 100, 100),
                       align='left')
        if self.paused:
            draw_text = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 25)
            message = (f'Press SPACE to start the game')
            self.draw.text((self.screen_size[0]//2 - 170, self.screen_size[1]//2),
                        text=str(message),
                        font=draw_text,
                        fill=(100, 100, 100),
                        align='center')
        return img
    
    def collision_check(self):
        # collisions with game wall's in x direction
        if self.ball_possition_x + BALL_SIZE // 2 <= 0:
            self.ball_move_x = random.choice(DIRECTION) * self.ball_speed
            self.ball_move_y = random.choice(DIRECTION) * self.ball_speed
            self.player_two_score += 1
            self.ball_possition_x = self.screen_size[0] // 2
            self.ball_possition_y = random.randint(0, self.screen_size[1])
            self.number_of_games += 1
        if self.ball_possition_x - BALL_SIZE // 2 >= self.screen_size[0]:
            self.player_one_score += 1
            self.ball_move_x = random.choice(DIRECTION) * self.ball_speed
            self.ball_move_y = random.choice(DIRECTION) * self.ball_speed
            self.ball_possition_x = self.screen_size[0] // 2
            self.ball_possition_y = random.randint(
                BALL_SIZE // 2, 
                self.screen_size[1] - BALL_SIZE // 2)
            self.number_of_games += 1
        # collisions with game wall's in y direction
        if self.ball_possition_y <= BALL_SIZE // 2:
            self.ball_possition_y = BALL_SIZE // 2
            self.ball_move_y = (-1) * self.ball_move_y
        if self.ball_possition_y >= self.screen_size[1] - BALL_SIZE // 2:
            self.ball_possition_y = self.screen_size[1] - BALL_SIZE // 2
            self.ball_move_y = (-1) * self.ball_move_y
        # ball <-> players collisions
        if (self.ball_possition_x <= self.player_one_x + 
            PLAYER_SIZE[0] // 2 + BALL_SIZE // 2 and 
            (self.ball_possition_y > self.player_one_y - 
             PLAYER_SIZE[1] // 2 - BALL_SIZE and 
             self.ball_possition_y <= self.player_one_y + 
             PLAYER_SIZE[1] // 2 + BALL_SIZE)):
            self.ball_move_x = (-1) * self.ball_move_x
            # ball speedup after collision
            difference_in_y = self.player_one_y - self.ball_possition_y
            reduction_factor = (PLAYER_SIZE[1] // 2) // self.max_ball_speed
            self.ball_move_y = difference_in_y // reduction_factor
            self.ball_move_y = (-1) * self.ball_move_y
            self.hits_counter += 1
        if (self.ball_possition_x > self.player_two_x - 
            PLAYER_SIZE[0] // 2 - BALL_SIZE // 2 and 
            (self.ball_possition_y >= self.player_two_y - 
             PLAYER_SIZE[1] // 2 - BALL_SIZE and
             self.ball_possition_y <= self.player_two_y + 
             PLAYER_SIZE[1] // 2 + BALL_SIZE)):
            self.ball_move_x = (-1) * self.ball_move_x
            # ball speedup after collision
            difference_in_y = self.player_two_y - self.ball_possition_y
            reduction_factor = (PLAYER_SIZE[1] // 2) // self.max_ball_speed
            self.ball_move_y = difference_in_y // reduction_factor
            self.ball_move_y = (-1) * self.ball_move_y
            self.hits_counter += 1
    
    def pause_game(self):
        if keyboard.is_pressed('space') and self.paused == True:
            self.paused = False
            time.sleep(0.13)
        elif keyboard.is_pressed('space') and self.paused == False:
            self.paused = True
            time.sleep(0.13)
            
    def loop(self):
        if self.paused == False:
            self.player_one_move()
            # self.player_two_move()
            self.computer()
            self.collision_check()
            self.ball_move()
            
        
            
        

        
            
            
        
        



