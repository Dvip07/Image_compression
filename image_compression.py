import tkinter as tk
from tkinter import filedialog
from PIL import Image

def compress_image():
    input_path = filedialog.askopenfilename(title="Select an Image")
    if not input_path:
        return  # User canceled file selection
    
    output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG Files", "*.jpg")], title="Save Compressed Image")
    if not output_path:
        return  # User canceled save dialog
    
    quality = compression_quality.get()  # Get compression quality from a GUI variable
    
    try:
        img = Image.open(input_path)
        img.save(output_path, optimize=True, quality=quality)
        status_label.config(text=f"Image compressed and saved to {output_path}")
    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")

# Create the GUI window
root = tk.Tk()
root.title("Image Compression Tool")

# Create a button to trigger compression
compress_button = tk.Button(root, text="Compress Image", command=compress_image)
compress_button.pack()

# Create a slider for compression quality
compression_quality = tk.Scale(root, from_=0, to=100, orient="horizontal", label="Compression Quality")
compression_quality.set(80)  # Set default quality
compression_quality.pack()

# Create a label to display the compression status
status_label = tk.Label(root, text="")
status_label.pack()

# Start the GUI event loop
root.mainloop()
