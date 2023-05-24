from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
import pickle
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land=Mapmanager()
        self.land.loadLand("land.txt")
        self.hero=Hero((7,2,4),self.land)
        base.camLens.setFov(100)
game=Game()
game.run()
