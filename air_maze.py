# https://www.youtube.com/watch?v=ifRZJCZYcwo

world.time = 'day'
world.weather = 'clear'

from minecraft.location import Location

ppos = Location(-0, 1, 0)

def from_pos(x, y, z):
  global ppos
  return ppos + Location(x, y, z)

n = 5
size = 3

a = [[0]*(n+2) for i in range(n+2)]
for i in range(n+2):
  a[0][i] = 1
  a[i][0] = 1
  a[n+1][i] = 1
  a[i][n+1] = 1
  
def get(pos):
  return a[pos[0]][pos[1]]
  
def set(pos, val):
  a[pos[0]][pos[1]] = val
  
def add(p1, p2):
  return (p1[0]+p2[0], p1[1]+p2[1])

step = []

import random
def maze(pos):
  set(pos, 1)
  ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
  random.shuffle(ds)
  for d in ds:
    if get(add(pos, d)) == 0:
      step.append((pos, d))
      maze(add(pos, d))
maze((1,1))

WATER = 'air'

def buildcell(r, c):
  size = 3
  # base
  world.fill(from_pos(r*size  , c*size , -1),    from_pos(r*size+size  , c*size + size, -1), 'quartz block')
  world.fill(from_pos(r*size  , c*size ,  0),    from_pos(r*size+size  , c*size + size,  0), 'stone brick')
  world.fill(from_pos(r*size+1, c*size+1, 0),    from_pos(r*size+size-1, c*size + size-1,0), WATER)
  world.fill(from_pos(r*size  , c*size ,  1),    from_pos(r*size+size  , c*size + size,  1), 'glass')
  if r == 5 and c == 5:
    for _ in range(10):
        summon('parrot', from_pos(r*size+1, c*size+1, 0))
  
def breakcell(r, c, dr, dc):
  size = 3
  if dr == 1:
    world.set(from_pos(r*size+size, c*size+1, 0), WATER)
    world.set(from_pos(r*size+size, c*size+2, 0), WATER)
  if dr == -1:
    world.set(from_pos(r*size, c*size+1, 0), WATER)
    world.set(from_pos(r*size, c*size+2, 0), WATER)
  if dc == 1:
    world.set(from_pos(r*size+1, c*size+size, 0), WATER)
    world.set(from_pos(r*size+2, c*size+size, 0), WATER)
  if dc == -1:
    world.set(from_pos(r*size+1, c*size, 0), WATER)
    world.set(from_pos(r*size+2, c*size, 0), WATER)
  

for i in range(1, n+1):
  for j in range(1, n+1):
    buildcell(i, j)

for s in step:
  breakcell(s[0][0], s[0][1], s[1][0], s[1][1])

world.set(from_pos(4,4,1), 'air')
world.set(from_pos(4,5,1), 'air')
world.set(from_pos(5,4,1), 'air')
world.set(from_pos(5,5,1), 'air')
'''
agent.teleport('100 0 0')
world.fill(from_pos(0, 0,  -1), from_pos(18,18,1), 'air')
'''
