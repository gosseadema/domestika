import math
import datetime

def setup():

    size(1000, 1000)
    no_stroke()
    fill (255); rect (0,0,width, height)  

    wd = width
    hg = height
    mb = 50 # min size triangle 

#   3 triangles (with left part (second triangle) and right part (third triangle) outside sketch)
    f_triangle ((width/2 , 0), (0, height), (width, height), mb, 1)
    f_triangle ((-width/2 , 0), (width/2, 0), (0, height), mb, 1)
    f_triangle ((width/2 , 0), (width + width/2, 0), (width, height), mb, 1)

#   border around image   
    ma = mb * 0.05          # 5% whitespace around each triangle (0 = no whitespace)
    mx  = ma * math.sqrt(3) # distance delta x (x offset: base triangle)
    my2 = ma * 2            # distance delta y (y offset: base triangle)
    fill (255)
    rect (0, 0 ,mx , hg)            # left 
    rect (width - mx, 0, my2, hg)   # right
    rect (0, 0 ,wd, my2 )           # top
    rect (0, hg - my2 ,wd , my2)    # bottom

    time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
    save ('Triangle_' + time_now + '.png')

def f_triangle (p1, p2, p3, maxbase, depth):

    if (p2[1] == p3[1] and abs(p1[1] - p2[1]) <= maxbase) or (p1[1] == p2[1] and abs(p1[1] - p3[1]) <= maxbase) or (depth > 2 and random_int(4) == 0): 
        draw_triangle (p1, p2, p3, maxbase)
    else:
        if p2[1] == p3[1]: # point up
            dx = (p3[0] - p2[0]) / 4
            dy = (p3[1] - p1[1]) / 4
            pa = (p2[0] + dx,      p1[1] + dy + dy)
            pb = (p3[0] - dx,      p1[1] + dy + dy)
            pc = (p2[0] + dx + dx, p2[1])            
        else: # point downwards
            dx = (p2[0] - p1[0]) / 4
            dy = (p3[1] - p1[1]) / 4
            pa = (p1[0] + dx + dx , p1[1])
            pb = (p1[0] + dx , p1[1] + dy + dy)
            pc = (p2[0] - dx , p1[1] + dy + dy)
        # 4 triangles inside the given triangle values
        f_triangle (p1, pa, pb, maxbase, depth + 1)
        f_triangle (pa, pb, pc, maxbase, depth + 1)
        f_triangle (pa, p2, pc, maxbase, depth + 1)
        f_triangle (pb, pc, p3, maxbase, depth + 1)

def draw_triangle (p1, p2, p3, maxbase):

    ma = maxbase * 0.05     # 5% whitespace around each triangle (0 = no whitespace)
    mx  = ma * math.sqrt(3) # distance delta x (x offset: base triangle)
    my1 = ma * 1            # distance delta y (y offset: base triangle)
    my2 = ma * 2            # distance delta y (y offset: point triangle)

    r = random_int( 10, 150) # red
    g = random_int( 20, 200) # green
    b = random_int( 50, 250) # blue
    fill (r,g,b)

    begin_shape()
    if p1[1] == p2[1]: # point downwards
        vertex (p1[0] + mx, p1[1] + my1)
        vertex (p2[0] - mx, p2[1] + my1)
        vertex (p3[0]     , p3[1] - my2)        
    else: # point upwards 
        vertex (p1[0]     , p1[1] + my2)
        vertex (p2[0] + mx, p2[1] - my1)
        vertex (p3[0] - mx, p3[1] - my1)
    end_shape (CLOSE)