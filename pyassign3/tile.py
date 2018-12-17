"""tile.py:
Module for filling tiles
This module provides all solutions to 
fill the assigned tiles using given bricks 
__author__ = 'Friedrich Foo'
__pkuid__ = '1800011746'
__email__ = '1800011746@pku.edu.cn'
"""

# Part initial: Input
import math
ans = []
final = []
mstr = input('The lenth of the tile: ')
nstr = input('The width of the tile: ')
astr = input('One lenth of the brick: ')
bstr = input('Another lenth of the brick: ')

# Part A: Using Recursion to Give Solutions
def judge(x0, y0, x1, y1):
    """Function for judging whether bricks from one 
    brick with coordinate(x0,y0) to another with 
    coordinate(x1,y1) are filled.
    Return True if not filled.
    """
    if x0 < 0 or y0 < 0:
        return False
    if x1 >= m or y1 >= n:
        return False
    for i in range(x0, x1 + 1):
        for j in range(y0, y1 + 1):
            if vis[i][j]:
                return False
    return True

def search(step):
    """Main function to find all solutions:
    step means the really depth for recursion 
    equaling (m * n) // (a * b)
    """
    if step == 0:
        """Recursion basement
        Return the final answer found
        """
        final.append(ans[:])
        return
    for i in range(m):
        """To find a nearest brick which 
        is not filled
        """
        if False in vis[i]:
            x, y = i, vis[i].index(False)
            break

    # a x b filling
    if judge(x, y, x + a - 1, y + b - 1):
        """First way to fill
        Recursion part1
        """
        x0, y0, x1, y1 = x, y, x + a - 1, y + b - 1
        now = []
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                vis[i][j] = True
                now.append(idx[i][j])
        now.sort()
        ans.append(now)
        search(step - 1)
        ans.pop()
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                vis[i][j] = False
    # b x a filling
    if judge(x, y, x + b - 1, y + a - 1) and a!=b:
        """Second way to fill
        while a == b, skip this process
        Recursion part2
        """
        x0, y0, x1, y1 = x, y, x + b - 1, y + a - 1
        now = []
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                vis[i][j] = True
                now.append(idx[i][j])
        now.sort()
        ans.append(now)
        search(step - 1)
        ans.pop()
        for i in range(x0, x1 + 1):
            for j in range(y0, y1 + 1):
                vis[i][j] = False
                
# Part B: Visualization Using Turtle
import turtle as tt

def draw_line1(x0, y0, x1, y1):
    """Function to draw frame of the tile
    from coordinate(x0, y0) to (x1, y1)
    """
    tt.speed(0)
    tt.pensize(5)
    tt.pencolor('black')
    tt.penup()
    tt.goto(x0, y0)
    tt.pendown()
    tt.begin_fill()
    tt.goto(x1, y1)
    tt.end_fill()
    tt.penup()

def draw_line2(x0, y0, x1, y1):
    """Function to draw frame of filling bricks
    from coordinate(x0, y0) to (x1, y1)
    """
    tt.speed(0)
    tt.pensize(1)
    tt.pencolor('blue')
    tt.penup()
    tt.goto(x0, y0)
    tt.pendown()
    tt.begin_fill()
    tt.goto(x1, y1)
    tt.end_fill()
    tt.penup()

def draw_num(number, x, y):
    """Function to write down a corresponding number 
    in the matrix
    Adjust the size of number 
    to make it easy to be seen
    """
    tt.speed(0)
    tt.penup()
    tt.pencolor('black')
    tt.goto(x, y)
    tt.pendown()
    tt.write(str(number),align="center",\
             font=("Arial", size, "normal"))
    tt.penup()

def get_ij(block_id):
    """Function to build connection 
    between block_id to 
    corresponding number
    """
    for i in range(m):
        for j in range(n):
            if idx[i][j] == block_id:
                return i, j

def get_xy(block_id, width=50):
    """Function to get the (x, y) 
    to draw frame of bricks
    """
    tt.speed(0)
    i, j = get_ij(block_id)
    x = (i + 1) * width
    y = (j - 1) * width
    return [x, x + width], [y, y + width]

def draw(answer, width=50):
    """Main function to draw one answer from final
    Adjust the screen to make it easy to be seen
    tt as turtle
    bg as the screen
    """
    tt.speed(0)
    bg = tt.Screen()
    total_x = m * width
    total_y = n * width
    hx = total_x / 2
    hy = total_y / 2
    sizelenth = max(hx+width,hy+width)
    bg.setworldcoordinates(-sizelenth,-sizelenth,\
                           sizelenth,sizelenth)
    for i in range(m + 1):
        x0, x1 = i * width, i * width
        y0, y1 = 0, total_y
        draw_line2(x0 - hx, y0 - hy, x1 - hx, y1 - hy)
    for j in range(n + 1):
        y0, y1 = j * width, j * width
        x0, x1 = 0, total_x
        draw_line2(x0 - hx, y0 - hy, x1 - hx, y1 - hy)
    for i in range(m):
        for j in range(n):
            x = i * width + 0.5 * width
            y = j * width + 0.5 * width
            draw_num(idx[i][j], x - hx, y - hy)
    for block in answer:
        x = []
        y = []
        for block_id in block:
            tx, ty = get_xy(block_id)
            x += tx
            y += ty
        x0 = min(x) - width
        x1 = max(x) - width
        y0 = min(y) + width
        y1 = max(y) + width
        draw_line1(x0 - hx, y0 - hy, x0 - hx, y1 - hy)
        draw_line1(x0 - hx, y0 - hy, x1 - hx, y0 - hy)
        draw_line1(x1 - hx, y1 - hy, x0 - hx, y1 - hy)
        draw_line1(x1 - hx, y1 - hy, x1 - hx, y0 - hy)
    tt.done()

# Part C: Main Process to Finish the Assign
def main():
    """Main function
    Test whether the input is valid
    Error if not
    Then to recursion part to find solution
    After which to visualize one solution
    """
    global m, n, a, b, size, vis, idx
    try:
        m = int(mstr)
        n = int(nstr)
        a = int(astr)
        b = int(bstr)
    except Exception as e:
        print('Invalid Input')
        print('Reason:',e)
    else:
        m = int(mstr)
        n = int(nstr)
        a = int(astr)
        b = int(bstr)
        size = 12 - int(math.log1p(m*n+1))
        if (m * n) % (a * b) != 0:
            print('Invalid Lenth')
        else:
            idx = [[m * j + i for j in range(n)] for\
                   i in range(m)]
            vis = [[False for j in range(n)] for\
                   i in range(m)]
            search((n * m) // (a * b))
            print('Follows are all solutions to fill: ')
            for i in range(len(final)):
                print(final[i])
            print('There are '+str(len(final))+' ways to fill')
            numk = tt.numinput('Choose an Approach',\
                               'Ranging from 1-'+\
                               str(len(final)),1,minval=1,\
                               maxval=len(final))
            num = int(numk)
            draw(final[num-1])

if __name__ == '__main__':
    main()
