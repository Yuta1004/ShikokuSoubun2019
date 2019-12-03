# Copylight(c) 2019 NakagamiYuta
# LICENCE : MIT

class Agent:
    def __init__(self, team, _id, x, y):
        self.team = team
        self.id = _id
        self.x = x
        self.y = y
        self.remove_panel = False
        self.dx = -10
        self.dy = -10


    def __str__(self):
        return  "TeamID : " + str(self.team) + "\n" +\
                "AgentID : " + str(self.id) + "\n" +\
                "Position : (" + str(self.x) + "," + str(self.y) + ")"


    def move(self):
        if not self.remove_panel:
            self.x += self.dx
            self.y += self.dy


    def reset(self):
        self.remove_panel = False
        self.dx = 0
        self.dy = 0
