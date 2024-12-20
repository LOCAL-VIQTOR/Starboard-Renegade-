from pygame.math import Vector2
from pygame.transform import rotozoom
from pygame import font, draw
import random
from SRvessels import SpaceVessel
import SRplanets
from SRvessels import SpaceVessel as srv
from math import radians, sin, cos, tan
from utils import *

from utils import load_sprite, wrap_position, get_random_velocity

# PYGAME FONT TO PROB GO IN UTILS
font.init()
my_font = font.SysFont('PV 6x8', 16)
label_font = font.SysFont('Bahnschrift', 22)

UP = Vector2(0, -1)


class GameObject:
    def __init__(self, position, sprite, velocity):

        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):

        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = (self.position + self.velocity) #surface?

    def collides_with(self, other_object):
        distance = self.position.distance_to(other_object.position)
        return distance < self.radius + other_object.radius

    def text_fade(self, player, min_fade_distance=250, max_fade_distance=500):
        GRAY = 40
        obj_distance = self.position.distance_to(player.position)
        ratio = (max_fade_distance - min_fade_distance) / 215  # (255 - GRAY)
        color_value = -1 * (obj_distance - max_fade_distance) * ratio + GRAY
        if obj_distance < min_fade_distance or color_value >= 255: color_value = 255
        if obj_distance >= max_fade_distance or color_value < GRAY: color_value = GRAY
        return color_value

    def rotate(self,clockwise=True):
        MANEUVERABLILITY = 3
        sign = 1 if clockwise else -1
        angle = MANEUVERABLILITY * sign
        self.direction.rotate_ip(angle)


class ScreenPrint():
    def __init__(self, text, pos, label_font='Bahnschrift', font_size=22, font_color=(255, 255, 255)):
        self.text = text
        self.position = pos
        self.font = font.SysFont(label_font, font_size)
        self.font_color = font_color

    def draw(self, surface):
        drawing_surface = self.font.render(self.text, False, self.font_color)
        surface.blit(drawing_surface, self.position)


class Blurb():
    def __init__(self, pos, text_list, font_style='Bahnschrift', font_size=22, font_color=(255, 255, 255)):
        self.text_list = text_list
        self.position = pos
        self.font = font.SysFont(font_style, font_size)
        self.font_size = font_size
        self.font_color = font_color

    def draw(self, surface):
        for l in range(len(self.text_list)):
            blit_surface = self.font.render(self.text_list[l], False, self.font_color)
            blit_position = (self.position[0], self.position[1] + l * self.font_size)
            surface.blit(blit_surface, blit_position)


# $class StatusBar(GameObject):
class StatusBar(ScreenPrint):
    def __init__(self, name, x, y, width, height, maximum):
        self.name = name
        self.color = ['red', 'green', 'blue']
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.max = maximum
        self.SBtext = font.SysFont('Bahnschrift', 22)
        super().__init__(self.name, (x, y))

    def draw(self, pygame, surface, value, second_value=False, round_val=True, show_max=True,
             font_color=(255, 255, 255)):
        pygame.draw.rect(surface, self.color[0], (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, self.color[1], (self.x, self.y, self.w * (value / self.max), self.h))
        if second_value != False: pygame.draw.rect(surface, self.color[2], (
        self.x + self.w * (value / self.max), self.y, self.w * (second_value / self.max), self.h))
        if round_val == True: value = round(value)
        label_text = self.name + ': ' + str(value)
        if show_max == True: label_text = label_text + '/' + str(self.max)
        label_blit = self.SBtext.render(label_text, False, font_color)
        label_pos = (self.x + self.w + 5, self.y + (self.h / 4))
        surface.blit(label_blit, label_pos)

def create_feducials(num,surface):
    feducials = []
    for i in range(num): feducials.append(Feducial(get_random_position(surface)))
    return feducials

class Feducial(GameObject):
    def __init__(self,position):
        layer1 = [0.125,-0.005]
        layer2 = [0.0625,-0.0025]
        self.layer = random.choice([layer1,layer2])
        super().__init__(position, load_sprite('feducial'), 0)

    def move(self,surface):
        self.position = wrap_position((self.position + self.velocity),surface)

class Vessel(GameObject):
    MANEUVERABLILITY = 3    # This was an artifact of aster but. . . Where would this best be fit for moving everything else? see: thrust
    def __init__(self, position):
        self.direction = Vector2(UP)
        self.fuel = [100,100]
        self.thrust = -0.25
        self.srv = srv(_random=True)
        #constructMallard(self.srv)
        #constructVessel(self.srv)
        self.fuel = self.srv.fuel
        self.hydrogen = [0,0]
        super().__init__(position,rotozoom(load_sprite('spaceship'),0,(self.srv.hull.tons / 1000)), Vector2(0))

    def rotate(self,clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABLILITY * sign
        self.direction.rotate_ip(angle)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

class Waypoint(GameObject):
    MANEUVERABLILITY = 3
    def __init__(self,position,vessel):
        self.direction = Vector2(UP)
        self.size_code = 1 #vessel.srv.hull.tons // 100
        self.second_position = Vector2((0,0))
        super().__init__(position,rotozoom(load_sprite('waypoint-arrow'),0,(0.75*self.size_code)), Vector2(0))

    def rotate(self,clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABLILITY * sign
        self.direction.rotate_ip(angle)

    def point_at(self,GameObject_or_Vector2,second_position=False):
        if isinstance(GameObject_or_Vector2, Vector2):
            point_pos = GameObject_or_Vector2
            self.second_position = Vector2(point_pos[0],point_pos[0]-30)
        else:
            point_pos = GameObject_or_Vector2.position
            x = GameObject_or_Vector2.position[0]
            y = GameObject_or_Vector2.position[1] - GameObject_or_Vector2.radius - 200
            self.second_position = Vector2(x,y)
        if second_position: self.direction = Vector2((self.second_position[0] - point_pos[0])*-1,(self.second_position[1] - point_pos[1])*-1)
        else: self.direction = Vector2((self.position[0] - point_pos[0])*-1,(self.position[1] - point_pos[1])*-1)

    def draw(self, surface,second_position=False):
        angle = self.direction.angle_to(UP)
        rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        if second_position: blit_position = self.second_position - rotated_surface_size * 0.5
        else: blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)

class BorderObject(GameObject):
    def __init__(self,position,rotation):
        self.direction = Vector2(UP)
        super().__init__(position,rotozoom(load_sprite('jump-border'),rotation,1), 0)

class JumpBorder():
    def __init__(self,origin,d_out=510,troubleshooting=False):
        # Hexagon Math
        # (x = (center_x + radius * cos(angle),
        # y=center_y + radius * sin(angle))
        # radius = d_out
        # center_x = origin[0]
        # center_y = origin[1]

        
        self.angles = [0,0,0,0,0,0]
        self.N = BorderObject((origin[0],origin[1]-d_out),0)

        NE_a = radians(330)
        NE_x = origin[0]+(d_out*cos(NE_a))
        NE_y = origin[1]+(d_out*sin(NE_a))
        print(NE_x,NE_y)
        self.NE = BorderObject((NE_x,NE_y),300)

        SE_a = radians(30)
        SE_x = origin[0]+(d_out*cos(SE_a))
        SE_y = origin[0]+(d_out*sin(SE_a))
        self.SE = BorderObject((SE_x,SE_y),240)
        
        self.S = BorderObject((origin[0],origin[1]+d_out),180)

        NW_a = radians(150)
        NW_x = origin[0]+(d_out*cos(NW_a))
        NW_y = origin[1]+(d_out*sin(NW_a))
        self.NW = BorderObject((NW_x,NW_y),120)

        SW_a = radians(210)
        SW_x = origin[0]+(d_out*cos(SW_a))
        SW_y = origin[0]+(d_out*sin(SW_a))
        self.SW = BorderObject((SW_x,SW_y),60)

        self.d_out = d_out
        self.origin = origin
        
        if troubleshooting: print(origin,self.N,self.N.sprite)
        
        self.all = [self.S,self.N,self.NE,self.SE,self.SW,self.NW]

    def move(self,troubleshooting=False):
        for border in self.all:
            border.move()
            if troubleshooting: print(border)

    def inertia(self,direction,troubleshooting=False):
        for border in self.all:
            border.velocity -= direction
            if troubleshooting: print(border.velocity)

    def realign(self,vessel):
        vx = vessel.position[0]
        self.N.position[0] = vx
        self.S.position[0] = vx
        ##-60 is -173.2051
        #intercept = self.NE.position[1] - (-173.2051*self.NE.position[0])
        #self.NE.position[0] = -173.2051*vessel.position[1]

    def draw(self,surface):
        for border in self.all:
            angle = border.direction.angle_to(UP)
            rotated_surface = rotozoom(border.sprite, angle, 1.0)
            rotated_surface_size = Vector2(rotated_surface.get_size())
            blit_position = border.position - rotated_surface_size * 0.5
            surface.blit(rotated_surface, blit_position)
