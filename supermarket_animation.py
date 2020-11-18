from PIL import Image
import numpy as np

im = Image.open('images/supermarket.png')
market = np.array(im)
print(market.shape, market.dtype)

im2 = Image.open('images/tiles.png')
tiles = np.array(im2)
print(tiles.shape, tiles.dtype)

x = 4 * 32   # 5th column starting from 0
y = 1 * 32   # 2nd row
apple = tiles[y:y + 32, x:x + 32]


tx = 13 * 32
ty = 2 * 32
market[ty:ty+32, tx:tx+32] = apple

im = Image.fromarray(market)
im.save('./images/supermarket_filled.png')
