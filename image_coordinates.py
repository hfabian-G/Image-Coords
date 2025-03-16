#!/usr/bin/env python3
import tkinter as tk
from tkinter import filedialog, Label, Frame
from PIL import Image, ImageTk

class ImageCoordinateViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Coordinate Viewer")
        
        # Create main frame
        self.main_frame = Frame(root)
        self.main_frame.pack(expand=True, fill='both')
        
        # Create coordinate label
        self.coord_label = Label(self.main_frame, text="Coordinates: (-, -)")
        self.coord_label.pack(pady=5)
        
        # Create image label
        self.image_label = Label(self.main_frame)
        self.image_label.pack(expand=True, fill='both')
        
        # Create open button
        self.open_button = tk.Button(self.main_frame, text="Open Image", command=self.open_image)
        self.open_button.pack(pady=5)
        
        # Bind mouse motion
        self.image_label.bind('<Motion>', self.show_coordinates)
        
        # Initialize image variable
        self.image = None
        self.photo = None
        
    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            # Open and display the image
            self.image = Image.open(file_path)
            # Convert to PhotoImage for display
            self.photo = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.photo)
            
            # Update window title with image dimensions
            width, height = self.image.size
            self.root.title(f"Image Coordinate Viewer ({width}x{height})")
    
    def show_coordinates(self, event):
        if self.image:
            # Get cursor position relative to the image
            x, y = event.x, event.y
            
            # Update coordinate label
            self.coord_label.config(text=f"Coordinates: ({x}, {y})")

def main():
    root = tk.Tk()
    app = ImageCoordinateViewer(root)
    root.mainloop()

if __name__ == "__main__":
    main() 