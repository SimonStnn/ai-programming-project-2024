import pygame
from src.const import WINDOW_SIZE
from pygame_gui import UIManager, elements, UI_BUTTON_PRESSED
from src.root.main_game import MainGame

class Window:
    running: bool
    screen: pygame.SurfaceType

    def __init__(self):
        self.running = False
        self.flags = pygame.HWACCEL | pygame.DOUBLEBUF | pygame.RESIZABLE | pygame.SCALED
        self.screen = pygame.display.set_mode(WINDOW_SIZE, self.flags)
        self.clock = pygame.Clock()
        self.vsync = False
        self.current_scene = MainGame()
        self.manager = UIManager(WINDOW_SIZE)
        self.hello_button = elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Say Hello', manager=self.manager)
        self.delta = 0



    def pre_draw_update(self):
        self.delta = self.clock.tick(pygame.display.get_desktop_refresh_rates()[0] if self.vsync else 60) / 1000.0
        self.current_scene.delta = self.delta
        self.current_scene.pre_draw_update()

    def draw(self):
        self.screen.fill("White")
        self.current_scene.draw()
        self.manager.draw_ui(self.screen)
        pygame.display.flip()

    def post_draw_update(self):
        self.manager.update(self.delta)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

            if event.type == UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    self.vsync = not self.vsync

            self.manager.process_events(event)





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