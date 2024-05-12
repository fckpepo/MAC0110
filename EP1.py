#A nota deste EP foi 9.2
#(-0,4) Erro de formatação: As impressões deveriam ser exatamente como no enunciado.
#(-0,4) Código confuso nas linhas 30-51: todo esse trecho poderia estar fora do laço principal.

velocidade_media = 0
distancia_total = 0 
tempo_total = 0  
distancia_anterior = 0  
continuar = True
desconto = False
maior_bpm = 0

while continuar:
    gps = input("Digite (ou copie e cole) os dados do seu GPS, linha por linha, e termine com a linha 000: ")
    if gps == "000":
        continuar = False
    else:
        metros = int(gps) // 1000
        bpm = int(gps) % 1000
        if bpm > maior_bpm:
            maior_bpm = bpm
        else: 
            maior_bpm = maior_bpm
        if distancia_anterior != 0:
            distancia_parcial = metros - distancia_anterior
            distancia_total = distancia_total + distancia_parcial
            tempo_total = tempo_total + 1
        distancia_anterior = metros
        
        if tempo_total >= 1:
            velocidade_media = distancia_total / tempo_total
            
        if velocidade_media >= 4:
            pelotao = "QUENIA"
        elif velocidade_media < 4 and velocidade_media >= 2:
            pelotao = "AZUL"
        else:
            pelotao = "BRANCO"

        soma_divisores = 0
        divisores = 1

        while divisores <= maior_bpm:
            if maior_bpm % divisores == 0:
                soma_divisores = soma_divisores + divisores
            divisores = divisores + 1
        soma_divisores = soma_divisores - maior_bpm
        if soma_divisores >= maior_bpm: 
            desconto = True
        else:
            desconto = False

idade_aptidao_fisica = 220 - maior_bpm

print("##### SEGUEM AS SUAS ESTATISTICAS #####")
if (int(idade_aptidao_fisica)) < 10:
    print("Sua idade de aptidão física não pode ser calculada!")
else:
    print("Sua idade de aptidão física é: " + str(idade_aptidao_fisica))
print("Seu pelotão é " + str(pelotao))
if desconto == True:
    print("Parabéns! Você terá desconto na inscrição! \o/\o/\o/") 
