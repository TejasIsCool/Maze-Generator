from ntpath import join
import random,time
from PIL import Image,ImageDraw
import gc
time1 = time.time()
#class Cell():
    #def __init__(self,x,y):
        #self.x=x
        #self.y=y

        #self.left = True
        #self.right = True
        #self.top = True
        #self.bottom = True
        #self.visited = False



#cell[0] = x
#cell[1] = y
#cell[2] = left
#cell[3] = right
#cell[4] = top
# cell[5] = bottom
# cell[6] = visited



def get_neighbors(x,y,arr):
    x,y = x,y
    ret = []
    try:
        if not(x-1 < 0):
            if not arr[x-1][y][6]:
                ret.append(arr[x-1][y])
    except:
        pass
    try:
        if not arr[x+1][y][6]:
            ret.append(arr[x+1][y])
    except:
        pass
    try:
        if not y-1 < 0:
            if not arr[x][y-1][6]:
                ret.append(arr[x][y-1])
    except:
        pass
    try:
        if not arr[x][y+1][6]:
            ret.append(arr[x][y+1])
    except:
        pass
    return ret

def removewall(cell,nigh):
    if nigh[1] > cell[1]:
        #wall is the bottom one
        cell[5] = False
        nigh[4] = False
    if nigh[1] < cell[1]:
        #wall is top one
        cell[4] = False
        nigh[5] = False
    if nigh[0] < cell[0]:
        #wall is left one
        cell[2] = False
        nigh[3] = False
    if nigh[0] > cell[0]:
        cell[3] = False
        nigh[2] = False


row_cols = input("Enter size (Recommended: (20,20)): ")
rows,cols = row_cols.split(",")

colls = int(cols)
rowss = int(rows)


colls,rowss = rowss,colls

#creates a 2d array with all elements as 0
cells = [[0 for x in range(colls)] for y in range(rowss)]
stack = []

for i in range(0, rowss):
    for j in range(0, colls):
        #x,y,left,right,top,bottom,visited
        cells[i][j] = [i,j,True,True,True,True,False]

current_cell = cells[0][0]
current_cell[6]= True
stack.append(current_cell)
while len(stack) > 0:
    current_cell = stack.pop()
    neighbors = get_neighbors(current_cell[0],current_cell[1],cells)
    if len(neighbors) > 0:
        stack.append(current_cell)
        choice = random.choice(neighbors)
        removewall(current_cell,choice)
        choice[6] = True
        stack.append(choice)

print(len(stack))
print(time.time() - time1)
del stack
#Now drawing part
print("Now drawing")
time1 = time.time()
#print(cells)
size = rowss*10+2,colls*10+2
im = Image.new(mode="1",size=size)
draw = ImageDraw.Draw(im)

uporleft = random.choice(["UP","LEFT"])
downorright = random.choice(["DOWN","RIGHT"])

po = 10
for i in range(0, rowss):
    for j in range(0, colls):
        cell = cells[i][j]
        x = i*po
        y = j*po
        xo = (i+1)*po
        yo = (j+1)*po
        if cell[4]:
            if not(i == 0 and j == 0 and uporleft == "UP"):
                draw.line((x,y,xo,y),fill=1)
        if cell[5]:
            if not(i == rowss-1 and j == colls-1 and downorright == "DOWN"):
                draw.line((x,yo,xo,yo),fill=1)
        if cell[2]:
            if not(i == 0 and j == 0 and uporleft == "LEFT"):
                draw.line((x,y,x,yo),fill=1)
        if cell[3]:
            if not(i == rowss-1 and j == colls-1 and downorright == "RIGHT"):
                draw.line((xo,y,xo,yo),fill=1)

print("Drawing time:",time.time() - time1)
print("Garbage collect")
del cells
gc.collect()
im.save("Maze.png","PNG")
print("done")
del im
gc.collect()
print("out")