velocidade = 61 #Velocidade atual do carro
local_carro = 90 #Posição do carro na via

RADAR_1 = 60 #Velocidade permitida pelo radar
LOCAL_1 = 100 #Posição do radar na via
RADAR_RANGER = 1 #Alcance do radar

RADAR_RANGER_MIN = LOCAL_1 - RADAR_RANGER #ponto menor do alcance do radar em relação a via
RADAR_RANGER_MAX = LOCAL_1 + RADAR_RANGER #ponto maior do alcance do radar em relação a via

#Bloco de códio pra verificar se veiculo ultrapassou limite permitido

if velocidade > RADAR_1:
    print (f'O veiculo ultrapassou o limite permitido no radar 1, {RADAR_1}km/h')


    if RADAR_RANGER_MIN <= local_carro <= RADAR_RANGER_MAX:
        print(f'O viculo estava dentro do alcance, {RADAR_RANGER_MIN}-{RADAR_RANGER_MAX}km, do radar_1')

    elif  local_carro < RADAR_RANGER_MIN or \
          local_carro > RADAR_RANGER_MAX:
            print(f'O viculo não estava dentro do alcance, {RADAR_RANGER_MIN}-{RADAR_RANGER_MAX}km, do radar_1')

elif velocidade <= RADAR_1:
     print(f'O veiculo estava dentro do limite de velocide permitido do radar 1, {RADAR_1}km/h')


