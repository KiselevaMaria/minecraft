# напиши здесь код создания и управления картой
import pickle

class Mapmanager():
    def __init__(self):
        self.model = 'block.egg'
        self.texture = 'block.png'
        self.color = [(0.0, 0.0, 0.5, 1),(0.2, 0.2, 0.3, 1),(0.5, 0.5, 0.2, 1),(0.0, 0.6, 0.0, 1)]
        self.startNew()
        self.addBlock((0, 10, 0))


    def startNew(self):
        self.land = render.attachNewNode('Land')

    def addBlock(self, pos):
        self.colors = self.getColor(int(pos[2]))
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(pos)
        self.block.setColor(self.colors)
        self.block.reparentTo(self.land)
        self.block.setTag('at', str(pos))
    
    def getColor(self, z):
        if z < len(self.color):
            return self.color[z]
        else:
            return self.color[len(self.color)-1]

    def clear(self):
        self.land.removeNode()
        self.startNew()
    
    def loadland(self, filename):
        self.clear()
        with open(filename) as File:
            y = 0
            for line in File:
                x = 0
                line = line.split(' ')

                for z in line:

                    for i in range(int(z)+1):
                        block = self.addBlock((x,y,i))
                        x += 1
                y += 1
    
    def is_Empty(self, pos):
        blocs = self.findBlocks(pos)
        if blocs:
            return False
        else:
            return True

    def findBlocks(self, pos):
        return self.land.findAllMatches('=at=' + str(pos))

    def findHighestEmpty(self, pos):
        x,y,z = pos
        z = 1
        while not self.is_Empty((x,y,z)):
            z += 1
        return (x,y,z)

    def buildBlock(self, pos):
        x,y,z = pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z + 1:
             self.addBlock(new)

    def delBlock(self, position):
        blocks = self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, position):
        x, y, z = self.findHighestEmpty
        pos = x, y, z - 1
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def saveMap(self):
        blocks = self.land.getChildren()
        with open('my_map.dat', 'wb') as f:
            pickle.dump(len(blocks), f)
            for i in blocks:
                x, y, z = i.getPos()
                pos = (int(x), int(y), int(z))
                pickle.dump(pos, f)

    def loadMap(self):
        self.clear()
        with open('my_map.dat', 'rb') as f:
            lenght = pickle.load(f)
            for i in range(lenght):
                pos = pickle.load(f)
                self.addBlock(pos)


    