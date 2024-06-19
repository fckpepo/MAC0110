#A nota deste EP foi 10.0

import random

MAX_TENTATIVAS = 6
NUM_LETRAS = 5

def main(): 
    ' Implementa mecanismo principal do jogo. '
    lingua = ''
    while lingua != 'P' and lingua != 'I':
        lingua = input("Qual o idioma (I para inglês ou P para português)? ").upper()
    if lingua == 'P':
        lista_palavras = cria_lista_palavras('palavras.txt')
    elif lingua == 'I':
        lista_palavras = cria_lista_palavras('words.txt')

    palavra = lista_palavras[random.randint(0, len(lista_palavras) - 1)]
    
    num_tentativas = 0
    lista_tentativas = []
    ganhou = False
    teclado = inicializa_teclado()

    while num_tentativas < MAX_TENTATIVAS and not ganhou:
        imprime_teclado(teclado)
        palavra_valida = False
        while not palavra_valida:
            chute = input("Tentativa {}: ".format(num_tentativas + 1)).strip()
            if chute in lista_palavras:
                palavra_valida = True
            else:
                print("Palavra inválida!")
        feedback = checa_tentativa(palavra, chute)
        lista_tentativas.append((chute, feedback))
        imprime_resultado(lista_tentativas)
        atualiza_teclado(chute, feedback, teclado)
        if feedback == [1] * NUM_LETRAS:
            ganhou = True
        num_tentativas += 1

    if ganhou:
        print("PARABÉNS!")
    else:
        print("Que pena... A palavra era",palavra,".")

##### FUNÇÕES PRONTAS #####

def inicializa_teclado():
    '''
    Devolve a lista com as teclas na ordem.
    As letras que aparecem nos chutes e que não estão no teclado são substituídas por ' '.
    '''
    
    teclado = [['q','w','e','r','t','y','u','i','o','p'],
               ['a','s','d','f','g','h','j','k','l'],
               ['z','x','c','v','b','n','m']]
    return teclado

def imprime_teclado(teclado):
    ''' Exibe o teclado com as letras possiveis. '''   
    print('-----------------------------------------')
    for linha in teclado:
        for letra in linha:
            print(letra, end = ' ')
        print()
    print('-----------------------------------------')

##### FUNÇÕES OBRIGATÓRIAS #####

def cria_lista_palavras(nome_arquivo):
    ''' recebe uma string com o nome do arquivo e devolve uma lista
        contendo as palavras do arquivo'''
    arq = open(nome_arquivo, 'r')
    palavras = []
    for linha in arq:
        linha = linha.strip()
        palavras.append(linha)
    arq.close()
    return palavras

def checa_tentativa(palavra, chute): 
    ''' Recebe a `palavra` secreta e o `chute` do usuario e devolve
     uma lista ‘feedback’ de 5 elementos para indicar acertos e erros. 
     A lista `feedback` deve conter o 
     valor 1 (verde) se a letra correspondente em `chute` ocorre na mesma posicao
     em `palavra` (letra certa no lugar certo), deve conter 2 se a letra 
     em `chute` ocorre em outra posicao em `palavra` (letra certa no lugar errado),
     e deve conter 0 caso contrario. '''
    feedback = [0] * NUM_LETRAS
    for i in range(NUM_LETRAS):
        if chute[i] == palavra[i]:
            feedback[i] = 1
        elif chute[i] in palavra:
            feedback[i] = 2
    return feedback

def imprime_resultado(lista): 
    ''' Recebe a lista de tentativas e imprime as tentativas,
      usando * para verde , + para amarelo e _ para letras que não aparecem na 
      palavra sorteada. A lista de tentativas tem formato 
      [[chute1, feedback1], [chute2, feedback2], …, [chuten,feedbackn]. 
      Esta funcao nao devolve valor. '''
    for tentativa, feedback in lista:
        resultado = ''
        for i in range(NUM_LETRAS):
            if feedback[i] == 1:
                resultado += '*'
            elif feedback[i] == 2:
                resultado += '+'
            else:
                resultado += '_'
        print(tentativa, resultado) 

def atualiza_teclado(chute, feedback, teclado):
    ''' Modifica teclado para que as letras marcadas como inexistentes
	 no chute sejam substituidas por espacos. Esta funcao nao devolve valor.'''
    for i in range(NUM_LETRAS):
        if feedback[i] == 0:
            for linha in teclado:
                for j in range(len(linha)):
                    if linha[j] == chute[i]:
                        linha[j] = ' '
                        
##### FUNÇÕES EXTRAS (caso existam) #####

##### NÃO ALTERE O TRECHO ABAIXO #####
if __name__ == "__main__":
    main()
