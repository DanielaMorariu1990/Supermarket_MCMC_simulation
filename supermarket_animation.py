from PIL import Image
import numpy as np

im = Image.open('images/supermarket.png')
market = np.array(im)
print(market.shape, market.dtype)