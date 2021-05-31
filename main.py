#import math
#import
#user input
    #distance to target
    #muzzle velocity
    #ballistic coefficent
    #bullet weight
    #maybe add ballistic profile saving from user input?
        #convert to standardized values from fps/mps

#static variables that shouldn't change
GRAV = 9.81
elev = 0
class BallisticProfile:
    def __init__(self, name, mv, bc):
        self.name = name
        self.mv = mv #fps
        self.bc = bc

m118 = BallisticProfile("m118",2650, .496)
print(m118.bc)

distance = int(input('Input distance in metric: '))
print(str(distance) + ' meters\n')


velocity = m118.mv / 3.281

time = distance/velocity

drop = elev+(.5)*(GRAV)*(time)

print("Drop is " + str(drop) + ' meters')

    #standard .308
        #MV = 2650 #fps / 807.72 m/s
        #BC = G1 .505 @ > 2800 fps, .496 2800-1800fps, .485 < 1800fps

    #distance
    #
#calculations
    #Time to target
    #pull of gravity over distance
        #-9.81m/s
        #32ft/
    #distance = elevation + (.5)(9.81m/s)(time)^2
    #vertical drop = 0 + (.5)(9.81m/s)(time in seconds)^2
    #25.525 = 0 + (.5)(9.81m/s)(5s)
#return result
