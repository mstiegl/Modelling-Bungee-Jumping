# Model of the movement of a vertical spring
import matplotlib.pyplot as plt
dt=0.001
velocity = 0
mass = 0.2
acceleration_due_to_gravity = 9.81
weight = mass * acceleration_due_to_gravity
spring_constant = 10
unweighted_length = 1
weight_displacement = weight / spring_constant
displacement = 0.3
length = unweighted_length + weight_displacement + displacement
restoring_spring_force = -spring_constant * (length - unweighted_length)
total_force = weight + restoring_spring_force
acceleration = total_force / mass
change_in_velocity = acceleration
change_in_length = velocity
t = 0
timeLst = [0]
velocityLst = [velocity]
lengthLst = [length]
while t<3:
    t = t+dt
    timeLst.append(t)
    velocity = velocity + (change_in_velocity) *dt
    velocityLst.append(velocity)
    length = length + (change_in_length) *dt
    lengthLst.append(length)
    restoring_spring_force = -spring_constant * (length - unweighted_length)
    total_force = weight + restoring_spring_force
    acceleration = total_force / mass
    change_in_length = velocity
    change_in_velocity = acceleration
plt.plot(timeLst,lengthLst)
plt.show()