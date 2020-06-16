import pygame
import math

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255, 255, 255))

degrees = 45.0
speed = 50.0
speedX = 0
speedY = 0
viscosity = 1
viscosityType = "laminar"
gravity = -9.8
directionX = 0
directionY = 0
mass = 10.0
forces = []
timestep = 0.001
accelX = 0
accelY = 0
Px = 0
Py = 0


while(True):

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    print("Firing at", degrees, "degrees, at", speed,
        "m/s.\nViscosity is "+ str(viscosity) +" , type is " + str(viscosityType) + ", gravity is " + str(gravity) +
        ".\nThe mass of the object is " + str(mass) + ".")

    Px = 30
    Py = 429
    speedX = speed * math.cos(math.radians(degrees))
    speedY = -(speed * math.sin(math.radians(degrees)))
    directionX = speedX / abs(speed)
    directionY = speedY / abs(speed)

    for i in range(len(forces)):
        accelX += forces[i][0] / mass
        accelY += forces[i][1] / mass
    while((Py <= 430) and (Py > -500)):
        if (viscosityType == "laminar"):
            Px += speedX * timestep + 0.5*(-viscosity * speedX + accelX) * (timestep**2)
            Py += speedY * timestep + 0.5*(-gravity - viscosity * speedY - accelY) * (timestep**2)

            speedX += (-viscosity * speedX + accelX) * timestep
            speedY += (-gravity - viscosity * speedY - accelY) * timestep

            pygame.draw.circle(screen, (0,0,0), (int(Px),int(Py)), 1)
        elif (viscosityType == "turbulent"):
            Px += speedX * timestep + 0.5*(-viscosity * directionX * (speed**2) + accelX) * (timestep**2)
            Py += speedY * timestep + 0.5*(-gravity - viscosity * directionY * (speed**2) - accelY) * (timestep**2)

            speedX += (-viscosity * directionX * (speed**2) + accelX) * timestep
            speedY += (-gravity - viscosity * directionY * (speed**2) - accelY) * timestep
            directionX = speedX / abs(speed)
            directionY = speedY / abs(speed)
            speed = math.sqrt((speedX ** 2) + (speedY ** 2))

            pygame.draw.circle(screen, (0,0,0), (int(Px),int(Py)), 0.5)

    pygame.draw.circle(screen, (255,0,0), (int(Px),int(Py)), 3)
    pygame.display.flip()

    command = str(input(">")).lower()

    try:
        if(command[0:3] == "set"):

            if(command[4:9] == "speed"):
                speed = abs(float(command[10:]))
                screen.fill((255, 255, 255))

            elif(command[4:11] == "degrees"):
                if ((abs(float(command[12:])) <= 180) and (abs(float(command[12:])) >= 0)):
                    degrees = degrees = abs(float(command[12:]))
                    screen.fill((255, 255, 255))
                else:
                    print("invalid option")

            elif(command[4:13] == "viscosity"):
                viscosity = abs(float(command[14:]))
                screen.fill((255, 255, 255))

            elif(command[4:8] == "type"):
                viscosityType = str(command[8:].strip())
                screen.fill((255, 255, 255))

            elif(command[4:11] == "gravity"):
                gravity = abs(float(command[12:]))
                screen.fill((255, 255, 255))

            elif(command[4:8] == "mass"):
                mass = abs(float(command[8:]))
                screen.fill((255, 255, 255))

            else:
                print("invalid option")

        elif(command[0:6] == "forces"):
            i = 0
            for force in forces:
                print(str(i) + ". F = (" , force[0] ,",", force[1] , ")")
                i += 1

        elif(command[0:8] == "addforce"):
            space = 0
            command_space = 9
            error = 1

            for word in command[9:]:
                if(word == " "):
                    forces.append([float(command[9:command_space]),float(command[command_space+1:])])
                    error = 0
                    screen.fill((255, 255, 255))
                    break

                else:
                    command_space += 1

            if(error == 1):
                print("invalid option")

        elif(command[0:11] == "removeforce"):
            forces.pop(int(command[12:]))
            screen.fill((255, 255, 255))


        elif(command == "quit"):
            break

        else:
            print("invalid option")

    except:
        print("invalid option")

