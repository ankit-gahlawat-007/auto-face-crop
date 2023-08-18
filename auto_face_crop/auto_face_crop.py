from PIL import Image
from autocrop import Cropper
from rembg import remove
import cv2

# Step-1: Remove the background and set it to white color

input_path = 'data/a.jpeg'
rembg_path = 'data/rembg.jpeg'

input = cv2.imread(input_path)
rembg = remove(input,bgcolor=[255,255,255,255])
cv2.imwrite(rembg_path, rembg)

# Step-2: Make the image square, so that it is easier to square crop the entire head including the hairs and neck

def make_square(im, min_size=256, fill_color=(255, 255, 255, 255)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

input = Image.open(rembg_path)
square_image = make_square(input)

square_image_path = 'data/square_image.png'
square_image.save(square_image_path)

# Step-3: Crop the image with detected face as face_percent of the total output image

cropper = Cropper(face_percent=40)

cropped_array = cropper.crop(square_image_path)

cropped_image_path = 'data/cropped_image.jpeg'

if cropped_array.any():
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save(cropped_image_path)
