# https://youtu.be/RbaaTgJAnOI

def house(n):
    if n == 2:
        return
    else:
        blocks.fill(STONE_BRICKS, pos(-n,0,-n), pos(n,n,n), FillOperation.HOLLOW)
        blocks.fill(GLOWSTONE, pos(-n,n,-n), pos(n,n,n))
        house(n-2)

house(10)
