# напиши свой код здесь

class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 1, 1, 1)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.CameraBind()
        self.accept_events()

    def accept_events(self):
        base.accept('c', self.changeView)

        base.accept('q', self.turn_left)
        base.accept('q' + '-repeat', self.turn_left )
        base.accept('e', self.turn_right)
        base.accept('e' + '-repeat', self.turn_right )

        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)
        
        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back )

        base.accept('a', self.left)
        base.accept('a' + '-repeat', self.left )

        base.accept('d', self.right)
        base.accept('d' + '-repeat', self.right )

        base.accept('r', self.up)
        base.accept('r' + '-repeat', self.up )

        base.accept('f', self.down)
        base.accept('f' + '-repeat', self.down )

        base.accept('2', self.build)

        base.accept('3', self.destroy)

        base.accept('z', self.change_mode)

        base.accept('n', self.land.saveMap)
        base.accept('m', self.land.loadMap)

    
    def turn_left(self):
        a = self.hero.getH()
        a += 5
        self.hero.setH(a%360)

    def turn_right(self):
        b = self.hero.getH()
        b -= 5
        self.hero.setH(b%360)

    def changeView(self):
        if self.camera_on == True:
            self.CameraUP()
        else:
            self.CameraBind()
    
    def CameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.camera_on = True

    def CameraUP(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] -3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.camera_on = False
#_______________________________________________________________________________________________________

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.land.buildBlock(pos)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.land.delBlockFrom(pos)

#_______________________________________________________________________________________________________
    

    def look_at(self, angle):
        from_x = round(self.hero.getX())
        from_y = round(self.hero.getY())
        from_z = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)

        return from_x + dx, from_y + dy, from_z

    def check_dir(self, angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)

        elif angle <= 65:
            return (1, -1)
        
        elif angle <= 110:
            return (1, 0)

        elif angle <= 155:
            return (1, 1)

        elif angle <= 200:
            return (1, 0)

        elif angle <= 245:
            return (1, 1)

        elif angle <= 290:
            return (-1, 0)

        elif angle <= 335:
            return (1, -1)

        elif angle <= 360:
            return (0, -1)

#Обработчик событий______________________________________________________________________________

    def forward(self):
        angle = (self.hero.getH())%360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH()+180)%360
        self.move_to(angle)
    
    def left(self):
        angle = (self.hero.getH()+90)%360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH()+270)%360
        self.move_to(angle)

    def up(self):
        self.hero.setZ(self.hero.getZ()+1)

    def down(self):
        self.hero.setZ(self.hero.getZ()-1)
#__________________________________________________________________________________________________
    def just_move(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def try_move(self, angle):
        pos = self.look_at(angle)
        if self.land.is_Empty(pos):
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            pos = pos[0]. pos[1], pos[2] + 1
            if self.land.is_Empty(pos):
                self.hero.setPos(pos)

    def move_to(self, angle):
        if self.mode == True:
            self.just_move(angle)
        else:
            self.try_move(angle)

    def change_mode(self):
        if self.mode == True:
            self.mode = False
        else:
            self.mode = True

    