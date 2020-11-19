## Create a supermarket image

from PIL import Image
import numpy as np
import operator
from supermarket_simulation import Supermarket

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

# Customer icon
x = 15 * 32   
y = 10 * 32   
customer = tiles[y:y + 32, x:x + 32]
tx = 0 * 32
ty = 7 * 32
market[ty:ty+32, tx:tx+32] = customer

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

## Pseudocode animation path
def obstacles -> aisles

entrance = [0:32, 14*32:15*32+32] #make a function out of this, apply to all aisles
entrance = [0, 14:15]
drinks = [2:6, 4]
dairy = [2:6,5]
spices = [2:6,8:9]
fruit = [2:6,12:13]
checkout1 = [8:9,4:5]
checkout2 = [8:9,8:9]
checkout3 = [8:9,12:13]
checkout = [checkout1, checkout2, checkout3]

"""
Path finding algirthm ->astar.py
"""