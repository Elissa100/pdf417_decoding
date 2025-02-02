from PIL import Image as PIL
from pdf417decoder import PDF417Decoder
import os

def decode_pdf417(image_path):
    # Validating image path
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
        
    try:
        # Image loading using Pillow
        pil_image = PIL.open(image_path)
        
        # Initializing PDF417 decoder
        decoder = PDF417Decoder(pil_image)
        
        # Decoding barcode
        decode_result = decoder.decode()
        
        if decode_result > 0:
            # Extracting decoded data
            decoded_data = decoder.barcode_data_index_to_string(0)
            
            # Returning the decoded data
            return decoded_data
        else:
            return "No barcode detected"
            
    except PIL.UnidentifiedImageError:
        raise ValueError("Invalid image format")
    except Exception as e:
        raise RuntimeError(f"Decoding error: {str(e)}")

if __name__ == "__main__":
    try:
        result = decode_pdf417("IMG_1903 2.jpg")
        print(f"Decoded Data: \n{result}")
    except Exception as e:
        print(f"Error: {str(e)}")
