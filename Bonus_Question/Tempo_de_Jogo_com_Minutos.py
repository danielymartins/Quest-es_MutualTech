#Tempo pode haver 3 casos
# --> Hora Final > Hora Inicial (continua no mesmo dia)
#        tempo = Hora Final - Hora Inicial
# 
# --> Hora Final == Hora Inicial (Variação de Minutos)
#
# --> Hora Inicial > Hora Final (passou da meia noite)
#          Tempo = 24 - Hora Inicial + Hora Final
#          Tempo = Hora Final - Hora Inicial + 24

x = input().split() #Lista de numeros
hora_inicial, min_inicial, hora_final, min_final = x

#Posicões das variaveis
hora_inicial = int(x[0])
min_inicial = int(x[1])
hora_final = int(x[2])
min_final = int(x[3])

#########

if hora_inicial < hora_final:
    hora = hora_final - hora_inicial
    if min_inicial < min_final:
        minutos = min_final - min_inicial
    if min_inicial > min_final:
        hora = hora - 1 #Sempre que o minuto final for maior que o minuto inicial, diminuir 1 hora (exemplo 3:30 - 4:10 = 0:40)
        minutos = (60 - min_inicial) + min_final
    if min_inicial == min_final:
        minutos = 0

      
#########
if hora_inicial > hora_final:
    hora = (24 - hora_inicial) + hora_final
    if min_inicial < min_final:
        minutos = min_final - min_inicial
    if min_inicial > min_final:
        hora = hora - 1
        minutos = (60 - min_inicial) + min_final
    if min_inicial == min_final:
        minutos = 0

######### Se a hora e minuto inicial == hora e min final, se passou 24 horas pois o enunciado disse que o tempo minimo de jogo é 1min
if hora_inicial == hora_final:
    if min_inicial < min_final:
        minutos = min_final - min_inicial
        hora = 0 #Se passaram somente alguns minutos
    if min_inicial > min_final:
        minutos = (60 - min_inicial) + min_final
        hora = 23
    if min_inicial == min_final:
        hora = 24
        minutos = 0
    
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora, minutos))
