import pygame
from time import sleep
from tello_sdk import Tello

# Initialize Pygame
pygame.init()

# Set up Pygame window
window_size = (400, 400)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tello Mouse Control")

# Initialize the Tello object
tello = Tello()

# Function to send Tello commands based on mouse events
def control_tello(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # Left mouse button (take off)
            tello.takeoff()
        elif event.button == 3:  # Right mouse button (land)
            tello.land()

    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        # Adjust the mouse coordinates to match Tello's control range
        tello_x = int((x / window_size[0]) * 200 - 100)
        tello_y = int((y / window_size[1]) * 200 - 100)
        tello.go_xyz_speed(x=tello_x, y=tello_y, z=0, speed=30)  # Adjust the speed as needed

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            control_tello(event)

    pygame.display.update()

# Clean up
tello.land()
tello.quit()
pygame.quit()
