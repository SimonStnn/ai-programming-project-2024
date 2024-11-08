import pygame
from src.const import RESOLUTIONS
from src.root.main_game import MainGame
from src.root.settings import SettingsWindow

class Window:
    running: bool
    screen: pygame.SurfaceType

    def __init__(self):
        self.running = False
        self.screen = pygame.display.set_mode(RESOLUTIONS[0], self.__flags)
        self.clock = pygame.Clock()
        self.vsync = False
        self.scenes = {
            "MainGame": MainGame(self),
            "SettingsWindow": SettingsWindow(self)
        }
        self.current_scene = self.scenes["MainGame"]
        self.delta = 0
        self.vsync = False


    def set_vsync(self, vsync: bool):
        self.vsync = vsync
        self.screen = pygame.display.set_mode(RESOLUTIONS[0], self.__flags)
        self.clock = pygame.time.Clock()

    @property
    def __flags(self):
        return pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.FULLSCREEN

    def update_scale(self, resolution):
        for scene in self.scenes.values():
            if hasattr(scene, "update_scale"):
                scene.update_scale(resolution)


    @property
    def flags(self):
        return self.__flags

    @property
    def fps(self):
        return pygame.display.get_desktop_refresh_rates()[0] if self.vsync else 60

    def pre_draw_update(self):
        self.delta = self.clock.tick(self.fps) / 1000.0
        self.current_scene.delta = self.delta
        self.current_scene.pre_draw_update()

    def draw(self):
        self.screen.fill("White")
        self.current_scene.draw()
        pygame.display.flip()

    def post_draw_update(self):
        self.current_scene.post_draw_update()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if isinstance(self.current_scene, MainGame): self.swap_scene(self.scenes["SettingsWindow"])
                    else: self.swap_scene(self.scenes["MainGame"])
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

            self.current_scene.process_events(event)



    def swap_scene(self, scene):
        self.current_scene = scene
        self.current_scene.screen = self.screen


    @staticmethod
    def update_caption(text=""):
        pygame.display.set_caption(text)

    def run(self):
        self.running = True
        while self.running:
            self.process_events()
            self.pre_draw_update()
            self.draw()
            self.post_draw_update()