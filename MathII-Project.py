import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,480))
screen.fill((0, 0, 0))

degrees = 30.0
speed = 30.0
viscosity = 1.0
gravity = 9.81
forces = [[100.0, 20.0]]

def map_generator():
    return


while(True):

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            exit()

    print("Firing at", degrees, "degrees, at", speed,
        "m/s.\nViscosity is "+ str(viscosity) +", gravity is " + str(gravity) +" .")
    #Meter aqui funçao que faz que o mapa se actualize

    command = str(input(">")).lower()

    if(command[0:3] == "set"):

        if(command[4:9] == "speed"):
            try:
                speed = abs(float(command[10:]))
            except:
                print("invalid option")

        elif(command[4:11] == "degrees"):
            try:
                if ((abs(float(command[12:])) <= 180) and (abs(float(command[12:])) >= 0)):
                    degrees = degrees = abs(float(command[12:]))
                else:
                    print("invalid option")
            except:
                print("invalid option")

        elif(command[4:13] == "viscosity"):
            try:
                viscosity = abs(float(command[14:]))
            except:
                print("invalid option")

        elif(command[4:11] == "gravity"):
            try:
                gravity = abs(float(command[12:]))
            except:
                print("invalid option")

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
                try:
                    forces.append([float(command[9:command_space]),float(command[command_space+1:])])
                    error = 0
                    break
                except:
                    print("invalid option")
                    error = 0
                    break

            else:
                command_space += 1
        
        if(error == 1):
            print("invalid option")
    
    elif(command[0:11] == "removeforce"):
        try:
            forces.pop(int(command[12:]))
        except:
            print("invalid option")
    
    elif(command == "quit"):
        break

    else:
        print("invalid option")

