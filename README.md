# Image Coordinate Viewer

A simple application that allows you to view images and track cursor coordinates within the image.

## Features
- Open and view images in common formats (PNG, JPG, JPEG, GIF, BMP, TIFF)
- Real-time display of cursor coordinates as you move over the image
- Window title shows image dimensions

## Requirements
- Python 3.x
- Pillow (PIL) library

## Installation

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python image_coordinates.py
```

2. Click the "Open Image" button to select an image file
3. Move your cursor over the image to see the coordinates
4. The coordinates are displayed at the top of the window

## Command-line Setup (Optional)
To make the script executable from anywhere in your terminal:

1. Make the script executable:
```bash
chmod +x image_coordinates.py
```

2. Create a symbolic link (requires sudo):
```bash
sudo ln -s "/path/to/your/image_coordinates.py" /usr/local/bin/image-coords
```

After setup, you can run the application from anywhere by typing:
```bash
image-coords
```

To remove the command-line shortcut:
```bash
sudo rm /usr/local/bin/image-coords
```

## Supported Image Formats
- PNG
- JPG/JPEG
- GIF
- BMP
- TIFF 