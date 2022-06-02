import gridmaker
import cv2 as cv


def find_bombs(grid):
    n = len(grid)
    ignore = ['O', 'U', 'X', 'P']
    mem = []
    flag = True

    while flag:
        for i in range(n):
            for j in range(n):
                pos = grid[i][j]
                unopened = []
                bombs = []

                if pos not in ignore:
                    # print(pos)
                    for l in range(i-1, i+2):
                        for m in range(j-1, j+2):
                            try:
                                assert l in range(n) and m in range(n), ' '
                                new_pos = grid[l][m]
                                
                                with open('Assets/log.txt', 'a') as f:
                                    f.writelines(f"{pos} {[i, j]} {(l, m)}\n")

                                if new_pos == 'X':
                                    bombs.append([l, m])
                                    unopened.append([l, m])

                                if new_pos == 'U':
                                    unopened.append([l, m])


                            except:
                                continue

                    try:
                        if len(unopened) == int(pos):
                            for u in unopened:
                                grid[u[0]][u[1]] = 'X'

                        if len(bombs) == int(pos):
                            pop = [i for i in unopened if i not in bombs]
                            
                            for p in pop:
                                grid[p[0]][p[1]] = 'P'

                    except:
                        continue

                else:
                    continue

        if mem == grid:
            flag = False
        
        mem = [row.copy() for row in grid]
    
    return grid

if __name__ == '__main__':
    img = cv.imread('Assets/stage-6.png')
    mines = gridmaker.convertToGrid(img, 9)
    g = find_bombs(mines)

    for i in g:
        for j in i:
            print(j, end='  ')
        print('')
