import math
import datetime

def settings():
    size(1000, 1000)

def setup():
    x_elements = 26                                    # number of triangles in upper line 
    y_elements = round (x_elements / (math.sqrt(3)/2)) # optimal number of Y elements

    wd = width
    hg = height

    no_stroke()                           # no lines
    fill (255); rect (0,0,width, height)  # white background with no lines

    t_widht = wd / x_elements
    ma = t_widht * 0.05     # 5% whitespace around each triangle (0 = no whitespace)
    mx  = ma * math.sqrt(3) # distance delta x (x offset: base triangle)
    my1 = ma * 1            # distance delta y (y offset: base triangle)
    my2 = ma * 2            # distance delta y (y offset: point triangle)
    t_height = (hg - my2) / y_elements # height correction with margin

    y_pos  = [my1 + (i * t_height) for i in range (y_elements+1)]          # Y positions 
    x_pos0 = [(i * t_widht) for i in range (x_elements+1)]                 # X positions for even Y-values
    x_pos1 = [(i * t_widht) - (t_widht / 2) for i in range (x_elements+2)] # X positions for uneven Y-values

    for y in range (y_elements):
        if y%2 == 0: # even Y values
            for x in range (x_elements*2+1):
                p = int (x/2)    
                if x%2 == 0: # triangle point upwards
                    p1= (x_pos0[p]         , y_pos[y]     + my2)
                    p2= (x_pos1[p]     + mx, y_pos[y + 1] - my1)
                    p3= (x_pos1[p + 1] - mx, y_pos[y + 1] - my1)
                else: # triangle point downwards
                    p1= (x_pos0[p]     + mx, y_pos[y]     + my1)
                    p2= (x_pos0[p + 1] - mx, y_pos[y]     + my1)
                    p3= (x_pos1[p + 1]     , y_pos[y + 1] - my2)
                f_triangle (p1, p2, p3)
        else: # uneven Y values
            for x in range (x_elements*2+1):
                p = int (x/2)
                if x%2 == 0: # triangle point upwards
                    p1= (x_pos1[p]     + mx, y_pos[y] + my1)
                    p2= (x_pos1[p + 1] - mx, y_pos[y] + my1)
                    p3= (x_pos0[p]         , y_pos[y+1] - my2)
                else: # triangle point downwards
                    p1= (x_pos1[p + 1]     , y_pos[y]     + my2)
                    p2= (x_pos0[p]     + mx, y_pos[y + 1] - my1)
                    p3= (x_pos0[p + 1] - mx, y_pos[y + 1] - my1)
                f_triangle (p1, p2, p3)

    no_stroke() # border around all edges
    fill (255)
    rect (0, 0 ,mx , hg)            # left 
    rect (width - mx, 0, my2, hg)   # right
    rect (0, 0 ,wd, my2 )           # top
    rect (0, hg - my2 ,wd , my2)    # bottom

    time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
    save ('Triangle_' + time_now + '.png')

def f_triangle (p1,p2,p3):

    r = random_int( 10,  50) # red
    g = random_int( 50, 200) # green
    b = random_int(100, 250) # blue
    fill (r,g,b)

    begin_shape()
    vertex (p1[0], p1[1])
    vertex (p2[0], p2[1])
    vertex (p3[0], p3[1])
    end_shape (CLOSE)
