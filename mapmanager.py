import pickle
class Mapmanager():
    def __init__(self):
        self.model="block.egg"
        self.texture='block.png'
        self.colors=[(0.5,0.3,0.2,1), (0.1,0.6,0.2, 1), (0.2,0.1,0.6, 1), (0.1,0.5,0.7, 1)]
        self.startNew()
        self.addBlock((0,10,0))

    def startNew(self):
        self.land=render.attachNewNode("Land")    
        
    def addBlock(self,position):
        self.block=loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color=self.getColor(int(position[2]))
        self.block.setColor(self.color)
        self.block.reparentTo(self.land)
        self.block.setTag("at", str(position))
        

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors)-1]
    
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y=0
            for line in file:
                x=0
                line=line.split(' ')
                for z in line:
                    for i in range(int(z)+1):
                        block=self.addBlock((x, y, i))
                    x+=1
                y+=1
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at="+ str(pos))


    def is_Empty(self, pos):
        blocks=self.findBlocks(pos)
        if blocks:
            return False
        else:
            return True

    def findHighetsEmpty(self, pos):
        x,y,z=pos
        z=1
        while not self.is_Empty((x,y,z)):
            z+=1
        return (x,y,z)
    def delBlock(self, position):
        blocks=self.findBlocks(position)
        for block in blocks:
            block.removeNode()

    def buildBlock(self, pos):
        x,y,z=pos
        new=self.findHighetsEmpty(pos)
        if new[2]<=z+1:
            self.addBlock(new)

    def delBlockFrom(self, position):
        x,y,z=self.findHighetsEmpty(position)
        pos=x,y,z-1
        blocks=self.findBlocks(pos)
        for block in blocks:
            block.removeNode()

    def saveMap(self):
        blocks=self.land.getChildren()
        with open ('my_map.dat', 'wb') as f:
            pickle.dump(len(blocks), f)
            for i in blocks:
                x,y,z=i.getPos()
                pos=(int(x), int(y), int(z))
                pickle.dump(pos, f)

    def loadMap(self):
        self.clear()
        with open('my_map.dat', 'rb') as f:
            length=pickle.load(f)
            for i in range(length):
                pos=pickle.load(f)
                self.addBlock(pos)
