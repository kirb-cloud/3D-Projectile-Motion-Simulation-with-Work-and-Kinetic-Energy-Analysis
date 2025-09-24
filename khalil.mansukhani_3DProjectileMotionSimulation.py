from vpython import *
#Web VPython 3.2

# setting up variables 
d = 0.2 # height of the ground object 
g = 9.81 # gravitational acceleration (m/s**2)
m = 0.5 # mass of projectile (kg)
r = 0.2 #radius of object A

#initial position
x0 = 0 
y0 = 0.5
#initial velocity magnitude 
v0 = 5.0
theta = 45 * (pi/180) #launch angle converted from degrees to radians 

#set up 3D objects 
# set up the ground as a box with (pos, size, color)
ground = box (pos = vec (3/2, -d/2, 0), size = vec (3, d, 1), color = color.white)

# set up the objectA as a sphere with (pos, radius, color)
objectA = sphere (pos = vec (x0, y0, 0), radius = r, color = color.blue, make_trail = True)
objectB = sphere (pos = vec (x0, y0, 0), radius = r, color = color.purple, make_trail = True)


#defining velocity:
objectA.v = vec(v0 * cos(theta), v0 * sin(theta), 0)
objectB.v = vec(v0 * cos(theta), v0 * sin(theta), 0)  #Horizontal velocity component (constant)

#defining momentum:
objectA.p = m * objectA.v
objectB.p = m * objectB.v


###### Measure initial kinetic energy
objectA.KE0 = ((m**2) * objectA.v.mag2)/ (2 * m)
objectB.KE0 = ((m**2) * objectB.v.mag2)/ (2 * m)

###### Initialize work 
objectA.work = 0
objectB.work = 0


#time value:
t = 0 #keep track of time  
dt = 0.001 #change in time

# work graph
workGraph = graph(title="Work on System Over Time (J/s)", xtitle="Time (s)", ytitle="Work (J)")
workACurve = gcurve(graph= workGraph, color=color.red)
workBCurve = gcurve(graph= workGraph, color=color.blue)

# kinetic energy graph 
KEGraph = graph(title="Change in Kinetic Energy Over Time (J/s)", xtitle="Time (s)", ytitle="Kinetic Energy (J)")
KEACurve = gcurve(graph= KEGraph, color=color.red)
KEBCurve = gcurve(graph= KEGraph, color=color.blue)

# run while loop as long as the projectile hasn't hit the ground 

while objectA.pos.y > 0:
    rate(200) # animation rate 
    
    
    #define force of objectA (a vector): 
    FA = vec(0, -m * g, 0) 
    #define force of objectB (a vector): 
    FB = vec(0, m, 0)
    
   
    #update momentum p using force
    objectA.p = objectA.p + (FA*dt)
    objectB.p = objectB.p + (FB*dt)
    
   
    #calculating velocity from p and m    
    objectA.v = (objectA.p / m)
    objectB.v = (objectB.p / m)
    

    #update position using velocity    
    objectA.pos = objectA.pos + (objectA.v * dt)
    objectB.pos = objectB.pos + (objectB.v * dt)
    
    ##### calculate KE
    objectA.KE = ((m**2) * objectA.v.mag2)/ (2 * m)
    objectB.KE = ((m**2) * objectB.v.mag2)/ (2 * m)
    
    ##### update work
    objectA.work += FA.dot(objectA.v * dt)
    objectB.work += FB.dot(objectB.v * dt)
    
    
    ##### calculate change in kinetic energy 
    objectA.KEF = objectA.KE - objectA.KE0
    objectB.KEF = objectB.KE - objectB.KE0
    
 
    # Plot work and change in KE for object A & B
    workACurve.plot(pos=(t, objectA.work))
    workBCurve.plot(pos=(t, objectB.work))
    KEACurve.plot(pos=(t, objectA.KEF))
    KEBCurve.plot(pos=(t, objectB.KEF))
    

    #update the time 
    t = t + dt