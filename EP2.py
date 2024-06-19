
#A nota deste EP foi 10.0

import math  # Importa o módulo de matemática para usar a função sqrt (raiz quadrada)

def distancia(P1, P2):
    """
    Calcula a distância entre dois pontos fornecidos P1 e P2.
    
    Args:
    P1 (list): Lista contendo as coordenadas (x, y) do primeiro ponto.
    P2 (list): Lista contendo as coordenadas (x, y) do segundo ponto.
    
    Returns:
    float: Distância entre os pontos P1 e P2.
    """
    # Extrai as coordenadas x e y de cada ponto
    x1, y1 = P1
    x2, y2 = P2
    
    # Calcula a distância usando a fórmula da distância euclidiana
    distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    return distancia  # Retorna a distância calculada entre os dois pontos

def aceleracaoGravitacional(Astro, P):
    """
    Calcula a aceleração da atração gravitacional exercida pelo astro sobre a nave no ponto P.
    
    Args:
    Astro (list): Lista contendo as informações do astro: [posição (x, y), massa, raio].
    P (list): Lista contendo as coordenadas (x, y) do ponto onde está a nave.
    
    Returns:
    list: Lista contendo as componentes da aceleração [ax, ay].
    """
    # Constante de gravitação universal
    G = 8.65e-13
    
    # Extrai as informações do astro: posição, massa e raio
    posicao, massa_astro, raio = Astro
    x_astro, y_astro = posicao
    x, y = P
    
    # Calcula a distância entre o astro e o ponto P usando a função distancia
    d = distancia(posicao, P)
    
    # Calcula as componentes da aceleração gravitacional usando a lei da gravitação universal
    ax = G * massa_astro * (x_astro - x) / d ** 3
    ay = G * massa_astro * (y_astro - y) / d ** 3
    
    return [ax, ay]  # Retorna as componentes da aceleração gravitacional


def aceleracaoResultante(Astros, P):
    """
    Calcula a aceleração resultante da soma das contribuições exercidas por cada astro sobre a nave no ponto P.
    
    Args:
    Astros (list): Lista contendo as informações de todos os astros: [[posição (x, y), massa, raio], ...].
    P (list): Lista contendo as coordenadas (x, y) do ponto onde está a nave.
    
    Returns:
    list: Lista contendo as componentes da aceleração resultante [ax, ay].
    """
    # Inicializa as componentes da aceleração resultante como zero
    ax_total, ay_total = 0, 0
    
    # Itera sobre todos os astros para calcular a contribuição de cada um
    for astro in Astros:
        # Calcula a aceleração gravitacional exercida pelo astro sobre a nave no ponto P
        ax_astro, ay_astro = aceleracaoGravitacional(astro, P)
        
        # Soma as componentes da aceleração gravitacional de cada astro às totais
        ax_total += ax_astro
        ay_total += ay_astro
    
    return [ax_total, ay_total]  # Retorna as componentes da aceleração resultante


def deteccaoColisao(Nave, Astros):
    """
    Verifica se ocorre sobreposição entre a nave fornecida com algum dos astros presentes na lista de Astros.
    
    Args:
    Nave (list): Lista contendo as informações da nave: [posição (x, y), velocidade (vx, vy), raio].
    Astros (list): Lista contendo as informações de todos os astros: [[posição (x, y), massa, raio], ...].
    
    Returns:
    bool: True se a nave colidiu com algum astro, False caso contrário.
    """
    colidiu = False  # Inicializa a variável de colisão como False
    for astro in Astros:  # Itera sobre cada astro na lista de Astros
        if not colidiu:  # Verifica se uma colisão já foi detectada
            distancia_centros = distancia(Nave[0], astro[0])  # Calcula a distância entre os centros da nave e do astro
            soma_raios = Nave[2] + astro[2]  # Calcula a soma dos raios da nave e do astro
            if distancia_centros <= soma_raios:  # Verifica se a distância entre os centros é menor ou igual à soma dos raios
                posicao = astro[0]  # Obtém a posição do astro
                distancia_ao_centro = distancia(Nave[0], posicao)  # Calcula a distância da nave ao centro do astro
                proporcao = (distancia_ao_centro - Nave[2]) / distancia_ao_centro  # Calcula a proporção para reposicionar a nave
                novo_x = posicao[0] + (Nave[0][0] - posicao[0]) * proporcao  # Calcula a nova coordenada x da nave
                novo_y = posicao[1] + (Nave[0][1] - posicao[1]) * proporcao  # Calcula a nova coordenada y da nave
                Nave[0] = [novo_x, novo_y]  # Atualiza a posição da nave para evitar a colisão
                colidiu = True  # Define que uma colisão foi detectada
    return colidiu  # Retorna True se uma colisão foi detectada, False caso contrário



def atualizaNave(Nave, Astros, delta_t):
    """
    Atualiza a posição e velocidade da nave sujeita às forças de atração gravitacional dos astros, após um intervalo de tempo delta_t.
    
    Args:
    Nave (list): Lista contendo as informações da nave: [posição (x, y), velocidade (vx, vy), raio].
    Astros (list): Lista contendo as informações de todos os astros: [[posição (x, y), massa, raio], ...].
    delta_t (float): Intervalo de tempo.
    
    Returns:
    list: Lista contendo as novas posições e velocidades atualizadas da nave.
    """
    # Extrai as informações da posição e velocidade da nave
    pNave = Nave[0]
    vNave = Nave[1]
    
    # Calcula a aceleração resultante exercida pelos astros sobre a nave no ponto atual
    ar = aceleracaoResultante(Astros, pNave)

    # Calcula a nova posição da nave usando a equação de movimento com aceleração constante
    novo_x = pNave[0] + vNave[0] * delta_t + (ar[0] * delta_t ** 2 / 2)
    novo_y = pNave[1] + vNave[1] * delta_t + (ar[1] * delta_t ** 2 / 2)
    
    # Calcula a nova velocidade da nave usando a equação de movimento com aceleração constante
    velocidade_x = vNave[0] + ar[0] * delta_t
    velocidade_y = vNave[1] + ar[1] * delta_t

    # Atualiza as informações de posição e velocidade da nave
    Nave[0] = [novo_x, novo_y]
    Nave[1] = [velocidade_x, velocidade_y]
    
    return Nave  # Retorna as novas posições e velocidades atualizadas da nave



def distanciaAstroMaisProximo(Nave, Astros):
    """
    Calcula a distância da nave em relação ao astro mais próximo dentre os astros presentes na lista Astros.
    A distância é medida em relação à superfície do astro e da nave. Em caso de nave colidida, a distância é zero.
    
    Args:
    Nave (list): Lista contendo as informações da nave: [posição (x, y), velocidade (vx, vy), raio].
    Astros (list): Lista contendo as informações de todos os astros: [[posição (x, y), massa, raio], ...].
    
    Returns:
    float: Distância da nave ao astro mais próximo.
    """
    # Inicializa a distância mínima com um valor grande
    distancia_min = 9999999999.999
    
    # Itera sobre todos os astros para encontrar o mais próximo
    for astro in Astros:
        # Calcula a distância da nave ao astro (considerando a superfície)
        distancia_superficie = distancia(Nave[0], astro[0]) - Nave[2] - astro[2]
        
        # Atualiza a distância mínima se necessário
        if distancia_superficie < distancia_min:
            distancia_min = distancia_superficie
    
    # Retorna a distância mínima encontrada
    if distancia_min < 0:  # Se a distância mínima for negativa (colisão), retorna zero
        return 0.0
    return distancia_min  # Caso contrário, retorna a distância mínima



def simulacao(Naves, Astros, niter, delta_t):
    """
    Realiza a simulação das trajetórias das naves sob o efeito da força gravitacional exercida pelos astros.
    
    Args:
    Naves (list): Lista contendo as informações das naves.
    Astros (list): Lista contendo as informações dos astros.
    niter (int): Número de iterações da simulação.
    delta_t (float): Intervalo de tempo da simulação.
    
    Returns:
    list: Lista das trajetórias de cada nave.
    list: Lista com as distâncias de cada nave em relação ao seu astro mais próximo a cada iteração.
    """
    # Inicializa duas listas vazias para armazenar as trajetórias e as distâncias das naves
    T = []
    D = []
    for nave in Naves:
        T.append([])
        D.append([])
    # Loop principal da simulação para cada iteração
    for j in range(niter):
        # Loop para cada nave
        for k in range(len(Naves)):
            nave = Naves[k]
            if nave:
                atualiza = True
                if D[k] and D[k][-1] <= 0:
                    atualiza = False
                if atualiza:
                    # Atualiza a posição e velocidade da nave
                    atualizaNave(nave, Astros, delta_t)
                    # Calcula a distância da nave ao seu astro mais próximo
                    dp = distanciaAstroMaisProximo(nave, Astros)
                    # Armazena as informações da nave e sua distância ao astro mais próximo
                    T[k].append(nave[0][:])
                    D[k].append(dp)
                else:
                    # Se a nave colidiu, armazena a posição atual e distância zero
                    T[k].append(nave[0][:])
                    D[k].append(0)
            else:
                # Se a nave não existe, armazena zeros
                T[k].append(0)
                D[k].append(0)
    return T, D  # Retorna as trajetórias das naves e as distâncias de cada nave ao seu astro mais próximo


#Não altere o código abaixo:
def main():
    niter = int(input("Número máximo de iterações: "))    
    delta_t = float(input("Delta t: "))
    nnaves = int(input("Número de naves: "))
    Naves = []
    for i in range(nnaves):
        print("*** Nave %d ***"%(i+1))
        x,y = input("Digite a posição (x,y): ").split()
        x,y = float(x),float(y)
        vx,vy = input("Digite a velocidade inicial (vx,vy): ").split()
        vx,vy = float(vx),float(vy)
        r = float(input("Digite o raio: "))
        Naves.append([[x,y], [vx,vy], r])

    nastros = int(input("Número de astros: "))
    Astros = []
    for i in range(nastros):
        print("*** Astro %d ***"%(i+1))
        x,y = input("Digite a posição (x,y): ").split()
        x,y = float(x),float(y)
        massa = float(input("Digite a massa: "))
        R = float(input("Digite o raio: "))        
        Astros.append([[x,y], massa, R])

    T, D = simulacao(Naves, Astros, niter, delta_t)
    for i in range(niter):
        print("********* iteração %d *********"%(i+1))
        for j in range(nnaves):
            print("*** Nave %d ***"%(j+1))
            print("Posição: ",end="")
            if len(T[j]) > i:
                P = T[j][i]
                print("(%.3f, %.3f)" % (P[0], P[1]))
            else:
                print("Nave %d não existe nesta iteração." % (j + 1))
            print("Distância ao astro mais próximo: ", end="")
            print("%.3f"%(D[j][i]))

#Não altere o código abaixo.
if __name__ == "__main__":
    main()
