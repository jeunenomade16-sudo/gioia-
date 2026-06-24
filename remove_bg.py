import sys
import io
from PIL import Image
from rembg import remove

def remove_background(input_path, output_path):
    print(f"Processing {input_path}...")
    with open(input_path, 'rb') as i:
        input_data = i.read()
    
    # Process the image to remove background
    output_data = remove(input_data)
    
    # Save the result
    with open(output_path, 'wb') as o:
        o.write(output_data)
    print(f"Saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_bg.py <input> <output>")
        sys.exit(1)
    
    remove_background(sys.argv[1], sys.argv[2])
