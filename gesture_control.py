import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

class HandGestureDetector:
    def __init__(self, max_hands=1):
        self.hands = mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )

    def detect_gesture(self, frame_rgb):
        results = self.hands.process(frame_rgb)
        gesture = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame_rgb, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Simple gesture example: Open palm vs fist
                landmarks = hand_landmarks.landmark
                if landmarks[8].y < landmarks[6].y:  # Index finger extended
                    gesture = "cloak_on"
                else:
                    gesture = "cloak_off"

        return gesture
