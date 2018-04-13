from PIL import Image
import zbarlight


def qr_decode(img):
 file_path = img
 with open(file_path, 'rb') as image_file:
     image = Image.open(image_file)
     image.load()
 converted_image = image.convert('L')  # Convert image to gray scale (8 bits per pixel).
 image.close() 
 raw = converted_image.tobytes()  # Get image data.
 width, height = converted_image.size  # Get image size.
 code = zbarlight.qr_code_scanner(raw, width, height)
 return img + ' QR code: %s' % code.decode()

print qr_decode("img0.png")
print qr_decode("img1.png")
print qr_decode("img2.png")
print qr_decode("img3.png")
print qr_decode("img4.png")
