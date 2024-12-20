import pygame
from pygame import font
from pygame.math import Vector2
from pygame.transform import rotozoom
from models import *
from utils import *
import random
import SRplanets

class StarboardRenegade():
    HUD_FONT_SIZE = 22
    def __init__(self):
        self._init_pygame()

        # Pygame Screen Setup
        PLAYER_FULLSCREEN_CHOICE = int(input('FULLSCREEN? 1=yes, 2=no\n>>>: '))
        if PLAYER_FULLSCREEN_CHOICE == 1: self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        else: self.screen = pygame.display.set_mode((1100,700))
        SCREEN_INFO = pygame.display.Info()
        self.screen_height = SCREEN_INFO.current_h
        self.screen_width = SCREEN_INFO.current_w
        BACKGROUND = load_sprite("space",False)
        DEFAULT_BACKGROUND_SIZE = (self.screen_width,self.screen_height)
        BACKGROUND = pygame.transform.scale(BACKGROUND,DEFAULT_BACKGROUND_SIZE)
        if self.screen_height > self.screen_width: BACKGROUND = pygame.transform.rotate(BACKGROUND,90)
        self.background = BACKGROUND
        self.clock = pygame.time.Clock()
        self.spaceship = Vessel((self.screen_width / 2, self.screen_height / 2))
        self.compass = ScreenPrint('(x,y)',self.spaceship.position)
        self.origin = GameObject((0,0),load_sprite('cube'),0)
        self.feducials = create_feducials(13,self.screen)
        self.border = JumpBorder((0,0))
        self.waypoint = Waypoint((self.screen_width / 2, (self.screen_height / 2)),self.spaceship)
        self.planets = [GameObject((500,500),load_sprite('sampson'),0)]
        # galaxy

    def main_loop(self):
        while True:
            self._handle_input()
            self._process_game_logic()
            self._draw()

    def _init_pygame(self):
        pygame.init()
        pygame.display.set_caption('Starboard, Renegade!')

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                quit()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT] or is_key_pressed[pygame.K_d]: self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT] or is_key_pressed[pygame.K_a]: self.spaceship.rotate(clockwise=False)
            #if is_key_pressed[pygame.K_UP]: self.spaceship.accelerate()

        if is_key_pressed[pygame.K_UP] or is_key_pressed[pygame.K_w]:
            if self.spaceship.fuel[0] > -1:  # If you have fuel, accel fully., changed to -1 from 0 for troubleshooting purposes
                #self.spaceship.fuel[0] -= 0.1
                for p in self.planets:
                    p.velocity -= self.spaceship.direction * 0.25
                for marker in self.feducials:
                    marker.velocity -= self.spaceship.direction * marker.layer[0]
                self.border.inertia(self.spaceship.direction)
                #print(self.spaceship.direction)
                #print(self.border.N.position)
                self.waypoint.velocity -= self.spaceship.direction
                self.origin.velocity -= self.spaceship.direction

            if self.spaceship.fuel[0] <= -1:  # If out of fuel, accel very slow. changed from 0 to -2 for 
                for p in self.planets:
                    p.velocity -= self.spaceship.direction * 0.01
                for marker in self.feducials:
                    marker.velocity += self.spaceship.direction * marker.layer[1]
                #self.border.velocity -= self.spaceship.direction

        if is_key_pressed[pygame.K_DOWN] or is_key_pressed[pygame.K_s]:
            for marker in self.feducials: marker.velocity -= marker.velocity * 0.05
            #self.border.velocity -= self.border.velocity * 0.05
            for p in self.planets: p.velocity -= p.velocity * 0.05
            for obj in self._get_map_objects():
                obj.velocity -= obj.velocity * 0.05
            for border in self.border.all: border.velocity -= border.velocity * 0.05
            self.origin.velocity -= self.origin.velocity * 0.05


    def _process_game_logic(self):
        for game_object in self._get_game_objects():
            if isinstance(game_object,Feducial):
                game_object.move(self.screen)
            else: game_object.move()
        for map_object in self._get_map_objects(): map_object.move()
        second_position = False
        if self.spaceship.position.distance_to(self.planets[0].position) < 200: second_position = True
        self.waypoint.point_at(self.border.S,second_position=second_position) #self.planets[0]
        self.border.move()
        self.border.realign(self.spaceship)
        self.origin.move()
        self.compass.text = '('+str(self.origin.position[0])+', '+str(self.origin.position[0])+')'
        self.compass.position = self.origin.position

    def _draw(self,troubleshooting=False):
        self.screen.blit(self.background, (0,0))
        for game_object in self._get_game_objects():
            game_object.draw(self.screen)
        self.border.draw(self.screen)
        self.spaceship.draw(self.screen)
        second_position = False
        if self.spaceship.position.distance_to(self.border.S.position) < 200: second_position = True
        self.waypoint.draw(self.screen,second_position)

        self.origin.draw(self.screen)
        self.compass.draw(self.screen)

        if troubleshooting: print('x')
        pygame.display.flip()
        self.clock.tick(60)

    def _get_game_objects(self):
        game_objects = [*self.feducials,*self.planets] #*self.feducials
        return game_objects

    def _get_map_objects(self):
        map_objects = [] #self.border
        return map_objects

