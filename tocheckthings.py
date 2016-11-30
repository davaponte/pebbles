#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  tocheckthings.py
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
import pygame


def main(args):

    pygame.init()
    pygame.display.set_mode()
    while True:
        for event in pygame.event.get():
            print(event.type)
            if event.type == pygame.QUIT:
                pygame.quit(); #sys.exit() if sys is imported
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print("Hey, you pressed the key, '0'!")
                if event.key == pygame.K_1:
                    print("Doing whatever")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
