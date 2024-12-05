import math
import datetime

# gives circle through 3 points
def define_circle(p1, p2, p3):
    t  = p2[0] * p2[0] + p2[1] * p2[1]
    bc = (p1[0] * p1[0] + p1[1] * p1[1] - t) / 2
    cd = (t - p3[0] * p3[0] - p3[1] * p3[1]) / 2
    dt = (p1[0] - p2[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p2[1])
    cx = (bc*(p2[1] - p3[1]) - cd*(p1[1] - p2[1])) / dt
    cy = ((p1[0] - p2[0]) * cd - (p2[0] - p3[0]) * bc) / dt
    radius = math.sqrt((cx - p1[0])**2 + (cy - p1[1])**2)
    return cx, cy, radius

def setup():
    size(1000, 1600)

    mb = 50    # min size triangle 

    background (255)
    stroke (255) 
    stroke_weight (mb * 0.05) # no need for extra math
    
    # blue (left, right)
    f_triangle  ((-width/2 , 0), (width/2, 0), (0, height), (20, 80), (50, 140), (110, 250), mb, 1, 4 ,6 , 3 , 0)
    f_triangle  ((width/2 , 0), (width + width/2, 0), (width, height), (20, 80), (50, 140), (110, 250), mb, 1, 4 ,6 , 3, 0)

    # white (overlay, round by colors) (left, right)
    f_triangle  ((-width/2 , 0), (width/2, 0), (0, height), (230, 255), (230, 255), (230, 255), mb/2, 1, 6 ,7 , 0, 20)
    f_triangle  ((width/2 , 0), (width + width/2, 0), (width, height), (230, 255), (230, 255), (230, 255), mb/2, 1, 6 ,7 , 0, 20)

    # green
    f_triangle  ((width/2 , 0), (0, height), (width, height), (10, 50), (150, 200), (50, 200), mb, 1, 6 ,7, 0, 0)
    
    # yellow (overlay)
    f_triangle  ((width/2 , 0), (0, height), (width, height), (200, 250), (200, 250), (10, 20), mb, 1, 7 ,7, 0, 20)

    # red (overlay)
    f_triangle  ((width/2 , 0), (0, height), (width, height), (150, 255), (10, 20), (10, 20), mb, 1, 5 ,6, 0, 10)

    fill (255)
    rect (0, 0 ,mb * 0.03, height)               # left border
    rect (width, 0 ,width - (mb * 0.03), height) # right border 

    # save card
    time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
    save ('Triangle_' + time_now + '.png')

# p1, p2, p3  = the 3 triangle points (x, y)
# r, g, b     = used for random rgb color values (minvalue, maxvalue)
# minbase     = minimal length of the base of the triangle (draw triangle and exit recursive loop) 
# mindept     = there is a 20% change for a large triangle, beyond this number of recursive loops
# maxdept     = draw triangle after this number of recursive loops
# colorcircle = make colors brighter
# overlay     = reduce the probability that a triangle will be drawn (0 = always). Used for additional layers

def f_triangle (p1, p2, p3, r, g, b, minbase, depth, mindepth, maxdepth, colorcircle, overlay):

    if ((p2[1] == p3[1] and abs(p1[1] - p2[1]) <= minbase) or (p1[1] == p2[1] and abs(p1[1] - p3[1]) <= minbase) or (depth >= mindepth and random_int(4) == 0) or (depth == maxdepth)): 
        if (random_int(overlay) == 0): # probability for additional layers. 
            draw_triangle (p1, p2, p3, r, g, b , minbase, colorcircle)
    else:
        if p2[1] == p3[1]: # point upwards, calculate new points
            dx = (p3[0] - p2[0]) / 4
            dy = (p3[1] - p1[1]) / 4
            pa = (p2[0] + dx,      p1[1] + dy + dy)
            pb = (p3[0] - dx,      p1[1] + dy + dy)
            pc = (p2[0] + dx + dx, p2[1])            
        else: # point downwards, calculate new points
            dx = (p2[0] - p1[0]) / 4
            dy = (p3[1] - p1[1]) / 4
            pa = (p1[0] + dx + dx , p1[1])
            pb = (p1[0] + dx , p1[1] + dy + dy)
            pc = (p2[0] - dx , p1[1] + dy + dy)
        # draw 4 triangles inside the given triangle (p1, p2, p3)
        f_triangle (p1, pa, pb, r, g, b, minbase, depth + 1, mindepth, maxdepth, colorcircle, overlay)
        f_triangle (pa, pb, pc, r, g, b, minbase, depth + 1, mindepth, maxdepth, colorcircle, overlay)
        f_triangle (pa, p2, pc, r, g, b, minbase, depth + 1, mindepth, maxdepth, colorcircle, overlay)
        f_triangle (pb, pc, p3, r, g, b, minbase, depth + 1, mindepth, maxdepth, colorcircle, overlay)

def draw_triangle (p1, p2, p3, r, g, b, maxbase, colorcircle):

    mx, my1, my2 = 0,0,0

    if colorcircle > 0: # reduce colors: pct depends on distance from a point
        dtmax = math.sqrt ((width / 2) ** 2 + height ** 2) # base point = (1/2 width, height)
        dx = abs((width / 2) - p1[0]) * colorcircle
        dy = abs(height - p1[1]) * colorcircle
        dt = math.sqrt (dx * dx + dy * dy)
        pct = dt / dtmax
    else:
        pct = 1

    rv =  pct * random_int(r[0], r[1]) # red
    gv =  pct * random_int(g[0], g[1]) # green
    bv =  pct * random_int(b[0], b[1]) # blue
    fill (rv,gv,bv)
    
    # Bonus: circle if white (no border)
    if (r == (230, 255) and g == (230, 255) and b == (230, 255)):
        cx, cy, radius = define_circle(p1, p2, p3)        
        fill (rv,gv,bv)    
        circle (cx, cy, radius*2)
    else: # triangle
        begin_shape() # triangle
        if p1[1] == p2[1]: # point downwards
            vertex (p1[0], p1[1])
            vertex (p2[0], p2[1])
            vertex (p3[0], p3[1])        
        else: # point upwards 
            vertex (p1[0], p1[1])
            vertex (p2[0], p2[1])
            vertex (p3[0], p3[1])
        end_shape (CLOSE)
