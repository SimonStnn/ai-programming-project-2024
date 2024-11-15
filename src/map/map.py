import time
from typing import Any
import numpy as np
from numpy import ndarray, dtype, signedinteger

from src.map.tiles import TILE_TRANSLATIONS

TILE_WEIGHTS = {
    1: 1/3,
    2: 1/3,
    3: 1/3,
}

# get a system attibute to randomize the seed
np.random.seed(time.time_ns()%(2**32))

def check_condition_without_breaking(condition: bool) -> bool:
    try:
        return condition
    except:
        return False

def generate_empty_map(size: list[int]) -> ndarray[Any, dtype]:
    return np.zeros(size, dtype=int)

def get_random_tile(weights=None) -> int:
    return np.random.choice(list(TILE_TRANSLATIONS.keys()) , p=weights or list(TILE_WEIGHTS.values()))

def seed_map(_map: ndarray[Any, dtype], start_pos: list[int], chunk_range: list[int]) -> ndarray[Any, dtype]:
    m = _map.copy()
    count_zeros = np.count_nonzero(m[start_pos[0]:start_pos[0]+chunk_range[0], start_pos[1]:start_pos[1]+chunk_range[1]] == 0)
    x_offset = chunk_range[0]//2
    y_offset = chunk_range[1]//2

    a = start_pos[0]-x_offset
    b = start_pos[0]+x_offset

    c = start_pos[1]-y_offset
    d = start_pos[1]+y_offset

    while count_zeros != 0:
        for x in range(a, b):
            for y in range(c, d):
                if m[min(max(x, 0), m.shape[0]-1), min(max(y, 0), m.shape[1]-1)] != 0: continue

                grass_count = 0
                sand_count = 0
                water_count = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue

                        _X = min(max(x+i, 0), m.shape[0]-1)
                        _Y = min(max(y+j, 0), m.shape[1]-1)

                        if m[_X, _Y] == 1:
                            grass_count += 1
                        elif m[_X, _Y] == 2:
                            sand_count += 1
                        elif m[_X, _Y] == 3:
                            water_count += 1

                total = grass_count + sand_count + water_count
                grass_weight = grass_count / total if total != 0 else TILE_WEIGHTS[1]
                sand_weight = sand_count / total if total != 0 else TILE_WEIGHTS[2]
                water_weight = water_count / total if total != 0 else TILE_WEIGHTS[3]

                # Ensure no weight is fully 1
                min_weight = 0.01
                grass_weight = max(min_weight, grass_weight)
                sand_weight = max(min_weight, sand_weight)
                water_weight = max(min_weight, water_weight)

                # Normalize weights to sum to 1
                total_weight = grass_weight + sand_weight + water_weight
                grass_weight /= total_weight
                sand_weight /= total_weight
                water_weight /= total_weight

                weights = [grass_weight, sand_weight, water_weight]

                m[x, y] = get_random_tile(weights)

        count_zeros = np.count_nonzero(m[a:b, c:d] == 0)
    return m

def get_map_chunk(_map: ndarray[Any, dtype], start_pos: list[int], chunk_range: list[int]) -> ndarray[Any, dtype]:
    top_left = [max(0, start_pos[0]-chunk_range[0]//2), max(0, start_pos[1]-chunk_range[1]//2)]
    bottom_right = [min(_map.shape[0], start_pos[0]+chunk_range[0]//2), min(_map.shape[1], start_pos[1]+chunk_range[1]//2)]
    return _map[top_left[0]:bottom_right[0], top_left[1]:bottom_right[1]]


if __name__ == '__main__':
    map = generate_empty_map([100, 100])
    map = seed_map(map, (map.shape[0]//2, map.shape[1]//2), (32,32))
    map = seed_map(map, (map.shape[0]//2+16, map.shape[1]//2), (16,16))

    chunk = get_map_chunk(map, (map.shape[0],map.shape[1]//2), (32, 32))
    print(chunk)
    # write to txt file
    np.savetxt('map.txt', map, fmt='%d')
