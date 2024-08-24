import cv2
import mediapipe as mp
import streamlit as st
class HandTracker:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)
        self.frame_placeholder = st.empty()

    def capture_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def process_frame(self, frame):
        with self.mp_hands.Hands(max_num_hands=2) as hands:  # Allow detecting up to 2 hands
            results = hands.process(frame)
            return results.multi_hand_landmarks if results.multi_hand_landmarks else []

    def release_resources(self):
        self.cap.release()
        cv2.destroyAllWindows()
