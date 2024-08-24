import numpy as np
import streamlit as st
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
import pythoncom
import mediapipe as mp
import cv2
class SoundControl:
    def __init__(self):
        self.volume_label = st.empty()  
        self.volume = self.initialize_volume_control()

    def initialize_volume_control(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, pythoncom.CLSCTX_INPROC_SERVER, None)
        return cast(interface, POINTER(IAudioEndpointVolume))

    def initialize_session_state(self):
        if 'volume' not in st.session_state:
            st.session_state.volume = 50

    def update(self, hand_landmarks, frame):
        thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]
        index_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
        h, w, _ = frame.shape
        thumb_coords = (int(thumb_tip.x * w), int(thumb_tip.y * h))
        index_coords = (int(index_tip.x * w), int(index_tip.y * h))

        # Draw a line between thumb and index finger
        cv2.line(frame, thumb_coords, index_coords, (0, 255, 0), 3)

        # Calculate the distance between thumb and index finger
        length = np.hypot(index_coords[0] - thumb_coords[0], index_coords[1] - thumb_coords[1])
       
       
        # Adjust the volume based on the distance
        vol = np.interp(length, [30, 300], [self.volume.GetVolumeRange()[0], self.volume.GetVolumeRange()[1]])
        self.volume.SetMasterVolumeLevel(vol, None)
        vol_percent = int(np.interp(vol, [self.volume.GetVolumeRange()[0], self.volume.GetVolumeRange()[1]], [0, 100]))
        if vol_percent != st.session_state.volume:
            st.session_state.volume = vol_percent
            self.volume_label.text(f'Volume: {vol_percent}%')
