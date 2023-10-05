from djitellopy import Tello
import threading

import cv2

Tello = Tello()

def video_stream():
    while True:
        frame = Tello.get_frame_read().frame
        cv2.imshow("Tello Video Stream", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):  # Press 'q' to exit the video stream
            break


def keyboard_control():
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):  # Press 'q' to quit the program
            break
        elif key == ord("t"):  # Press 't' to takeoff
            Tello.takeoff()
        elif key == ord("l"):  # Press 'l' to land
            Tello.land()
        elif key == ord("w"):  # Press 'w' to move forward
            Tello.move_forward(50)
        elif key == ord("s"):  # Press 's' to move backward
            Tello.move_back(50)
        elif key == ord("a"):  # Press 'a' to move left
            Tello.move_left(50)
        elif key == ord("d"):  # Press 'd' to move right
            Tello.move_right(50)
        elif key == ord("r"):  # Press 'r' to rotate clockwise
            Tello.rotate_clockwise(30)
        elif key == ord("f"):  # Press 'f' to rotate counterclockwise
            Tello.rotate_counter_clockwise(30)
#intitating the connection with the drone 
Tello.connect()

Tello.streamon()

video_thread = threading.Thread(target=video_stream)
video_thread.daemon = True
video_thread.start()

# takeoff function for the drone
Tello.takeoff()
# landing fucntion for the drone
Tello.land() 

Tello.streamoff()

cv2.destroyAllWindows()
