# CONSTANTE = variaveis que nao vao mudar durante a execucao do programa

velocidade = 61; # velocidade atual do carro
local_carro = 100; # local em que o carro esta na estrada

RADAR_1 = 60; # velocidade atual do carro
LOCAL_1 = 100; # local do radar 1 
RADAR_RANGE = 1; # A distancia onde o radar pega

velocidade_carro_passou_radar_1 = velocidade > RADAR_1;
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1;
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_carro_passou_radar_1;

if velocidade > RADAR_1:
    print("Velocidade carro passou do radar 1");

if carro_passou_radar_1:
    print("Carro passou no radar 1");

if carro_multado_radar_1:
    print("Carro multado no radar 1");