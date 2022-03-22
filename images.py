from hashlib import new
from PIL import Image, ImageFilter

img = Image.open('.\Pokedex\\astro.jpg')

img.thumbnail((400, 400))

img.save('thumbnail.jpg')

# como no era un cuadrado, al hacer 400 x 400 pierde el aspect ratio

print(img.size)
