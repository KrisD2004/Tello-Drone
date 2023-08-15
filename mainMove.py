from tello_sdk import Tello
import keyboard
import time

# Initialize the Tello object
tello = Tello.Tello()

def takeoff_and_land():
    response = tello.takeoff()
    print("Takeoff response:", response)
    time.sleep(120)  # Keep the drone in the air for 5 seconds
    response = tello.land()
    print("Land response:", response)

def move_up():
    response = tello.up(50)  # Replace 50 with the desired distance in cm
    print("Up response:", response)

def move_forward():
    response = tello.forward(100)  # Replace 100 with the desired distance in cm
    print("Forward response:", response)

def rotate_clockwise():
    response = tello.rotate('cw', 90)  # Rotate 90 degrees clockwise
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
