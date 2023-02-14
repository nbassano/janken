#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
opciones = ["Piedra", "Papel", "Tijera"]
computadora = random.choice(opciones) #el métofodo .choice() devuelve un elemento seleccionado aleatoriamente de la secuencia especificada
jugador = False
cpu_puntaje = 0
jugador_puntaje = 0
while True:
    jugador = input("Elegís piedra, papel o tijera?").capitalize()
    ## Reglas del juego 
    if jugador == computadora:
        print("Empate :o ")
    elif jugador == "Piedra":
        if computadora == "Papel":
            print("Perdiste jua jua!", computadora, "cubre", jugador)
            cpu_puntaje+=1
        else:
            print("Ganaste >:(", jugador, "aplasta", computadora)
            jugador_puntaje+=1
    elif jugador == "Papel":
        if computadora == "Tijera":
            print("Perdiste jejej", computadora, "corta", jugador)
            cpu_puntaje+=1
        else:
            print("Ganaste, malditazeah", jugador, "cubre", computadora)
            jugador_puntaje+=1
    elif jugador == "Tijera":
        if computadora == "Piedra":
            print("PERDEDOOR JAJAJ", computadora, "aplasta", jugador)
            cpu_puntaje+=1
        else:
            print("Ok, me ganaste esta vez >:( ", jugador, "corta", computadora)
            jugador_puntaje+=1
    elif jugador=='Fin':
        print("Puntaje final:")
        print(f"CPU:{cpu_puntaje}")
        print(f"jugador:{jugador_puntaje}")
        print("me aburrí, chau")
        break #corta el bucle


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




