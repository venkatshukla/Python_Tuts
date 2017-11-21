class girl:
    gender = "female"
    def __init__(self, name):
        self.name = name
        print(self.gender,self.name)
    def talk:
        print("I talk")
#tuna = girl("tuna")

#inheritance
class women(girl):
    def __init__(self,name):
        print(name, self.gender)

    def gossip:
        print("I gossip")

tuna = women("Tuna")

class OldWomen(girl, women):
    pass
    #if you want a class that has nothing to do...EMPTY

runa = OldWomen()
runa.gossip()
runa.talk()


