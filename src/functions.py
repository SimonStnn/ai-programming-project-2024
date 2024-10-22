import os

def relative_path(base_path: str, target_path: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", base_path, target_path))

def src_path(target_path: str) -> str:
    return relative_path("src", target_path)

def img_path(target_path: str) -> str | None:
    if (e := relative_path("images", target_path)).split(".")[-1] not in ["png", "jpg", "jpeg", "svg"]: raise ValueError("Invalid image file")
    if not os.path.exists(e): return None
    return e



if __name__ == "__main__":
    print(img_path("logo.png"))