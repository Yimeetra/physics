from math import inf
import pygame
import sys
from vec2d import Vec2d
run = 1
g = 9.8
ppm = 100

def free_fall_force(body):
    global g
    return Vec2d(0,body.m*g)

def archimedes_force(body):
    global g
    if body.pos.y>=800:
        V = 4/3*3.14*((body.r)**3)
        p = 1000
        return Vec2d(0,-p*g*V)
    return Vec2d(0,0)

def draw_vector(sc,color,st,vec,k,w):
    pos1 = st
    pos2 = pos1 + vec*k
    pygame.draw.line(sc,color,(pos1.x,pos1.y),(pos2.x,pos2.y),w)
    a = vec.angle()
    lp = pos2-vec.normalised().rotate(a-45)*5*w/2
    rp = pos2-vec.normalised().rotate(a+45)*5*w/2
    pygame.draw.polygon(sc,color,((pos2.x,pos2.y),(lp.x,lp.y),(rp.x,rp.y)))

class Body:
    def __init__(self,x,y,m,r):
        self.pos = Vec2d(x,y)
        self.v = Vec2d(0,0)
        self.a = Vec2d(0,0)
        self.m = m
        self.forces = []
        self.force = Vec2d(0,0)
        self.r = r

    def add_force(self,f):
        self.forces.append(f)
        for f in self.forces:
            self.force += f(self)

    def update_forces(self):
        self.a = Vec2d(0,0)
        self.force = Vec2d(0,0)
        for f in self.forces:
            self.force += f(self)
        self.a = self.force/self.m
 
if __name__ == '__main__':
    body = Body(800,0,10,10)
    body.add_force(free_fall_force)
    #body.add_force(archimedes_force)

    pygame.init()
    screen = pygame.display.set_mode((1600,1000))
    getTicksLastFrame = 0
    clock = pygame.time.Clock()
    t = pygame.time.get_ticks()/1000
    dt = getTicksLastFrame-t
    getTicksLastFrame = t
    

    while run:
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,100,255),(0,800,1600,1000))
        pygame.display.set_caption(str(clock.get_fps()))

        #t = pygame.time.get_ticks()/1000
        #dt = getTicksLastFrame-t
        #getTicksLastFrame = 
        
        body.update_forces()

        dt = .001
        
        if body.pos.y+body.r >= 800:
            body.v *= -1
            body.pos.y = 800-body.r

        body.v += body.a * dt
        body.pos += body.v*dt*ppm

        #print(dt,body.v,body.pos)
        
        pygame.draw.circle(screen,(255,255,255),(body.pos.x,body.pos.y),body.r)
        draw_vector(screen,(255,0,0),body.pos,body.v,5,3)
        draw_vector(screen,(0,255,0),body.pos,body.force,1,3)

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(inf)