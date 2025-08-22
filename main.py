import cv2
from gesture_control import HandGestureDetector
from effects import InvisibilityEffect

def main():
    cap = cv2.VideoCapture(0)
    gesture_detector = HandGestureDetector()
    invisibility = InvisibilityEffect()

    print("Press 'b' to capture background")
    print("Press 'q' to quit")

    cloak_active = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect gestures
        gesture = gesture_detector.detect_gesture(frame_rgb)
        if gesture == "cloak_on":
            cloak_active = True
        elif gesture == "cloak_off":
            cloak_active = False

        # Apply cloak effect
        if cloak_active:
            output = invisibility.apply_cloak(frame)
        else:
            output = frame

        cv2.imshow("Enchanted Invisibility Cloak", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("b"):
            invisibility.capture_background(frame)
            print("Background captured!")
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
