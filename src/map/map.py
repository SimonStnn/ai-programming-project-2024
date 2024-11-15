import time
from typing import Any
import numpy as np
from numpy import ndarray, dtype, signedinteger

from src.map.tiles import TILE_TRANSLATIONS, Tile

MIN_WEIGHT = 0.01
TILE_WEIGHTS = {
    1: 1 / 3,
    2: 1 / 3,
    3: 1 / 3,
}

# get a system attibute to randomize the seed
np.random.seed(time.time_ns() % (2 ** 32))


def check_condition_without_breaking(condition: bool) -> bool:
    try:
        return condition
    except:
        return False


def generate_empty_map(size: list[int]) -> ndarray[Any, dtype]:
    return np.zeros(size, dtype=int)


def get_random_tile(weights=None) -> int:
    return np.random.choice(list(TILE_TRANSLATIONS.keys()), p=weights or list(TILE_WEIGHTS.values()))


def seed_map(_map: ndarray[Any, dtype], start_pos: list[int], chunk_range: list[int]) -> ndarray[Any, dtype]:
    m = _map.copy()
    count_zeros = np.count_nonzero(
        m[start_pos[0]:start_pos[0] + chunk_range[0], start_pos[1]:start_pos[1] + chunk_range[1]] == 0)
    x_offset = chunk_range[0] // 2
    y_offset = chunk_range[1] // 2

    a = start_pos[0] - x_offset
    b = start_pos[0] + x_offset

    c = start_pos[1] - y_offset
    d = start_pos[1] + y_offset

    blocks = TILE_TRANSLATIONS.keys()

    while count_zeros != 0:
        for x in range(a, b):
            for y in range(c, d):
                if m[min(max(x, 0), m.shape[0]-1), min(max(y, 0), m.shape[1]-1)] != 0: continue

                block_counts = {block: 0 for block in blocks}

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue

                        _X = min(max(x + i, 0), m.shape[0] - 1)
                        _Y = min(max(y + j, 0), m.shape[1] - 1)

                        block_counts[m[_X, _Y]] += 1

                total = sum(block_counts.values())
                block_weights = {block: max(MIN_WEIGHT, block_counts[block] / total) if total != 0 else MIN_WEIGHT for
                                 block in blocks}
                total_block_weights = sum(block_weights.values())
                for block in block_weights:
                    block_weights[block] /= total_block_weights

                weights = [block_weights[block] for block in blocks]

                m[x, y] = get_random_tile(weights)

        count_zeros = np.count_nonzero(m[a:b, c:d] == 0)
    return m


def get_map_chunk(_map: ndarray[Any, dtype], start_pos: list[int], chunk_range: list[int]) -> ndarray[Any, dtype]:
    return _map[start_pos[0]:start_pos[0] + chunk_range[0], start_pos[1]:start_pos[1] + chunk_range[1]]


if __name__ == '__main__':
    map = generate_empty_map([100, 100])
    map = seed_map(map, (map.shape[0] // 2, map.shape[1] // 2), (32, 32))
    map = seed_map(map, (map.shape[0] // 2 + 16, map.shape[1] // 2), (16, 16))
    # write to txt file
    np.savetxt('map.txt', map, fmt='%d')
