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
        m[max(start_pos[0], 0):max(start_pos[0] + chunk_range[0], 0), max(start_pos[1], 0):max(start_pos[1] + chunk_range[1], 0)] == 0)
    x_offset = chunk_range[0] // 2
    y_offset = chunk_range[1] // 2

    a = max(start_pos[0] - x_offset, 0)
    b = max(start_pos[0] + x_offset, 0)

    c = max(start_pos[1] - y_offset, 0)
    d = max(start_pos[1] + y_offset, 0)

    blocks = TILE_TRANSLATIONS.keys()

    while count_zeros != 0:
        for x in range(max(a, 0), min(b, m.shape[0])):
            for y in range(max(c, 0), min(d, m.shape[1])):
                if m[x, y] != 0:
                    continue

                block_counts: dict[int, float] = {block: 0 for block in blocks}

                for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    _X = min(max(x + dx, 0), m.shape[0] - 1)
                    _Y = min(max(y + dy, 0), m.shape[1] - 1)

                    block_counts[m[_X, _Y]] += 1

                # Calculate weights
                total_count = sum(block_counts.values())
                block_weights = {
                    block: max(MIN_WEIGHT, count / total_count) if total_count > 0 else MIN_WEIGHT
                    for block, count in block_counts.items()
                }

                # Normalize weights
                total_weight = sum(block_weights.values())
                weights = [block_weights[block] / total_weight for block in blocks]

                m[min(max(x, 0), m.shape[0]-1), min(max(y, 0), m.shape[1]-1)] = get_random_tile(weights)

        count_zeros = np.count_nonzero(m[a:b, c:d] == 0)
    return m

def get_map_chunk(_map: ndarray[Any, dtype], start_pos: list[int], chunk_range: list[int]) -> ndarray[Any, dtype]:
    x_offset = chunk_range[0] // 2
    y_offset = chunk_range[1] // 2

    a = max(start_pos[0] - x_offset, 0)
    b = min(start_pos[0] + x_offset + 1, _map.shape[0])

    c = max(start_pos[1] - y_offset, 0)
    d = min(start_pos[1] + y_offset + 1, _map.shape[1])

    return _map[a:b, c:d]

if __name__ == '__main__':
    map = generate_empty_map([100, 100])
    map = seed_map(map, (map.shape[0] // 2, map.shape[1] // 2), (32, 32))
    map = seed_map(map, (map.shape[0] // 2 + 16, map.shape[1] // 2), (16, 16))
    # write to txt file
    np.savetxt('map.txt', map, fmt='%d')
