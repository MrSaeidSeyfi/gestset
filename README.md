
# GestSet-VirtualControl

This project is a hand gesture-based interface that enables users to interact with their computer and various applications using intuitive hand gestures. The application uses OpenCV for capturing video from your webcam, MediaPipe for hand detection and gesture recognition, and Streamlit for the user interface.

## Features

- **Brightness Control**: Adjust the screen brightness by moving your thumb and index finger closer or farther apart. A line is drawn between the thumb and index finger, and the distance is displayed on the screen.
  
- **Volume Control**: Adjust the system volume similarly by moving your thumb and index finger. The application draws a line between these two fingers and displays the distance, which is used to control the volume level.

- **Drawing Mode**: Use your index finger to draw on a virtual canvas. You can select a color to draw with, erase parts of your drawing by raising both the index and middle fingers, and clear the entire canvas by raising all fingers.

## Requirements

- Python 3.7 or higher
- Streamlit
- OpenCV
- MediaPipe
- Pycaw (for volume control on Windows)
- WMI (for brightness control on Windows)

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/MrSaeidSeyfi/gestset
    cd gestset
    ```

2. **Create a virtual environment**:

    ```bash
    python -m venv env
    ```

3. **Activate the virtual environment**:

    - On Windows:

      ```bash
      .\env\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source env/bin/activate
      ```

4. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:

    ```bash
    streamlit run app.py
    ```

2. **Navigate to the URL provided by Streamlit**, typically `http://localhost:8501`, in your web browser.

3. **Select a Control Mode**:

    - **Brightness Control**: Adjust the screen brightness.
    - **Volume Control**: Adjust the system volume.
    - **Drawing**: Draw on a virtual canvas.

4. **Interact with the application** using hand gestures:
    - **Brightness and Volume Control**: Move your thumb and index finger closer or farther apart to change the brightness or volume. A line will be drawn between the fingers, and the distance will be displayed.
    - **Drawing Mode**:
        - Use your index finger to draw.
        - Select a color using the color picker.
        - Raise both index and middle fingers to erase.
        - Raise all fingers to clear the canvas.

5. ** Result **
   


https://github.com/user-attachments/assets/f09e5578-db5e-49b4-b6e5-2a5581dd9b89


## Known Issues and Limitations

- **Platform-Specific Controls**: The brightness and volume controls are currently implemented for Windows only, using WMI and Pycaw. These features may not work on other operating systems.
- **Lighting Conditions**: The accuracy of hand tracking may vary depending on the lighting conditions and the quality of your webcam.
- **Multi-Hand Limitations**: The application currently only supports single-hand interactions for control modes.

## Future Improvements

- **Cross-Platform Support**: Extend brightness and volume control to work on macOS and Linux.
- **Enhanced Gesture Recognition**: Improve the accuracy and range of gestures recognized by the system.
- **Additional Features**: Add more control options, such as media playback controls or custom gesture-based shortcuts.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.


## References

This project is inspired and supported by recent advancements in hand pose detection and gesture control technologies. Below are some key references:

1. **CLIP-Hand3D: Exploiting 3D Hand Pose Estimation via Context-Aware Prompting**: This research explores using CLIP (Contrastive Language-Image Pretraining) to bridge text prompts with 3D hand pose estimation. It offers a new perspective on combining textual descriptions with visual features. [Read more](https://arxiv.org/abs/2309.16140).

2. **HandDiff: 3D Hand Pose Estimation with Diffusion on Image-Point Cloud**: This paper introduces a diffusion-based method for 3D hand pose estimation, treating the problem as a 3D point subset generative task. It shows promising results in generating accurate 3D hand poses from input images. [Read more](https://arxiv.org/abs/2404.03159).


## License

This project is licensed under the MIT License. See the LICENSE file for more details.


