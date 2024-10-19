import os

def relative_path(base_path: str, target_path: str) -> str:
    return os.path.relpath(target_path, start=base_path)

def src_path(target_path: str) -> str:
    return relative_path("src", target_path)

def img_path(target_path: str) -> str:
    return relative_path("image", target_path)

if __name__ == "__main__":
    print(relative_path("src", "src/game_handler/image/image.py"))