#Simulating Bird Flock Behavior in Python Using Boids

#pip install p5

#to create some “boids”

from p5 import setup, draw, size, background, run

class Boid():

    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        
#create another file named main.py and put the graphics handling
#get an empty canvas with defined size and color
#setup which prepare the canvas and runs just once at the beginning
#draw which runs in a loop
  
from p5 import setup, draw, size, background, run
import numpy as np
from boid import Boid

width = 1000
height = 1000

def setup():
    #this happens just once
    size(width, height) #instead of create_canvas

def draw():
    #this happens every time
    background(30, 30, 47)

run()    

#to create lots of static boids on canvas, add the function show
#stroke function determines the color of stroke
#circle function create a circle in the defined position with a defined radius

def show(self):
    stroke(255)
    circle((self.position.x, self.position.y), radius=10)
    
#go back to main.py to create 30 boids with random positions
#random.rand generates random numbers

from p5 import setup, draw, size, background, run
import numpy as np
from boid import Boid

width = 1000
height = 1000

flock = [Boid(*np.random.rand(2)*1000, width, height) for _ in range(30)]

def setup():
    #this happens just once
    size(width, height) #instead of create_canvas

def draw():
    #this happens every time
    background(30, 30, 47)

    for boid in flock:
        boid.show()

run()    

#to define their velocity and acceleration

class Boid():

    def __init__(self, x, y, width, height):
        self.position = Vector(x, y)
        vec = (np.random.rand(2) - 0.5)*10
        self.velocity = Vector(*vec)

        vec = (np.random.rand(2) - 0.5)/2
        self.acceleration = Vector(*vec) 
        
def update(self):
    self.position += self.velocity
    self.velocity += self.acceleration        

#to add this to main.py
    
def draw():
    #this happens every time
    background(30, 30, 47)

    for boid in flock:
        boid.show()
        boid.update()
        
#keep them inside the box
#to add another function to boids.py

def edges(self):
    if self.position.x > self.width:
        self.position.x = 0
    elif self.position.x < 0:
        self.position.x = self.width

    if self.position.y > self.height:
        self.position.y = 0
    elif self.position.y < 0:
        self.position.y = self.height
        
#to get smoother movements   
#use max_speed limit to them
        
def update(self):
    self.position += self.velocity
    self.velocity += self.acceleration
    #limit
    if np.linalg.norm(self.velocity) > self.max_speed:
        self.velocity = self.velocity / np.linalg.norm(self.velocity) * self.max_speed

    self.acceleration = Vector(*np.zeros(2))

#For alignment
#have to exert a force from the current direction, towards the desired direction  
#steering = avg_vec — self.velocity    
    
def align(self, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    avg_vec = Vector(*np.zeros(2))
    for boid in boids:
        if np.linalg.norm(boid.position - self.position) < self.perception:
            avg_vec += boid.velocity
            total += 1
    if total > 0:
        avg_vec /= total
        avg_vec = Vector(*avg_vec)
        avg_vec = (avg_vec /np.linalg.norm(avg_vec)) * self.max_speed
        steering = avg_vec - self.velocity

    return steering

#apply_behaviour, which is responsible for applying every rule as we proceed
    
def apply_behaviour(self, boids):
    alignment = self.align(boids)
    self.acceleration += alignment

#in main.py
    
def draw():
    #this happens every time
    background(30, 30, 47)

    for boid in flock:
        boid.show()
        boid.apply_behaviour(flock)
        boid.update()
        boid.edges()    

#For Cohesion
#vec_to_com = center_of_mass — self.position
#steering = vec_to_com — self.velocity
        
def cohesion(self, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    center_of_mass = Vector(*np.zeros(2))
    for boid in boids:
        if np.linalg.norm(boid.position - self.position) < self.perception:
            center_of_mass += boid.position
            total += 1
    if total > 0:
        center_of_mass /= total
        center_of_mass = Vector(*center_of_mass)
        vec_to_com = center_of_mass - self.position
        if np.linalg.norm(vec_to_com) > 0:
            vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
        steering = vec_to_com - self.velocity
        if np.linalg.norm(steering)> self.max_force:
            steering = (steering /np.linalg.norm(steering)) * self.max_force

    return steering

#add the cohesion function to theapply_behaviour function

def apply_behaviour(self, boids):
    #alignment = self.align(boids)
    cohesion = self.cohesion(boids)

    #self.acceleration += alignment
    self.acceleration += cohesion
    
#For separation
#diff vector — the direction of escape — by the distance to that particular flockmate
    
def separation(self, boids):
    steering = Vector(*np.zeros(2))
    total = 0
    avg_vector = Vector(*np.zeros(2))
    for boid in boids:
        distance = np.linalg.norm(boid.position - self.position)
        if self.position != boid.position and distance < self.perception:
            diff = self.position - boid.position
            diff /= distance
            avg_vector += diff
            total += 1
    if total > 0:
        avg_vector /= total
        avg_vector = Vector(*avg_vector)
        if np.linalg.norm(steering) > 0:
            avg_vector = (avg_vector / np.linalg.norm(steering)) * self.max_speed
        steering = avg_vector - self.velocity
        if np.linalg.norm(steering)> self.max_force:
            steering = (steering /np.linalg.norm(steering)) * self.max_force

    return steering

#apply all the acceleration at the same time using the law of force adding
    
def apply_behaviour(self, boids):
    alignment = self.align(boids)
    cohesion = self.cohesion(boids)
    separation = self.separation(boids)

    self.acceleration += alignment
    self.acceleration += cohesion
    self.acceleration += separation
    
#_______________________FINISH_________________________________________________