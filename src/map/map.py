import numpy as np

type Chunk = np.ndarray[int]
type Tile = int

TILE_TRANSLATIONS = {
    1: 'grass',
    2: 'sand',
    3: 'water',
}

