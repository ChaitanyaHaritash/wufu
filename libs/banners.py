#!/usr/bin/env python
"""
this method of wufu will print random banners in main class Wufu_Main
"""
from pyfiglet import *
from random import randint
class BannerLoad():
    
    def bannerloder(self):
        for i in range(1):
            RanBan = randint(1,7)
        if RanBan == 1:
            f = Figlet(font='slant')
            print f.renderText("WuFu")
        elif RanBan == 2:
            f = Figlet(font='ogre')
            print f.renderText("WuFu")
        elif RanBan == 3:
            f = Figlet(font='graceful')
            print f.renderText("WuFu")
        elif RanBan == 4:
            f = Figlet(font='doom')
            print f.renderText("WuFu")
        elif RanBan == 5:
            f = Figlet(font='graffiti')
            print f.renderText("WuFu")
        elif RanBan == 6:
            f = Figlet(font='big')
            print f.renderText("WuFu")
        elif RanBan == 7:
            f = Figlet(font='modular')
            print f.renderText("WuFu")