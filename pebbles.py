#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#  pebbles.py
#
#  Copyright 2016 data <data@Nessus>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import sys, pygame, random
from pygame.locals import *

size = width, height = 1024, 768
speed = [2, 2]
MaxLoops = 30

Black = (0, 0, 0)
Blue = (0, 0, 255)
Green = (0, 255, 0)
Cyan = (0, 255, 255)
Red = (255, 0, 0)
Magenta = (255, 0, 255)
Brown = (165, 43, 42)
LightGray = (223, 223, 223)
DarkGray = (169, 169, 169)
LightBlue = (173, 217, 230)
LightGreen = (144, 237, 146)
LightCyan = (224, 255, 255)
LightRed = (254, 128, 129)
LightMagenta = (255, 127, 255)
Yellow = (255, 255, 0)
White = (255, 255, 255)

Colors = {
  0: Black, 1: Blue, 2: Green, 3: Cyan, 4: Red, 5: Magenta, 6: Brown,
  7: LightGray,
  8: DarkGray,
  9: LightBlue,
  10: LightGreen,
  11: LightCyan,
  12: LightRed,
  13: LightMagenta,
  14: Yellow,
  15: White}

def load_image(filename, transparent = False):
        try: image = pygame.image.load(filename)
        except pygame.error, message:
                raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image


class Figura(pygame.sprite.Sprite):

    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image(filename, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.centery = height / 2
        self.speed = [0.5, -0.5]

    def actualizar(self, time):
        self.rect.centerx += self.speed[0] * time
        self.rect.centery += self.speed[1] * time
        if self.rect.left <= 0 or self.rect.right >= width:
            self.speed[0] = -self.speed[0]
            self.rect.centerx += self.speed[0] * time
        if self.rect.top <= 0 or self.rect.bottom >= height:
            self.speed[1] = -self.speed[1]
            self.rect.centery += self.speed[1] * time

def TextOut(texto, posx, posy, size, color=(255, 255, 255)):
    fuente = pygame.font.Font("fonts/DroidSans.ttf", size)
    salida = pygame.font.Font.render(fuente, texto, 1, color)
    salida_rect = salida.get_rect()
    salida_rect.centerx = posx
    salida_rect.centery = posy
    return salida, salida_rect

def main(args):


    pygame.init()

    infoObject = pygame.display.Info()
    size = width, height = infoObject.current_w, infoObject.current_h

    screen = pygame.display.set_mode(size)
    ##screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    pygame.display.set_caption("Pebbles 1.0")

    Background_image = load_image("images/background_white.png")
    Imagen = Figura("images/pebbles.png")

    clock = pygame.time.Clock()

    def Case(x):
        return {
            K_0 : ('0', None),
            K_1 : ('1', None),
            K_2 : ('2', None),
            K_3 : ('3', None),
            K_4 : ('4', None),
            K_5 : ('5', None),
            K_6 : ('6', None),
            K_7 : ('7', None),
            K_8 : ('8', None),
            K_9 : ('9', None),

            K_KP0 : ('0', None),
            K_KP1 : ('1', None),
            K_KP2 : ('2', None),
            K_KP3 : ('3', None),
            K_KP4 : ('4', None),
            K_KP5 : ('5', None),
            K_KP6 : ('6', None),
            K_KP7 : ('7', None),
            K_KP8 : ('8', None),
            K_KP9 : ('9', None),

            K_a : ('A', None),
            K_e : ('E', None),
            K_i : ('I', None),
            K_o : ('O', None),
            K_u : ('U', None),

            K_b : ('B', None),
            K_c : ('C', None),
            K_d : ('D', None),

            K_b : ('B', None),
            K_c : ('C', None),
            K_d : ('D', None),
            K_e : ('E', None),
            K_f : ('F', None),
            K_g : ('G', None),
            K_h : ('H', None),
            K_i : ('I', None),
            K_j : ('J', None),
            K_k : ('K', None),
            K_l : ('L', None),
            K_m : ('M', None),
            K_n : ('N', None),
            K_o : ('O', None),
            K_p : ('P', None),
            K_q : ('Q', None),
            K_r : ('R', None),
            K_s : ('S', None),
            K_t : ('T', None),
            K_u : ('U', None),
            K_v : ('V', None),
            K_w : ('W', None),
            K_x : ('X', None),
            K_y : ('Y', None),
            K_z : ('Z', None),
            K_q : ('Q', None),
            K_t : ('T', None),
        }.get(x, ('@', None))


    Pressed = (None, None)

    LoopCounter = MaxLoops

#####    pygame.event.set_grab(True)

    BufQuit = ''

    while True:
        time = clock.tick(8)

        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit(0)

            if event.type == pygame.KEYDOWN:
                Pressed = Case(event.key)
                print(BufQuit)
                if Pressed[0] in ('Q', 'U', 'I', 'T'):
                    BufQuit = BufQuit + Pressed[0]
                    if (len(BufQuit) == 4) & (BufQuit == 'QUIT'):
                        #print(len(BufQuit), BufQuit)
                        sys.exit(0)
                    if (len(BufQuit) >= 4):
                        BufQuit = ''
                else:
                    BufQuit = ''

        Imagen.actualizar(time)
        LoopCounter = LoopCounter + 1
        #print(LoopCounter)
        if (LoopCounter >= MaxLoops):
            screen.blit(Background_image, (0, 0))
            LoopCounter = 0

        if Pressed[0] != None:
            newx, newy = random.randrange(width), random.randrange(height)
            text, text_rect = TextOut(Pressed[0],
              newx, newy,
              160, Colors[random.randrange(15) + 1]
              )
            frame, frame_rect = TextOut(Pressed[0],
              newx + 3, newy + 3,
              160, (0, 0, 0))
            screen.blit(frame, frame_rect)
            screen.blit(text, text_rect)
            Pressed = (None, None)

        screen.blit(Imagen.image, Imagen.rect)

        pygame.display.flip()

#####    pygame.event.set_grab(False)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
