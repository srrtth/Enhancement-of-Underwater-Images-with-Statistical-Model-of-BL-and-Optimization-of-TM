import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk

def select_image():
    # Open a file dialog to select an image
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        # Copy the selected image to the input folder
        shutil.copy2(file_path, "EnhancementofUnderwaterImages/InputImages")
        messagebox.showinfo("Image Selected", "Image has been added to the InputImages folder.")

        # Display the selected image
        image = Image.open(file_path)  
        image.thumbnail((400, 400))  # Resize the image for display
        photo = ImageTk.PhotoImage(image)
        image_label.configure(image=photo)
        image_label.image = photo

def run_image_enhancement():
    # Run the image enhancement code
    try:
        messagebox.showinfo("Processing", "Image enhancement is in progress...")
        subprocess.run(["python", "C:/Users/legra/OneDrive/Documents/GitHub/Enhancement-of-Underwater-Images-with-Statistical-Model-of-BL-and-Optimization-of-TM/EnhancementofUnderwaterImages/main.py"])
        messagebox.showinfo("Execution Complete", "Image enhancement completed.")

        # Display the enhanced image from the output folder
        output_image_path = "EnhancementofUnderwaterImages/OutputImages/EnhancedbySAR.jpg"
        if os.path.exists(output_image_path):
            image = Image.open(output_image_path)
            image.thumbnail((400, 400))  # Resize the image for display
            photo = ImageTk.PhotoImage(image)
            image_label.configure(image=photo)
            image_label.image = photo
    except FileNotFoundError:
        messagebox.showerror("Error", "The 'main.py' file was not found.")

# Create the GUI window
window = tk.Tk()
window.title("Enhancement of  Underwater Images ")
window.geometry("1000x800")
window.configure(bg="#5A5A5A")

# Image Selection Button
select_button = tk.Button(window, text="Select Image", command=select_image, bg="red", fg="black")
select_button.pack(pady=50)

# Image Label
image_label = tk.Label(window, bg="#5A5A5A")
image_label.pack(pady=50)

# Start Button
start_button = tk.Button(window, text="Start", command=run_image_enhancement, bg="red", fg="black")
start_button.pack(pady=50)

# Run the GUI event loop
window.mainloop()
