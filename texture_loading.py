from direct.showbase.ShowBase import ShowBase
from panda3d.core import TextureStage,CardMaker
from direct.actor import Actor
import os

class Wrapper:
    def __init__(self):
        self.my_models = []
        self.b = ShowBase()
        c = 0
        while c < 3:
            self.load_gltf(c)
            c += 1
        
    def load_gltf(self,c):
        showbase = self.b
        pos=(-3 + c *3, 20, -2)
        scale=(1,1,1)
        try:
            #ob = self.b.loader.loadModel("Cube.glb")
            ob = Actor.Actor("Cube.glb")
            self.my_models.append(ob)
        except OSError as e:
            print("my error",e)
            #wait that probably should be in the create load function
            #can't find the file
            return None
            
        ob.setPos(*pos)
        ob.reparentTo(showbase.render)
        ob.setScale(*scale)
        ob.setTwoSided(True)
        ob.clearTexture()
        
        tex = self.b.loader.loadTexture("ground.jpg")
        cm = CardMaker('card')
        card = self.b.render.attachNewNode(cm.generate())
        pos=(-3 + c *3, 22,0)
        card.setPos(pos)
        card.setTexture(tex)
        
        if c==0:
            return
        
        ts2 = TextureStage('ts2')
        
        if False:
            if c == 1:
                ts2.setMode(TextureStage.MDecal)
            if c == 2:
                ts2.setMode(TextureStage.MBlend)
            if c == 3:
                ts2.setMode(TextureStage.MAdd)
            if c == 4:
                ts2.setMode(TextureStage.MBlend)
            #ts2.setTexcoordName("")
        
        ob.setTexture(ts2,tex)
        
        

def recursive_clear(ob,stage):
    if "children" in dir(ob):
        if len(ob.children)!=0:
            for x in ob.children:
                recursive_clear(x,stage)
    ob.clearTexture()
    try:
        ob.removeTextureStage(stage)
    except:
        a=1
        
def main():
    W = Wrapper()
    while True:
        W.b.taskMgr.step()

if __name__ == "__main__":
    main()
