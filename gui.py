
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def create_tire_monitoring_gui(tire_image_path):
    # Create the main application window
    root = tk.Tk()
    root.title("Tire Monitoring System")

    # Open the tire image
    tire_image = Image.open(tire_image_path)

    # Resize the image to a smaller size for the GUI
    tire_image = tire_image.resize((150, 150))

    # Convert the image to a format that tkinter can use
    tire_photo = ImageTk.PhotoImage(tire_image)

    # Create frames for each tire's information
    for i in range(4):
        frame = ttk.Frame(root, padding="10")
        frame.grid(row=i//2, column=i%2)

        # Place the tire image in each frame
        label = ttk.Label(frame, image=tire_photo)
        label.grid(row=0, column=0, columnspan=2)
        label.image = tire_photo # keep a reference!

        # Labels for the tire's temperature, pressure, and miles
        ttk.Label(frame, text="Temperature:").grid(row=1, column=0, sticky=tk.W)
        ttk.Label(frame, text="Pressure:").grid(row=2, column=0, sticky=tk.W)
        ttk.Label(frame, text="Miles:").grid(row=3, column=0, sticky=tk.W)

        # Labels for the tire's temperature, pressure, and miles values
        # For now, we'll just put placeholder text
        ttk.Label(frame, text="XXX°F").grid(row=1, column=1, sticky=tk.E)
        ttk.Label(frame, text="XXpsi").grid(row=2, column=1, sticky=tk.E)
        ttk.Label(frame, text="XXXXmi").grid(row=3, column=1, sticky=tk.E)

    # Run the application
    root.mainloop()

# Define the path to the tire image
tire_image_path = 'images/tire.png'

create_tire_monitoring_gui(tire_image_path)
