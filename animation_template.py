import time
import cv2
import numpy as np
import pandas as pd
from customer_animated import CustomerAnimated

transition_matrix = pd.read_csv("./data/transition_matrix.csv")
transition_matrix.set_index("location", inplace=True)


TILE_SIZE = 32
OFS = 50
MARKET = """
##################
##..............##
##..db..s#..x#..##
##..dp..s#..x#..##
##..da..s#..x#..##
##..dc..s#..x#..##
##..dg..s#..x#..##
##...............#
##..C#..C#..C#...#
##..##..##..##...#
##...............#
##############GG##
""".strip()

# Animate customers through the supermarket
# (skeleton code from Spiced 8.7.)


class SupermarketMap:
    """Visualizes the supermarket background"""

    def __init__(self, layout, tiles):
        """
        layout : a string with each character representing a tile
        tile   : a numpy array containing the tile image
        """
        self.tiles = tiles
        self.contents = [list(row) for row in layout.split('\n')]
        self.xsize = len(self.contents[0])
        self.ysize = len(self.contents)
        self.image = np.zeros(
            (self.ysize * TILE_SIZE, self.xsize * TILE_SIZE, 3), dtype=np.uint8)
        self.prepare_map()

    def get_tile(self, char):
        """returns the array for a given tile character"""
        if char == '#':
            return self.tiles[0:32, 0:32]
        elif char == 'G':
            return self.tiles[7*32:8*32, 3*32:4*32]
        elif char == 'C':
            return self.tiles[2 * 32:3 * 32, 8 * 32:9 * 32]
        elif char == "b":
            return self.tiles[0 * 32:1 * 32, 4 * 32:5 * 32]
        elif char == "p":
            return self.tiles[1 * 32:2 * 32, 4 * 32:5 * 32]
        elif char == "a":
            return self.tiles[5 * 32:6 * 32, 4 * 32:5 * 32]
        elif char == "c":
            return self.tiles[7 * 32:8 * 32, 4 * 32:5 * 32]
        elif char == "g":
            return self.tiles[4 * 32:5 * 32, 4 * 32:5 * 32]
        elif char == 'd':
            return self.tiles[6 * 32:7 * 32, 12 * 32:13 * 32]
        elif char == 's':
            return self.tiles[2 * 32:3 * 32, 3*32: 4*32]
        elif char == 'x':
            return self.tiles[3 * 32:4 * 32, 13 * 32: 14*32]
        else:
            return self.tiles[32:64, 64:96]

    def prepare_map(self):
        """prepares the entire image as a big numpy array"""
        for y, row in enumerate(self.contents):
            for x, tile in enumerate(row):
                bm = self.get_tile(tile)
                self.image[y * TILE_SIZE:(y+1)*TILE_SIZE,
                           x * TILE_SIZE:(x+1)*TILE_SIZE] = bm

    def draw(self, frame, offset=OFS):
        """
        draws the image into a frame
        offset pixels from the top left corner
        """
        frame[OFS:OFS+self.image.shape[0], OFS:OFS +
              self.image.shape[1]] = self.image

    def write_image(self, filename):
        """writes the image into a file"""
        cv2.imwrite(filename, self.image)


if __name__ == '__main__':
    background = np.zeros((700, 1000, 3), np.uint8)
    tiles = cv2.imread('./images/tiles.png')

    market = SupermarketMap(MARKET, tiles)
    cust1 = CustomerAnimated(market,
                             tiles[3 * 32:4 * 32, 0 * 32:1 * 32], 3, 4)

    while True:
        frame = background.copy()
        market.draw(frame)
        time.sleep(5)

        print(cust1.x, cust1.y)
        cust1.move("up")
        print(cust1.x, cust1.y)
        cust1.draw(frame)
        cv2.imshow('frame', frame)

        key = chr(cv2.waitKey(1) & 0xFF)
        if key == 'q':
            break

    cv2.destroyAllWindows()

    market.write_image("./images/supermarket_animation.png")
