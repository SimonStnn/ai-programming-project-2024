import pygame
from pygame.rect import Rect
from pygame_gui import UIManager
from pygame_gui.elements import UIButton
import pygame_gui
from src.const import RESOLUTIONS


class SettingsWindow:
    def __init__(self, master):
        self.master = master
        self.current_resolution = 0
        self.delta = 0
        self.create_ui() # making it a method so it can be called again when the resolution changes

    def create_ui(self):
        self.ui_manager = UIManager(self.master.screen.get_size())
        self.ui_manager.set_visual_debug_mode(True)

        self.dynamic_dimension_window = pygame_gui.ui_manager.UIContainer(
            relative_rect=Rect((0, 0), self.master.screen.get_size()),
            manager=self.ui_manager,
            visible=True
        )

        self.continue_button = UIButton(
            relative_rect=pygame.Rect(30, 20, -1, -1),
            text='Continue', manager=self.ui_manager,
            container=self.dynamic_dimension_window,
            tool_tip_text='Return to the main game',
            anchors={
                'left': 'left',
                'right': 'right',
                'top': 'top',
                'bottom': 'bottom'
            }
        )
        self.resolution_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(30, 60, -1, -1),
            text=f"current_resolution: {RESOLUTIONS[self.current_resolution]}", manager=self.ui_manager,
            container=self.dynamic_dimension_window,
            tool_tip_text='Change the resolution of the game',
            command=self.pressed_resolution_button,
            anchors={
                'left': 'left',
                'right': 'right',
                'top': 'top',
                'bottom': 'bottom'
            }
        )

        self.fullscreen_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(30, 100, -1, -1),
            text='Toggle Fullscreen', manager=self.ui_manager,
            container=self.dynamic_dimension_window,
            tool_tip_text='Toggle fullscreen mode',
            command=self.pressed_fullscreen_button,
            anchors={
                'left': 'left',
                'right': 'right',
                'top': 'top',
                'bottom': 'bottom'
            }
        )

        self.quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(30, 140, -1, -1),
            text='Quit', manager=self.ui_manager,
            container=self.dynamic_dimension_window,
            tool_tip_text='Quit the game',
            command=self.pressed_quit_button,
            anchors={
                'left': 'left',
                'right': 'right',
                'top': 'top',
                'bottom': 'bottom'
            }
        )

    def pressed_quit_button(self):
        self.master.running = False
        # maybe later implement a data saving system here

    def pressed_fullscreen_button(self):
        self.master.flags ^= pygame.FULLSCREEN
        self.master.screen = pygame.display.set_mode(RESOLUTIONS[self.current_resolution], self.master.flags)

    def pressed_resolution_button(self):
        self.current_resolution = (self.current_resolution + 1) % len(RESOLUTIONS)
        self.resolution_button.set_text(f"current_resolution: {RESOLUTIONS[self.current_resolution]}")
        self.change_resolution(RESOLUTIONS[self.current_resolution])

    def change_resolution(self, resolution):
        # check if currently in fullscreen
        if self.master.screen.get_flags() & pygame.FULLSCREEN: self.master.flags |= pygame.FULLSCREEN
        else: self.master.flags &= ~pygame.FULLSCREEN
        self.master.screen = pygame.display.set_mode(resolution, self.master.flags)
        self.master.current_scene.screen = self.master.screen
        self.create_ui()


    def pre_draw_update(self):
        pass

    def draw(self):
        self.ui_manager.draw_ui(self.master.screen)

    def post_draw_update(self):
        self.ui_manager.update(self.delta)

    def process_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.continue_button:
                self.master.swap_scene(self.master.scenes["MainGame"])
        self.ui_manager.process_events(event)