from pyzbar.pyzbar import decode
from PIL import Image

image_path = "image4_qrcode.jpg"  # Change this to your file path

image = Image.open(image_path)
decoded_objects = decode(image)

for obj in decoded_objects:
    print("Decoded Data:", obj.data.decode("utf-8"))