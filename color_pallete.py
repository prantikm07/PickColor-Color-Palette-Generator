import tkinter as tk
from tkinter import filedialog, messagebox
import colorgram
from PIL import Image, ImageDraw, ImageTk
import pyperclip

# Function to extract colors and return hex values
def extract_colors(image_path, num_colors):
    colors = colorgram.extract(image_path, num_colors)
    hex_colors = []
    for color in colors:
        rgb = color.rgb
        hex_colors.append('#{:02x}{:02x}{:02x}'.format(rgb.r, rgb.g, rgb.b))
    return hex_colors

# Function to create a color palette image
def create_palette_image(colors, palette_width=500, palette_height=100):
    block_width = palette_width // len(colors)
    palette = Image.new('RGB', (palette_width, palette_height))
    draw = ImageDraw.Draw(palette)

    for i, color in enumerate(colors):
        x0 = i * block_width
        x1 = (i + 1) * block_width
        draw.rectangle([x0, 0, x1, palette_height], fill=color)

    return palette

# Function to display the palette in Tkinter
def generate_palette():
    image_path = entry.get()
    try:
        # Extract and display palette
        colors = extract_colors(image_path, 6)
        palette_image = create_palette_image(colors)
        palette_tk = ImageTk.PhotoImage(palette_image)
        
        # Display the image
        palette_label.config(image=palette_tk)
        palette_label.image = palette_tk

        # Display hex codes and add copy functionality
        for i, color in enumerate(colors):
            hex_label = hex_labels[i]
            hex_label.config(text=color)
            hex_label.bind("<Button-1>", lambda e, c=color: copy_to_clipboard(c))

    except Exception as e:
        messagebox.showerror("Error", f"Failed to generate palette: {e}")

# Function to open file dialog and set the image path
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Function to copy hex code to clipboard
def copy_to_clipboard(hex_code):
    pyperclip.copy(hex_code)
    messagebox.showinfo("Copied", f"Hex code {hex_code} copied to clipboard!")

# Create the Tkinter window
root = tk.Tk()
root.title("Color Palette Generator")

# Entry and browse button for image path
frame = tk.Frame(root)
frame.pack(pady=10)

entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=10)

browse_button = tk.Button(frame, text="Browse", command=open_file_dialog)
browse_button.pack(side=tk.LEFT)

# Button to generate palette
generate_button = tk.Button(root, text="Generate Palette", command=generate_palette)
generate_button.pack(pady=10)

# Label to display the palette image
palette_label = tk.Label(root)
palette_label.pack()

# Hex code labels for colors
hex_labels_frame = tk.Frame(root)
hex_labels_frame.pack(pady=10)

hex_labels = [tk.Label(hex_labels_frame, text="", font=('Arial', 12)) for _ in range(6)]
for label in hex_labels:
    label.pack(side=tk.LEFT, padx=10)

# Start the Tkinter event loop
root.mainloop()
