import pygame
import csv
# pygame.init()
# screen = pygame.display.set_mode((640,480))
class types:
    blank = 0
    water = 1
    null = -1

class tile:
    def __init__(self,starttype = types.blank):
        self.type = starttype
    def update(self,neighbours):
        print(neighbours)
        if self.type != types.null:
            pass
    def __str__(self):
        return str(self.type)
    
class world:
    def __init__(self,dimension = None, wfile = None):
        self.world = []
        if dimension is not None:
            self.world = [[tile(types.blank) for x in range(dimension+y%2)] for y in range(dimension)]
        elif wfile is not None:
            with open(wfile, 'r') as worldfile:
                for row in csv.reader(worldfile):
                    self.world.append([tile(typ) for typ in row])
        else:
            dimension = 10
            self.world = [[0 for x in range(dimension+y%2)] for y in range(dimension)]
        self.update()
    def update(self):
        for row in range(1,len(self.world)-1):
            for cell in range(1,len(self.world[row])-2):
                neigs = [self.world[row-1][cell],
                        self.world[row-1][cell+1],
                        self.world[row][cell-1],
                        self.world[row][cell+1],
                        self.world[row+1][cell],
                        self.world[row+1][cell+1]]
                self.world[row][cell].update(neighs)
def createdurmap():
    with open("mapfile.txt", "w") as f:
        m = [[0 if x-y%2>0 and x<17 and y<17 and y>0 else -1 for x in range(18+y%2)] for y in range(18)]
        writr = csv.writer(f)
        for row in m:
            writr.writerow(row)
    print(m)


durham = world(wfile = 'mapfile.txt')
# createdurmap()
# while True:
#     screen.fill((0,0,0))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             pygame.quit()
#             break
    
#     pygame.display.update()