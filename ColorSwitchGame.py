import pygame
import time
import random
pygame.init() #initiate pygame, the first thing to do
pygame.mixer.init() # initialize mixer for music
display_width = 800
display_height = 600
black = (0,0,0) #red green blue 
white = (255,255,255)
red_ = (213, 0 , 0)
light_blue = (121,134,203)
bright_blue = (197,207,236)
#display
gameDisplay = pygame.display.set_mode((display_width, display_height)) #it takes single argument we use tuple on it for the surface or window we creat

pygame.display.set_caption('Color Switch')#change the title of our window

#time
clock = pygame.time.Clock() # our specific game time
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)  #font of the sys
    text = font.render("Score: " + str(count), True, black) #this will show on out screen
    gameDisplay.blit(text, (0,0)) #we will display it on 0,0 
    
def things(thingx,thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh]) #draw a rectangle
def custom_dialog_box(message):
    box_width = 350
    box_height = 180  # Increased to accommodate two lines
    box_x = (display_width - box_width) // 2
    box_y = (display_height - box_height) // 2

    pygame.draw.rect(gameDisplay, light_blue, (box_x, box_y, box_width, box_height)) # clolor of the box
    pygame.draw.rect(gameDisplay, black, (box_x, box_y, box_width, box_height), 2) #boarder of the box

    font = pygame.font.SysFont('gabriola', 36)
    lines = message.split('\n')  # Split the message into lines

    # Display the first line (Game Over)
    text1 = font.render(lines[0], True, red_)
    text1_rect = text1.get_rect(center=(display_width / 2, box_y + 40))
    gameDisplay.blit(text1, text1_rect)

    # Display the second line (Your score is: X)
    text2 = font.render(lines[1], True, black)
    text2_rect = text2.get_rect(center=(display_width / 2, box_y + 100))  # Adjusted position
    gameDisplay.blit(text2, text2_rect)

    restart_text = font.render("Restart", True, black)
    restart_rect = restart_text.get_rect(center=(box_x + box_width // 4, box_y + box_height - 40))
    pygame.draw.rect(gameDisplay,bright_blue, restart_rect)
    pygame.draw.rect(gameDisplay,black, restart_rect, 1)
    
    gameDisplay.blit(restart_text, restart_rect)

    quit_text = font.render("Quit", True, black)
    quit_rect = quit_text.get_rect(center=(box_x + 3 * box_width // 4, box_y + box_height - 40))
    pygame.draw.rect(gameDisplay, bright_blue, quit_rect)
    pygame.draw.rect(gameDisplay,black, quit_rect, 1)
    gameDisplay.blit(quit_text, quit_rect)
    pygame.mixer.music.pause()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if restart_rect.collidepoint(mouse_x, mouse_y):
                    return "restart"
                elif quit_rect.collidepoint(mouse_x, mouse_y):
                    return "quit"

        clock.tick(5)  # Limit frame rate

def crash(dodged):
    message = 'Game Over\nYour score is: {}'.format(dodged)
    choice = custom_dialog_box(message)
    if choice == "restart":
        car_loop()
    elif choice == "quit":
        pygame.quit()
        quit()

def car_loop():
    pygame.mixer.music.load('Ade Dorze.mp3')
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.9)
    x_change = 0
    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 5
    thing_width = 80
    thing_height = 60
    dodged = 0
    game_exit = False
    colors = [
        (255,0,0),#red
        (255,165,0), #orange
        (255,255,0), #yellow
        (85,115,200), #medium dark blue
        (0,0,255), #blue
        (75,0,130), #indigo
        (148,0,211), #violet
        (216,213,255), #lavender
        (0,255,0), #green
        (33,7,15), #dark brown
        (255,115,198), #pink
        (228,171,139), #peach
        #(100,100,87), #gray
        #(198,127,227), #light purple
        ]
    background_col = [(255, 255, 255),
                      (255,255,204),
                      (204,255,255),
                      (204,204,255),
                      (204,204,255),
                      (150,150,150),
                      (51,153,102),
                      (128,0,128),
                      (0,128,0),
                      (128,0,0),
                      (0,0,128),
                      (51,51,0),
                      (51,51,51)
                      ]
    col_indx_one = 0
    col_indx_two = 0
    background_col_indx = 0
    last_background_col_indx = 0
    while not game_exit:
        col_change = (random.randint(0,255), random.randint(0,255), random.randint(0, 255))
        for event in pygame.event.get(): # list of events that happens
            if event.type == pygame.QUIT: #if they decide to quit
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN: #if someone press keydown
                if event.key == pygame.K_LEFT: #if it is plessed left key
                    x_change = -20
                elif event.key ==pygame.K_RIGHT:
                    x_change = 20
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change   
        #changing the background color 
        if dodged // 5 != last_background_col_indx // 5:
            last_background_col_indx = dodged
            background_col_indx = dodged // 5
        # checking if the background color in the array is used and restarting it 
        if background_col_indx >= len(background_col):
            background_col_indx = 0
                   
        gameDisplay.fill(background_col[background_col_indx])# paint white the background
        col_one = colors[col_indx_one]
        col_two = colors[col_indx_two]
        pygame.draw.rect(gameDisplay, col_two, [x, y, thing_width, thing_height])
        col_change = (random.randint(0,255), random.randint(0,255), random.randint(0, 255))
        col_change_two = (random.randint(0,255), random.randint(0,255), random.randint(0, 255))
        if thing_startx + thing_width > display_width: # privanting the falling rectangle passing the edge of the screen
            thing_startx = display_width - thing_width
        things(thing_startx, thing_starty, thing_width, thing_height, col_one)
        thing_starty += thing_speed
        
        #car(x,y,thing_startx, thing_starty, thing_width, thing_height, black)       
        things_dodged(dodged)
        if x > display_width - thing_width or x < 0: #if it touches the edge
            x -= x_change
        # check for crashing and if they have same color count it as two point
        if thing_starty >= display_height - thing_height:
            if (thing_startx >= x and thing_startx <= x + thing_width) or \
                (thing_startx + thing_width >= x and thing_startx + thing_width<= x + thing_width):
                    if col_one == col_two:
                        dodged += 1
                    else:
                        crash(dodged)
        
        #if thing_starty > display_height:# if the box reach the end
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            
            dodged += 1
            thing_speed += 0.35
            #col_one = col_change
            #col_two = col_change_two
            col_indx_two = (col_indx_two - 2) % len(colors)
            col_indx_one = (col_indx_one + 1) % len(colors)
     
                  
            
        pygame.display.update() #update the screen
        
        clock.tick(60)#speed how the time moves
        
car_loop()        
pygame.quit() #stop the pygame
quit()