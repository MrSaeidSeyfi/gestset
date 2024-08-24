import numpy as np
import streamlit as st
from src.utils import set_brightness_windows
import mediapipe as mp
import cv2

class BrightnessControl:
    def __init__(self):
        self.brightness_label = st.empty()  # Placeholder for the brightness label
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands

    def initialize_session_state(self):
        if 'brightness' not in st.session_state:
            st.session_state.brightness = 50

    def update(self, hand_landmarks, frame):
        thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
        h, w, _ = frame.shape
        thumb_coords = (int(thumb_tip.x * w), int(thumb_tip.y * h))
        index_coords = (int(index_tip.x * w), int(index_tip.y * h))

        # Draw hand landmarks on the frame
        self.mp_drawing.draw_landmarks(
            frame,
            hand_landmarks,
            self.mp_hands.HAND_CONNECTIONS,
            self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2),
            self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
        )

        # Draw a line between thumb and index finger
        cv2.line(frame, thumb_coords, index_coords, (0, 255, 0), 3)

        # Calculate the distance between thumb and index finger
        length = np.hypot(index_coords[0] - thumb_coords[0], index_coords[1] - thumb_coords[1])
       
        # Adjust the brightness based on the distance
        brightness = int(np.interp(length, [30, 300], [0, 100]))
        if brightness != st.session_state.brightness:
            set_brightness_windows(brightness)
            st.session_state.brightness = brightness
            self.brightness_label.text(f'Brightness: {brightness}%')
