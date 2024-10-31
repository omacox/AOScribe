import os
from PIL import Image


def convert_jpg_to_png(subfolder_path):
    # Ensure the subfolder exists
    if not os.path.exists(subfolder_path):
        print("Subfolder path does not exist.")
        return

    # Loop through each file in the subfolder
    for filename in os.listdir(subfolder_path):
        if filename.lower().endswith(".jpeg"):
            print(filename)
            # Full path of the JPG file
            jpg_path = os.path.join(subfolder_path, filename)

            # Define the PNG filename and path
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(subfolder_path, png_filename)

            # Open and convert the image
            with Image.open(jpg_path) as img:
                img.save(png_path, "PNG")

            print(f"Converted {filename} to {png_filename}")

            # Optional: Remove the original JPG file after conversion
            os.remove(jpg_path)
            print(f"Deleted original file: {filename}")


# Replace './images/' with the path to your subfolder
convert_jpg_to_png("./images/")
