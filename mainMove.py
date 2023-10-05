from tello_sdk import Tello
import keyboard
import time

# Initialize the Tello object
# line 7 creates an instance of the tello class and creates the connection to the drone 
tello = Tello.Tello()

# initalize connection
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

# Function to land the drone
def land():
    response = tello.land()
    print("Land response:", response)

def move_up():
    response = tello.up(50)  
    print("Up response:", response)

def move_forward():
    response = tello.forward(100)  
    print("Forward response:", response)

def move_left():
    response = tello.left(100)  
    print("Left response:", response)

def move_right():
    response = tello.right(100)  # Replace 50 with the desired distance in cm
    print("Right response:", response)    

def rotate_clockwise():
    response = tello.rotate('cw', 90)  # this is Rotating the drone 90 degrees clockwise
    print("Rotate response:", response)

def flip():
    response = tello.flip('f')  # Replace 'f' with the desired flip direction
    print("Flip response:", response)

def move_backward():
    response = tello.back(100)
    print("Backward response:", response)



def main():
    print("Press the following keys to control the drone:")
    print("  - 't' to take off")
    print("  - 'u' to move up")
    print("  - 'f' to move forward")
    print("  - 'b' to move backward")
    print("  - 'r' to rotate clockwise")
    print("  - 'p' to perform a flip")
    print("press L to land")
    print("  - 'q' to quit")

    while True:
        if keyboard.is_pressed('t'):
            take_off()
        elif keyboard.is_pressed('u'):
            move_up()
        elif keyboard.is_pressed('f'):
            move_forward()
        elif keyboard.is_pressed('b'):  
            move_backward()
        elif keyboard.is_pressed('r'):
            rotate_clockwise()
        elif keyboard.is_pressed('p'):
            flip()
        elif keyboard.is_pressed('L'):
            land()    
        elif keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
