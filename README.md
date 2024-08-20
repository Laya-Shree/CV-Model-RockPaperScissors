# Rock-Paper-Scissors Gesture Detection Game

This project is a computer vision-based Rock-Paper-Scissors game that uses hand gesture detection via YOLOv10. The game allows you to play against an AI by detecting your hand gesture and comparing it with the AI's random choice.

## Features

- **Real-time Hand Gesture Detection**: Detects "Rock," "Paper," and "Scissors" gestures from your hand using your webcam.
- **AI Opponent**: The game randomly selects "Rock," "Paper," or "Scissors" for the AI.
- **Scorekeeping**: The game keeps track of the scores for both the player and the AI.

## Controls

- **Press 's'**: Start the game.
- **Press 'r'**: Reset the scores.
- **Press 'Esc'**: Exit the game.

## Tips for Better Detection

- **Bring your hand closer to the camera**: Ensure your hand is in focus for the camera to improve detection accuracy.
- **Keep your hand ready**: Keep your hand steady and ready when timer displays rock - paper - scissors for better detection.

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/Laya-Shree/CV-Model-RockPaperScissors
    cd CV-Model-RockPaperScissors
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:

    ```bash
    python game.py
    ```


## How the Game Works

1. **Start the Game**: Press 's' to start the game. The AI will randomly select its move, and the system will try to detect your gesture using your webcam.
2. **Show Your Gesture**: Hold your hand closer to the camera for better detection.
3. **Results**: The game compares your gesture with the AI's selection and updates the scores accordingly.
