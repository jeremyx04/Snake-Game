import random
class Food():
    def __init__(self,playerx,playery):
        self.x = playerx
        while (self.x==playerx):
            self.x = random.randint(0,15)
        self.y = playery
        while (self.y==playery):
            self.y = random.randint(0,15)
        self.eaten = 0
        