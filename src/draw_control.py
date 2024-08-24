import numpy as np
import cv2
import streamlit as st
import mediapipe as mp

class DrawControl:
    def __init__(self, color):
        self.color = DrawControl.hex_to_rgb(color)  
        self.draw_label = st.empty() 

    def initialize_session_state(self):
        if 'drawing_points' not in st.session_state:
            st.session_state.drawing_points = []

    def update(self, hand_landmarks, frame):
        # Get the positions of the index and middle finger tips
        index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP]

        h, w, _ = frame.shape
        index_coords = (int(index_tip.x * w), int(index_tip.y * h))

        # Check if the index and middle fingers are up
        index_up = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP].y < \
                   hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_PIP].y
        middle_up = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_TIP].y < \
                    hand_landmarks.landmark[mp.solutions.hands.HandLandmark.MIDDLE_FINGER_PIP].y
        ring_up = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_TIP].y < \
                  hand_landmarks.landmark[mp.solutions.hands.HandLandmark.RING_FINGER_PIP].y
        pinky_up = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_TIP].y < \
                   hand_landmarks.landmark[mp.solutions.hands.HandLandmark.PINKY_PIP].y
        thumb_up = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP].x < \
                   hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_IP].x
 
        eraser_active = index_up and middle_up and not (ring_up and pinky_up and thumb_up)
 
        if index_up and middle_up and ring_up and pinky_up and thumb_up:
            st.session_state.drawing_points = []   
            self.draw_label.text(f"Canvas cleared!")

        elif eraser_active: 
            erase_radius = 50   
            st.session_state.drawing_points = [
                point for point in st.session_state.drawing_points
                if np.hypot(point[0] - index_coords[0], point[1] - index_coords[1]) > erase_radius
            ]
        else: 
            if st.session_state.drawing_points:
                cv2.line(frame, st.session_state.drawing_points[-1], index_coords, self.color, 5)
            st.session_state.drawing_points.append(index_coords)
 
        for i in range(1, len(st.session_state.drawing_points)):
            cv2.line(frame, st.session_state.drawing_points[i-1], st.session_state.drawing_points[i], self.color, 5)

    @staticmethod
    def hex_to_rgb(hex_color):
        hex_color = hex_color.lstrip('#')
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
