from tello_sdk import Tello
import keyboard
import time

# Initialize the Tello object
# line 7 creates an instance of the tello class and creates the connection to the drone 
tello = Tello.Tello() 


# takeoff_and_land() that is responsible for taking off the drone, keeping it in the air for a few seconds, and then landing it
def takeoff_and_land():
    response = tello.takeoff()
    print("Takeoff response:", response)
    time.sleep(120)  # Keeping the drone in the air for 120 seconds(2 min)
    response = tello.land()
    print("Land response:", response)

def move_up():
    response = tello.up(50)  
    print("Up response:", response)

def move_forward():
    response = tello.forward(100)  
    print("Forward response:", response)

def rotate_clockwise():
    response = tello.rotate('cw', 90)  # this is Rotating the drone 90 degrees clockwise
    print("Rotate response:", response)

def flip():
    response = tello.flip('f')  # Replace 'f' with the desired flip direction
    print("Flip response:", response)

def main():
    print("Press the following keys to control the drone:")
    print("  - 't' to take off and land")
    print("  - 'u' to move up")
    print("  - 'f' to move forward")
    print("  - 'r' to rotate clockwise")
    print("  - 'l' to perform a flip")
    print("  - 'q' to quit")

    while True:
        if keyboard.is_pressed('t'):
            takeoff_and_land()
        elif keyboard.is_pressed('u'):
            move_up()
        elif keyboard.is_pressed('f'):
            move_forward()
        elif keyboard.is_pressed('r'):
            rotate_clockwise()
        elif keyboard.is_pressed('l'):
            flip()
        elif keyboard.is_pressed('q'):
            break

if __name__ == "__main__":
    main()
