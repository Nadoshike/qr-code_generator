import os
import argparse
import qrcode

def generate_qr(data: str, output_file: str, fill_color: str = "black", back_color: str = "white", box_size: int = 10):
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=box_size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    if not output_file.lower().endswith(".png"):
        output_file += ".png"
        
    img.save(output_file)
    print(f"QR code generated successfully: {os.path.abspath(output_file)}")

def main():
    parser = argparse.ArgumentParser(description="Generate a custom PNG QR code from a URL or text string.")
    parser.add_argument("data", type=str, help="The URL or text to encode inside the QR code")
    parser.add_argument("-o", "--output", type=str, default="qrcode.png", help="Output PNG filename (default: qrcode.png)")
    parser.add_argument("--fill", type=str, default="black", help="Foreground color (default: black)")
    parser.add_argument("--bg", type=str, default="white", help="Background color (default: white)")
    parser.add_argument("--size", type=int, default=10, help="Pixel size of each QR box (default: 10)")

    args = parser.parse_args()
    generate_qr(args.data, args.output, args.fill, args.bg, args.size)

if __name__ == "__main__":
    main()
