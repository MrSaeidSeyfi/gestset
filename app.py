import streamlit as st
from src.brightness_control import BrightnessControl
from src.sound_control import SoundControl
from src.draw_control import DrawControl
from src.hand_tracker import HandTracker
from src.display import DisplayHandler

def main():
    st.set_page_config(page_title="Hand Gesture Control App")
    st.title("GestSet") 

    control_mode = st.radio("Select Control Mode", ("Brightness Control", "Volume Control", "Drawing"))

    hand_tracker = HandTracker()
    display_handler = DisplayHandler()

    if control_mode == "Brightness Control":
        control = BrightnessControl()
    elif control_mode == "Volume Control":
        control = SoundControl()
    elif control_mode == "Drawing":
        selected_color = st.color_picker("Pick a drawing color", "#ff0000")  # Color picker
        control = DrawControl(selected_color)

    control.initialize_session_state()

    while hand_tracker.cap.isOpened():
        frame = hand_tracker.capture_frame()
        if frame is None:
            st.write("Video Capture Ended")
            break

        hand_landmarks_list = hand_tracker.process_frame(frame)
        if hand_landmarks_list:
            hand_landmarks = hand_landmarks_list[0]  # Use only the first detected hand
            control.update(hand_landmarks, frame)

        display_handler.display_frame(frame, hand_tracker.frame_placeholder)

    hand_tracker.release_resources()

if __name__ == "__main__":
    main()
