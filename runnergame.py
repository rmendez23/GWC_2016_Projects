
import pygame
import random
from cityrunner import *
import cityrunner

class RunnerSprite(pygame.sprite.Sprite):
    def __init__(self, file_name, width, height):
        super().__init__()
        self.image = pygame.image.load(file_name)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        #self.image = pygame.Surface([width,height])
        #self.image.fill(color)
        self.rect=self.image.get_rect()
        self.rect.x = screen_width
    def update(self):
        self.rect.x -=5
        if self.rect.x < 0:
            self.rect.x = SCREEN_WIDTH + 10
            self.rect.y = random.randrange(0,SCREEN_HEIGHT)
            

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("RunnerGame_rmendez")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

cityrunner.init(screen, SCREEN_WIDTH,SCREEN_HEIGHT)
all_sprites_list = pygame.sprite.Group()
good_sprites = pygame.sprite.Group()
bad_sprites = pygame.sprite.Group()
def make_sprites():
    all_sprites_list.add(player)
    for i in range(30):
        blue_block = RunnerSprite(("balloon.png"),20,15)
        blue_block.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH*2)
        blue_block.rect.y = random.randrange(SCREEN_HEIGHT)
        good_sprites.add(blue_block)
        all_sprites_list.add(blue_block)
    for i in range (10):
        red_block = RunnerSprite(("death.png"),20,15)
        red_block.rect.x = random.randrange(SCREEN_WIDTH, SCREEN_WIDTH*2)
        red_block.rect.y = random.randrange(SCREEN_HEIGHT)
        bad_sprites.add(red_block)
        all_sprites_list.add(red_block)
def empty():
    all_sprites_list.empty()
    good_sprites.empty()
    bad_sprites.empty()

done = False
player = RunnerSprite(("warrior.png"),20,15)
FRONT_SCROLLER_COLOR = (245,100,118)   #(0,0,30)
MIDDLE_SCROLLER_COLOR = (68,3,129)      #(30,30,100)
BACK_SCROLLER_COLOR = (255,214,192)      #(50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

make_sprites()

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 5)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 4)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 2)

# -------- Main Program Loop -----------
font = pygame.font.SysFont("Gills Sans", 20, True, False)
score = 0
lives = 3

    
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
	
    # --- Game logic should go here
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BACKGROUND_COLOR)
    pos = pygame.mouse.get_pos()
    blue_blocks_hit_list = pygame.sprite.spritecollide(player, good_sprites, True)
    red_blocks_hit_list = pygame.sprite.spritecollide(player, bad_sprites, True)
    for block in blue_blocks_hit_list:
        score += 1
    for block in red_blocks_hit_list:
        score -= 1
        lives -= 1
    good_sprites.update()
    bad_sprites.update()
    score_text = font.render("Score:" +str(score), True, (255,255,255))
    screen.blit(score_text, [500,50])
    lives_text = font.render("Lives:" +str(lives), True, (255,255,255))
    screen.blit(lives_text, [400,50])

    # --- Drawing code should go here
    player.rect.midright = pos
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()
    all_sprites_list.draw(screen)
    if lives < 1:
        empty()
        GAME_OVER = font.render("loser!", True, (255, 0, 0))
        screen.blit(GAME_OVER, [350,250])
    if score >= 28:
        empty()
        YOU_WON = font.render("You Won!", True, (255,50,5))
        screen.blit(YOU_WON, [350,250])
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
