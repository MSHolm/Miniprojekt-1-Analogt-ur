# Importing the modules that I'm gonna need.
import pygame
import math
from datetime import datetime # Here I'm importing the class 'datetime' from the module 'datetime'.

# Initializing pygame
pygame.init()

# Setting the pygame display/screen to the size (700 x 500) and defining the colors white and black.
screen = pygame.display.set_mode((700, 500))
white = (255, 255, 255)
black = (0, 0, 0)

# This is the main loop. Here running is set to True and if pygame detects a QUIT event, then running 
# is False and pygame stops. So if we quit the program, we are allowed to quit the program which is nice.
running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Defining the center and radius of the clock-circle. Center is defined as the width and height of
    # the screen divided by two, so it's right in the middle of the screen.
    center = (screen.get_width() // 2, screen.get_height() // 2)
    radius = 200


    # Here I'm defining three variables each referring to either the current second, minute or hour in
    # real time. I've defined current_min as the current minute plus current_sec divided by 60. 
    # And I've defined current_hour as the current hour plus current_min divided by 60.
    # I've done this to give the minute- and hour-arm a smooth moving motion.  
    # The second-arm moves 6 degrees every second because the clock-circle is 
    # 360 degrees and there are 60 seconds per minute, so 360 / 60 = 6. The minute-arm will move 
    # 6 / 60 = 0.1 degrees per second and the hour-arm will move 0.1 / 60 = 0.00166667 degrees per second. 
    # The minute arm will move correctly from minute to minute, but will also move 1 / 60 * 6 degrees
    # per second. 
    # The hour arm will also move correctly from hour to hour, but will also move 
    # 1 / 3600 * 6 degrees per second. 
    current_sec = datetime.now().second
    current_min = datetime.now().minute + current_sec / 60
    current_hour = datetime.now().hour + current_min / 60
    
    screen.fill((135, 180, 255)) # Here I clear the screen by filling the screen with the color white. 
    # I'm doing this in the beginning of my while loop, which is my main loop. This is clearing the screen
    # in the beginning of every iteration of the loop, which allows for the animation of the clock arms
    # moving with the current time to work. 

    # Drawing the clock-circle and filling it with a reddish color.
    pygame.draw.circle(screen, (255, 50, 100), (center[0], center[1]), radius,)
    # Drawing a black circle/edge around the red clock-circle
    pygame.draw.circle(screen, (0, 0, 0), (center[0], center[1]), radius, 3)

    # In the code below I'm drawing the second-arm. I'm defining the variable 'seconds' as a range() function with the parameters (1, 61), which means 
    # there are 60 elements in the function. The angle of the second-arm, 'angle_seconds', is
    # defined as the variable 'current_sec', which refers to the current second in real time multiplied
    # by 6, minus 90. I'm multiplying by 6 because the second-arm needs to move 6 degrees per second.
    # I'm minusing by 90 to adjust the starting position of the arm to the top of the clock at the 
    # '12' mark. The angle is then converted to radians with the functions 'math.radians()'. 
    
    # The starting position of the second-arm is the center of the clock-circle, (center[0], center[1])
    # and the end position consisting of the two variables (sec_x, sec_y), are defined as going from the
    # center of the clock-circle with the length (radius * 0.7) multiplied by cos to the angle 
    # 'angle_seconds' for the x-coordinate and sin to the angle for the y-coordinate. 
    seconds = range(1, 61)
    for sec in seconds:
        angle_seconds = math.radians(current_sec * 6 - 90)
        sec_x = center[0] + radius * 0.7 * math.cos(angle_seconds)
        sec_y = center[1] + radius * 0.7 * math.sin(angle_seconds)
        pygame.draw.line(screen, black, (center[0], center[1]), (sec_x, sec_y), 2)
    
    # Here I'm drawing the minute-arm and I'm doing the same as in the code above, except I'm using the
    # variable 'current_min'. I'm multiplying by 6 and minusing by 90, just like with the second-arm, 
    # because there are 60 minutes per hour. I'm multiplying the length of the arm, which is radius, by 
    # 0.5 to make it a little shorter than the second-arm. 
    minutes = range(1, 61)
    for min in minutes:
        angle_minutes = math.radians(current_min * 6 - 90)
        min_x = center[0] + radius * 0.5 * math.cos(angle_minutes)
        min_y = center[1] + radius * 0.5 * math.sin(angle_minutes)
        pygame.draw.line(screen, black, (center[0], center[1]), (min_x, min_y), 3)

    # Here I'm drawing the hour-arm. In the input of the math.radians function, I'm multiplying 
    # current_hour with 30 and minusing with 90 instead of multiplying with 6. This is because in an 
    # analog clock there's only 12 markings for the hours and 360 / 12 = 30. I'm multiplying the radius
    # by 0.35 to make it shorter than the minute-arm. 
    hours = range(1, 61)
    for hour in hours: 
        angle_hours = math.radians(current_hour * 30 - 90)
        hour_x = center[0] + radius * 0.35 * math.cos(angle_hours)
        hour_y = center[1] + radius * 0.35 * math.sin(angle_hours)
        pygame.draw.line(screen, black, (center[0], center[1]), (hour_x, hour_y), 4)

    
    # Drawing the 60 minute marks in the clock-circle. I'm using a for loop and the range() 
    # function and inserting 60 in the function parameter of range(). I'm calculating the angle of
    # the minute markings the same way I calculate the angle of the minute-arm. I'm setting the
    # starting position of the minute marks to the exact path on the circle and the end position to the
    # same as the starting position, but where the length is 5% shorter, which is creating a visible
    # mark starting on the circle-path and going a bit towards the center of the circle. 
    for min_marks in range(60): 
        angle_min_mark = math.radians(min_marks * 6 - 90)
        x_min_mark = center[0] + radius * 0.95 * math.cos(angle_min_mark)
        y_min_mark = center[1] + radius * 0.95 * math.sin(angle_min_mark)
        pygame.draw.line(screen, black, (center[0] + radius * math.cos(angle_min_mark), center[1] + radius * math.sin(angle_min_mark)), (x_min_mark, y_min_mark), 1)

    # Drawing the hour marks in the clock-circle. I'm doing the same as with the minute marks, but only
    # drawing 12 marks. 
    for hour_marks in range(12):
        angle_hour_mark = math.radians(hour_marks * 30 - 90)
        x_hour_mark = center[0] + radius * 0.93 * math.cos(angle_hour_mark)
        y_hour_mark = center[1] + radius * 0.93 *math.sin(angle_hour_mark)
        pygame.draw.line(screen, black, (center[0] + radius * math.cos(angle_hour_mark), center[1] + radius * math.sin(angle_hour_mark)), (x_hour_mark, y_hour_mark), 3)

    # Inserting the clock numbers from 1 to 12 in form of text/string. 
    font = pygame.font.SysFont("Comic Sans MS", 36)
    numbers = range(1, 13)
    for number in (numbers):
        angle_number = math.radians(number * 30 - 90)
        text = font.render(str(number), True, (0, 0, 0))
        text_pos_x = center[0] + radius * 0.83 * math.cos(angle_number) - text.get_width() / 2
        text_pos_y = center[1] + radius * 0.83 * math.sin(angle_number) - text.get_height() / 2
        screen.blit(text, (text_pos_x, text_pos_y))

    # Updating the display
    pygame.display.flip()

# Quitting pygame
pygame.quit()