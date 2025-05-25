# Hand Tracking Project

This project implements real-time hand tracking using computer vision and can optionally control servo motors through an ESP32 microcontroller.

## Features

- Real-time hand tracking using MediaPipe
- Precise finger position detection
- Optional ESP32 integration for servo motor control
- Visual feedback with landmark visualization
- Coordinate mapping for servo control

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- PySerial (for ESP32 integration)

## Installation

1. Clone the repository:
```bash
git clone [Your GitHub Repository URL]
cd "project hand tracking"
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Hand Tracking
Run the basic hand tracking script:
```bash
python hand_tracking.py
```

### Hand Tracking with ESP32 Integration
1. Connect your ESP32 to your computer
2. Update the serial port in `hand_tracking_with_servos.py`
3. Run the script:
```bash
python hand_tracking_with_servos.py
```

## Project Structure

- `hand_tracking.py`: Basic hand tracking implementation
- `hand_tracking_with_servos.py`: Hand tracking with ESP32 integration
- `requirements.txt`: Project dependencies

## Demo

[Add your demo video link here]

## LinkedIn Profile

[Add your LinkedIn profile image and link here]

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- MediaPipe for the hand tracking solution
- OpenCV for computer vision capabilities
- ESP32 community for microcontroller support

## Contact

[Add your contact information here] 