class Snake():
    def __init__(self):
        self.x = 7
        self.y = 7
        self.size = 1
        self.pos = [(self.x,self.y)]
        self.direction = ''
        self.score = 0
    def move(self):
        if self.direction == 'u':
            self.y-=1
        elif self.direction == 'd':
            self.y+=1
        elif self.direction == 'r':
            self.x+=1
        elif self.direction == 'l':
            self.x-=1
        self.pos.insert(0,(self.x,self.y))
        self.pos.pop()