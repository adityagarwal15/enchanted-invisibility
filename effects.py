import cv2
import numpy as np

class InvisibilityEffect:
    def __init__(self):
        self.background = None

    def capture_background(self, frame):
        self.background = frame.copy()

    def apply_cloak(self, frame):
        if self.background is None:
            return frame

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define red cloak color range (can adjust)
        lower_red = np.array([0, 120, 70])
        upper_red = np.array([10, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        lower_red = np.array([170, 120, 70])
        upper_red = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv, lower_red, upper_red)

        mask = mask1 + mask2

        # Refine mask
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

        mask_inv = cv2.bitwise_not(mask)

        res1 = cv2.bitwise_and(self.background, self.background, mask=mask)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)

        return cv2.addWeighted(res1, 1, res2, 1, 0)
