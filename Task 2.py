from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")  # Convert image to RGB mode

    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Get the pixel value
            encrypted_pixel = (b, g, r)  # Encrypt the pixel

            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img = img.convert("RGB")  # Convert image to RGB mode

    pixels = img.load()
    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]  # Get the pixel value
            decrypted_pixel = (b, g, r)  # Decrypt the pixel

            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

# Image paths
input_image = "C:/Users/titan/Desktop/path/Phishing.png"
encrypted_image = "C:/Users/titan/Desktop/path/encrypted_image.jpg"
decrypted_image = "C:/Users/titan/Desktop/path/decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)
