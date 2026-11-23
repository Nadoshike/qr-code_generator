# Custom QR Code Generator

A command-line Python tool that encodes URLs, text, or credentials into customizable high-resolution PNG QR codes.

## Windows & VS Code Setup Instructions

1. **Extract this folder** into `C:\Users\tolov\Documents\Project\qr-code-generator`.
2. **Open the folder in VS Code**:
   - Open VS Code, click `File > Open Folder`, and select `qr-code-generator`.
3. **Open the Integrated Terminal** (`Terminal > New Terminal`).
4. **Set up your Python environment**:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Usage
```cmd
# Generate a standard QR code (saves as qrcode.png)
python qr_generator.py "https://github.com"

# Specify a custom filename and colors
python qr_generator.py "https://github.com" -o github_qr.png --fill navy --bg white --size 12
```
