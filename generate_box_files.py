import os
import subprocess

# Define the paths
image_folder = 'D:/Edge Downloads/Number-Plate-Recognition-Using-OpenCV-main/dataset/images'
tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ensure the image folder exists
if not os.path.exists(image_folder):
    print(f"Error: Image folder '{image_folder}' does not exist.")
    exit(1)

# List all image files in the directory
image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg')]

# Generate box files for each image
for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    output_base = os.path.splitext(image_path)[0]
    
    # Construct the Tesseract command
    command = [
        tesseract_cmd,
        image_path,
        output_base,
        '-l', 'eng',
        '--psm', '6',
        'batch.nochop', 'makebox'
    ]
    
    # Run the Tesseract command
    try:
        subprocess.run(command, check=True)
        print(f"Generated box file for {image_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error generating box file for {image_file}: {e}")
