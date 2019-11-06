import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
class types(Enum):
    blank = 0
    water = 1

class tile:
    def __init__(self,type = types.blank):
        pass
class world:
    def __init__(self,dims):
        self.world=[]
# with open("mapfile.txt", "r") as f:
#     map = [[int(x) for x in i.split(",")] for i in f.read().split("\n")]
# print(map)
# while True:
#     screen.fill((0,0,0))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             break
    
#     pygame.display.update()