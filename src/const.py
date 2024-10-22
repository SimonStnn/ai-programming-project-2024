WINDOW_SIZE = (1400, 800)


BLOCKSIZE = (32, 32)

# blocksize scaled to the window size
SCALED = (WINDOW_SIZE[0] // BLOCKSIZE[0], WINDOW_SIZE[1] // BLOCKSIZE[1])
# to fully fill the screen you need a list[list[int]] with the same dimensions as SCALED
PREGENERATED_LEVEL = [[ 0 for _ in range(SCALED[0] + 1)] for _ in range(SCALED[1] + 1)]