import os, platform, sys

if platform.system() == "Windows":
    def get_keyboard_layout():
        import locale
        current_locale = locale.getdefaultlocale()[0]
        azerty_locales = ['fr_FR', 'be_FR', 'fr_BE', 'fr_LU', 'fr_CH', 'fr_MC']
        return "AZERTY" if current_locale in azerty_locales else "QWERTY"


def relative_path(base_path: str, target_path: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", base_path, target_path))

def src_path(target_path: str) -> str:
    return relative_path("src", target_path)

def img_path(target_path: str) -> str | None:
    if (e := relative_path("images", target_path)).split(".")[-1] not in ["png", "jpg", "jpeg", "svg"]: raise ValueError("Invalid image file")
    if not os.path.exists(e): return None
    return e

def get_animals_path(animal) -> str:
    return img_path(f"Animals/{animal}.png")

def get_character_path(character) -> str:
    return img_path(f"Characters/{character}.png")


if __name__ == "__main__":
    print(get_keyboard_layout())