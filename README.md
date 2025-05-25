
# Hand Tracking Project - PUG 2023

This project implements real-time hand tracking using computer vision and optionally controls servo motors through an **Arduino** microcontroller. Developed as part of the PUG 2023 initiative, it offers an intuitive interface for detecting finger positions and translating them into motion commands.

![Project Demo](assets/demo_image.jpg) 

## Features

- ✅ Real-time hand tracking using MediaPipe
- ✅ Precise finger position detection
- ✅ Optional **Arduino** integration for servo motor control
- ✅ Visual feedback with landmark visualization
- ✅ Coordinate mapping for servo movement control

## Requirements

- Python 3.7+
- OpenCV
- MediaPipe
- NumPy
- PySerial (for Arduino integration)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/[your-username]/hand-tracking-pug2023.git
   cd hand-tracking-pug2023
```
```
2. **Install dependencies**
```
   bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Hand Tracking

To run hand tracking without Arduino:

```bash
python hand_tracking.py
```

### Hand Tracking with Arduino Integration

1. Connect your **Arduino** to your computer via USB.
2. Open `hand_tracking_with_servos.py` and update the serial port (e.g., `COM3` or `/dev/ttyUSB0`).
3. Run the script:

```bash
python hand_tracking_with_servos.py
```

## Project Structure

```
├── hand_tracking.py                # Basic hand tracking
├── hand_tracking_with_servos.py   # With Arduino integration
├── requirements.txt               # Python dependencies
├── assets/                        # Demo images/videos
├── README.md                      # Project documentation
```

## Demo

🎬 **Watch the demo video here**
[![Watch the demo](https://img.youtube.com/vi/your_video_id/0.jpg)](https://www.youtube.com/watch?v=your_video_id)

> Replace `your_video_id` with the actual YouTube video ID.

Or upload a `.mp4` to `assets/` and embed it like:

```html
<video src="assets/demo.mp4" controls width="100%"></video>
```

## LinkedIn

👤 **P. N. Bhargav Teja**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bhargav%20Teja-blue?logo=linkedin)](https://www.linkedin.com/in/bhargavteja)

## Contributing

Contributions are welcome! Feel free to:

* Submit issues
* Suggest features
* Create pull requests

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* [MediaPipe](https://mediapipe.dev/) – Hand tracking solution
* [OpenCV](https://opencv.org/) – Computer vision toolkit
* Arduino Community – Servo and serial support

## Contact

📧 [bhargavteja5098171@gmail.com](mailto:bhargavteja5098171@gmail.com)
🌐 [https://www.linkedin.com/in/bhargavteja](https://www.linkedin.com/in/bhargavteja)
📍 VIT Vellore | Founder, Allure Tech Services

```

---

Let me know if you'd like me to generate:
- A banner image
- Video thumbnail
- Social media card for GitHub

Or help you deploy this to GitHub Pages or make it a portfolio piece!
```
