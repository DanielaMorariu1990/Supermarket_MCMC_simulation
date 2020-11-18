## Create a supermarket image

from PIL import Image
import numpy as np

im = Image.open('images/supermarket.png')
market = np.array(im)
print(market.shape, market.dtype)

im2 = Image.open('images/tiles.png')
tiles = np.array(im2)
print(tiles.shape, tiles.dtype)

# Fruits icon
x = 4 * 32   # 5th column starting from 0
y = 1 * 32   # 2nd row
apple = tiles[y:y + 32, x:x + 32]


tx = 13 * 32
ty = 2 * 32
market[ty:ty+32, tx:tx+32] = apple

# Drinks icon
x = 13 * 32   
y = 6 * 32   
drink = tiles[y:y + 32, x:x + 32]
tx = 4 * 32
ty = 6 * 32
market[ty:ty+32, tx:tx+32] = drink

# Dairy icon
x = 11 * 32   
y = 7 * 32   
drink = tiles[y:y + 32, x:x + 32]
tx = 5 * 32
ty = 2 * 32
market[ty:ty+32, tx:tx+32] = drink

# Spices icon
x = 9 * 32   
y = 6 * 32   
drink = tiles[y:y + 32, x:x + 32]
tx = 9 * 32
ty = 6 * 32
market[ty:ty+32, tx:tx+32] = drink

im = Image.fromarray(market)
im.save('./images/supermarket_filled.png')


"""
# generate supermarket image with numpy
a = np.zeros((300, 500, 3), dtype=np.uint8)
a[50:200, 50:150, 2] = 255
a[50:200, 200:300, 2] = 255
a[50:200, 350:450, 2] = 255
a[250:, 450:, 0] = 255
im = Image.fromarray(a)
im.save('./images/supermarket_generated.png')
"""