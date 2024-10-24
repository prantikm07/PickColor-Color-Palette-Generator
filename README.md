# 🎨 Color Palette Generator

This Python-based application allows users to extract dominant colors from any image and generate a color palette with corresponding hex codes. The hex codes can be easily copied with a single click. The application features a simple and user-friendly graphical interface (GUI) using Tkinter.

## 🖼 Features
- **Extract Colors**: Extract up to 6 dominant colors from any image.
- **Copy Hex Codes**: Hex codes for each color are displayed below the palette and can be copied by clicking on them.
- **File Browser**: Easily select images via a file browser.
- **Supports Multiple Formats**: Works with `.jpg`, `.jpeg`, and `.png` image files.


## 🛠 How It Works
1. Browse for an image file using the "Browse" button or manually enter the image path.
2. Click the "Generate Palette" button to extract and display a color palette.
3. Copy any hex code by clicking on it, and a confirmation message will appear.

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/color-palette-generator.git
   cd color-palette-generator
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python color_palette.py
   ```

## 📋 Requirements
- Python 3.x
- `colorgram.py`: Extracts the colors from images.
- `Pillow`: Handles image manipulation.
- `pyperclip`: Copies the hex codes to your clipboard.
- `Tkinter`: The built-in library for GUI creation.

## 📄 File Structure
- `color_palette.py`: The main application script.
- `requirements.txt`: File with all required dependencies.

## 🧰 Dependencies
Listed in `requirements.txt`:
```plaintext
colorgram.py==1.2.0
Pillow==9.3.0
pyperclip==1.8.2
```

To install all dependencies:
```bash
pip install -r requirements.txt
```

## 👨‍💻 Usage

1. Run the script `color_palette.py`.
2. Select or input the path of your image file.
3. Click the **Generate Palette** button.
4. The color palette will be displayed, and hex codes can be copied by clicking them.

## ✨ Example

After selecting an image:

- The generated palette will appear.
- Hex values like `#FF5733`, `#33FF57`, etc., are displayed.
- Click on any hex value to copy it to your clipboard.

## 🤝 Contributing
Feel free to open issues or submit pull requests to help improve this project!

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
