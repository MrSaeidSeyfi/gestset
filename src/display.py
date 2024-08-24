class DisplayHandler:
    def display_frame(self, frame, frame_placeholder):
        frame_placeholder.image(frame, channels="RGB")
