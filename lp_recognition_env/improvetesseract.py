import cv2
import pytesseract
import pandas as pd
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the annotation file
annot_df = pd.read_csv('D:/Edge Downloads/Number-Plate-Recognition-Using-OpenCV-main/dataset/annot_file.csv')

# Define the paths to the image folders
image_folder = 'D:/Edge Downloads/Number-Plate-Recognition-Using-OpenCV-main/dataset/images'
crop_folder = 'D:/Edge Downloads/Number-Plate-Recognition-Using-OpenCV-main/dataset/crops'

# Define the preprocessing function
def preprocess_image(image_path):
    # Check if the image file exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' does not exist.")
        return None

    # Load the image
    img = cv2.imread(image_path)

    # Check if the image was loaded successfully
    if img is None:
        print(f"Error: Unable to read image file '{image_path}'.")
        return None

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Return the preprocessed image
    return thresh

# Define the function to extract text from an image
def extract_text(image_path):
    # Preprocess the image
    img = preprocess_image(image_path)

    # Check if the image was preprocessed successfully
    if img is None:
        return None

    # Define the custom configuration for Tesseract
    custom_config = r'--oem 3 --psm 6'

    # Extract text from the image
    text = pytesseract.image_to_string(img, config=custom_config)

    # Return the extracted text
    return text

# Loop through the annotation file and extract text from each image
for index, row in annot_df.iterrows():
    # Get the image path
    image_path = f'{image_folder}/{row["files"]}'

    # Extract text from the image
    text = extract_text(image_path)

    # Check if the text was extracted successfully
    if text is None:
        continue

    # Print the extracted text
    print(f"Extracted text from {image_path}: {text}")

    # Save the extracted text to a file
    with open(f'{crop_folder}/{row["files"]}.txt', 'w') as f:
        f.write(text)