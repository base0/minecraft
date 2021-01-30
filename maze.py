n = 10
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

WATER = 'flowing water'
#WATER = 'water'
def buildcell(r, c):
  size = 3
  world.fill(from_me(r*size, -1, c*size),    from_me(r*size + size, 0, c*size + size), 'stone brick')
  world.fill(from_me(r*size+1, 0, c*size+1), from_me(r*size + size - 1, 0, c*size + size-1), WATER)
def breakcell(r, c, dr, dc):
  size = 3
  if dr == 1:
    world.set(from_me(r*size+size, 0, c*size+1), WATER)
    world.set(from_me(r*size+size, 0, c*size+2), WATER)
  if dr == -1:
    world.set(from_me(r*size, 0, c*size+1), WATER)
    world.set(from_me(r*size, 0, c*size+2), WATER)
  if dc == 1:
    world.set(from_me(r*size+1, 0, c*size+size), WATER)
    world.set(from_me(r*size+2, 0, c*size+size), WATER)
  if dc == -1:
    world.set(from_me(r*size+1, 0, c*size), WATER)
    world.set(from_me(r*size+2, 0, c*size), WATER)
  

for i in range(1, n+1):
  for j in range(1, n+1):
    buildcell(i, j)

for s in step:
  breakcell(s[0][0], s[0][1], s[1][0], s[1][1])

for i in range((n*n) / 2):
    summon('tropical fish', '~4 ~0 ~4')

say('complete')
