from tello_sdk import Tello
import keyboard
import time

# Initialize the Tello object
# line 7 creates an instance of the tello class and creates the connection to the drone 
tello = Tello.Tello() 

# initalizing the connection
tello.init()



# takeoff_and_land() that is responsible for taking off the drone, keeping it in the air for a few seconds, and then landing it
# def takeoff_and_land():
#     response = tello.takeoff()
#     print("Takeoff response:", response)
#     time.sleep(120)  # Keeping the drone in the air for 120 seconds(2 min)
#     response = tello.land()
#     print("Land response:", response)

def take_off():
    response = tello.takeoff()
    print("Takeoff response:", response)

def hover():
    response = tello.hover()
    print("hover response:", response)

# Function to land the drone
def land():
    response = tello.land()
    print("Land response:", response)

def move_up():
    response = tello.up(50)  
    print("Up response:", response)

def move_down():
    response = tello.down(50)
    print("Down response:", response)
    

def move_forward():
    response = tello.forward(100)  
    print("Forward response:", response)

def move_left():
    response = tello.left(100)  
    print("Left response:", response)

def move_right():
    response = tello.right(100)  # Replacing the 50 with the new distance in cm
    print("Right response:", response)    

def rotate_clockwise():
    response = tello.rotate('cw', 90)  # this is Rotating the drone 90 degrees clockwise
    print("Rotate response:", response)

def flip():
    response = tello.flip('f')  
    print("Flip response:", response)

def circle_around_object():
    for _ in range(4):
        response = tello.forward(50)  # Move forward
        print("Forward response:", response)
        response = tello.rotate('cw', 90)  # Rotate 90 degrees clockwise
        print("Rotate response:", response)

def figure_eight():
    for _ in range(2):
        # Loop to complete one loop of the figure-eight
        response = tello.forward(50)  # Move forward
        print("Forward response:", response)
        response = tello.rotate('cw', 45)  # Rotate 45 degrees clockwise
        print("Rotate response:", response)
        response = tello.forward(50)  # Move forward
        print("Forward response:", response)
        response = tello.rotate('ccw', 90)  # Rotate 90 degrees counterclockwise
        print("Rotate response:", response)

def barrel_roll():
    # Perform a barrel roll by combining roll and yaw commands
    response = tello.roll('right', 360)  # Roll right 360 degrees
    print("Roll response:", response)
    time.sleep(1)  # Wait for the roll to complete
    response = tello.rotate('cw', 360)  # Rotate 360 degrees clockwise (yaw)
    print("Rotate response:", response)

def move_backward():
    response = tello.back(100)
    print("Backward response:", response)



def main():
    print("Press the keys to control the drone:")
    print("  - 't' to take off")
    print(" - 'h' to move hover")
    print("  - 'i' to move up")
    print(" - 'k' to move down")
    print("  - 'w' to move forward")
    print("  - 's' to move backward")
    print(" - 'a' to turn left")
    print(" - 'd' to turn right")
    print("  - 'r' to rotate clockwise")
    print("  - 'f' to perform a flip")
    print("  - 'c' to circle around an object")
    print("  - 'e' to fly in a figure-eight pattern")
    print(" - 'b' to barrel roll")
    print("  - press 'L' to land")
    print("  - 'q' to quit")

    while True:
        if keyboard.is_pressed('t'):
            take_off()
        elif keyboard.is_pressed('h'):
            hover()
        elif keyboard.is_pressed('i'):
            move_up()
        elif keyboard.is_pressed('k'):
            move_down()
        elif keyboard.is_pressed('a'):
            move_left    
        elif keyboard.is_pressed('d'):
            move_right    
        elif keyboard.is_pressed('w'):
            move_forward()
        elif keyboard.is_pressed('s'):  
            move_backward()
        elif keyboard.is_pressed('r'):
            rotate_clockwise()
        elif keyboard.is_pressed('f'):
            flip()
        elif keyboard.is_pressed('c'):
            circle_around_object()
        elif keyboard.is_pressed('e'):
            figure_eight() 
        elif keyboard.is_pressed == ('b'):
            barrel_roll()       
        elif keyboard.is_pressed('L'):
            land()    
            break
        elif keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
