ids = ['Jose','Pepe','Angol','Mes','Cr7','Conej']
scores = [20.6,40.1,5.2,200.3,100.4,64]

def player_split(ids, scores):
    nombres = ids
    puntos = scores
    temp1 = []
    temp2 = []
    total1, total2 = 0, 0
    mezcla = sorted(zip(puntos,nombres),reverse = True)     #Juntamos las list y las ordenamos de mayor a menor
    tamano = len(mezcla)
    max = tamano//2
    print('\nLos jugadores son ', tamano, ', Max por equipo:',max)

    if tamano % 2 == 0:                                     #Si el equipo es par, comienza la magia
        for i in range(0, len(mezcla)):
            if((total1<total2) and (len(temp1)<max)):
                temp1.append(mezcla[i])
                total1 += mezcla[i][0]
            elif(len(temp2)<max):
                temp2.append(mezcla[i])
                total2 += mezcla[i][0]
            else:
                temp1.append(mezcla[i])

        #print(temp1,'- Score del equipo', total1,'- Jugadores ',len(temp1))
        #print(temp2,'- Score del equipo', total2,'- Jugadores ',len(temp2))

        return temp1, temp2

    else:
        print('\nEl equipo es Impar - Te falta un jugador o despide a alguno, con buena onda')

team1, team2 = player_split(ids, scores)

print(team1)
print(team2)