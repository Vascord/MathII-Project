import pygame
import math

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,480))
screen.fill((0, 0, 0))

degrees = 30.0
speed = 30.0
speedX = 0
speedY = 0
viscosity = 1.0
gravity = 9.81
mass = 10.0
forces = [[100.0, 20.0]]
timestep = 0.02
accelX = []
accelY = []
Px = 0
Py = 0

def map_generator():
    return


while(True):

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    print("Firing at", degrees, "degrees, at", speed,
        "m/s.\nViscosity is "+ str(viscosity) +", gravity is " + str(gravity) +
        ".\nThe mass of the object is " + str(mass))
    #Meter aqui funçao que faz que o mapa se actualize
    speedX = speed * math.cos(degrees)
    speedY = speed * math.sin(degrees)
    for i in range(len(forces)):
        accelX[i] = forces[0][i] / mass
        accelY[i] = forces[1][i] / mass
    while(Py >= 0):
        #Perguntar ao stor se as forças são constantes(provavelmente) ou de impulso
        Px = Px + speedX * timestep + 0.5*(-viscosity * speedX + accelX) * (timestep**2)
        Py = Py + speedY * timestep + 0.5*(-gravity - viscosity * speedY + accelY) * (timestep**2)
        # massa afeta acelaração do cociente de viscosidade? Tenho quase a certeza que não pq é uma força de resposta à velocidade
        # e se houver massa envolvida também esta do lado a que desacelera mas melhor verificar
        speedX = speedX + 0.5*(-viscosity * speedX) * timestep
        speedY = speedY + 0.5*(-gravity - viscosity * speedY) * timestep

        if (Py >= 0):
            #mostra função
            pygame.draw.circle(screen, (255,255,255), (Px,Py), 0.1, 0)
        if (Py < 0):
            pygame.draw.circle(screen, (255,0,0), (Px,Py), 0.1, 0)
        pygame.display.update()
    Px = 0
    Py = 0

    command = str(input(">")).lower()

    try:
        if(command[0:3] == "set"):

            if(command[4:9] == "speed"):
                speed = abs(float(command[10:]))

            elif(command[4:11] == "degrees"):
                if ((abs(float(command[12:])) <= 180) and (abs(float(command[12:])) >= 0)):
                    degrees = degrees = abs(float(command[12:]))
                else:
                    print("invalid option")

            elif(command[4:13] == "viscosity"):
                viscosity = abs(float(command[14:]))

            elif(command[4:11] == "gravity"):
                gravity = abs(float(command[12:]))

            elif(command[4:8] == "mass"):
                mass = abs(float(command[8:]))

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
                    break

                else:
                    command_space += 1
            
            if(error == 1):
                print("invalid option")
        
        elif(command[0:11] == "removeforce"):
            forces.pop(int(command[12:] + 1))
            
        
        elif(command == "quit"):
            break

        else:
            print("invalid option")

    except:
        print("invalid option")

