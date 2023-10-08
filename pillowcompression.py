from PIL import Image
import os

image = Image.open('images/push.jpg')

width, height = image.size
# new_size = (width//2, height//2)
new_size = (16, 16)
resized_image = image.resize(new_size)

resized_image.save('compressed_image.jpg', optimize=True, quality=50)

original_size = os.path.getsize('images/push.jpg')
compressed_size = os.path.getsize('compressed_image.jpg')

print("Original Size: ", original_size)
print("Compressed Size: ", compressed_size)