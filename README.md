# Number Plate Recognition

A Python-based project that detects and recognizes number plates from vehicle images using advanced image processing techniques and Optical Character Recognition (OCR). This repository provides a framework for extracting text from vehicle number plates, which can be applied in various fields such as traffic monitoring, parking management, and law enforcement.

## Features

- Automatic detection of vehicle number plates in images.
- Recognition of characters on the number plate using OCR.
- Easy-to-use and customizable codebase.
- Supports multiple image formats.

## Technologies Used

- **Python**: The core programming language.
- **OpenCV**: For image processing and number plate detection.
- **Tesseract OCR**: For optical character recognition.
- **NumPy**: For numerical operations.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- OpenCV
- Tesseract OCR
- NumPy

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KaranJaiswal02/Number-Plate-Recognition.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Number-Plate-Recognition
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR:
   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install tesseract-ocr
     ```
   - On macOS (using Homebrew):
     ```bash
     brew install tesseract
     ```
   - On Windows, download the installer from [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract).

## Usage

1. Place the images of vehicles in the `input_images` directory.
2. Run the script:
   ```bash
   python number_plate_recognition.py
   ```
3. Recognized text and processed images will be saved in the `output` directory.

## File Structure

```
Number-Plate-Recognition/
├── input_images/         # Directory to store input images
├── output/               # Directory to store processed images and results
├── number_plate_recognition.py # Main script
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Demo

![Demo GIF](demo.gif)

## Contributing

Contributions are welcome! If you have any ideas or enhancements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [OpenCV](https://opencv.org/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- Inspiration from various open-source projects and tutorials.
