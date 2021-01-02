import math # biblioteca pra usar função sqrt (raiz quadrada)

# PONTO INICIAL - CASA DO INDIO NESSE CASO
pontoIni = (5,5)

# LISTA DE DADOS LIDOS DO BANCO
name = ['Indio', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
data = ( (3,6), (4,10), (15,20), (5,8), (10,12), (20,30), (-2, -10), (500,20), (-1000, -2500), (4,4), (13, 30), (2, -10), (50, -35), (2,76), (5,2), (2,5), (8,3), (1,2))




# esses dados acima são só para testes, depois tu terá que dar um jeito de armazenar neles os dados do teu banco

coordenadas = list(data)  # variavel 'coordenadas' receberá todos os dados acima no formato de lista

# Função pra calcular a distância
def distance(xi,xii,yi,yii): # usa como parâmetro o eixo X e Y de dois pontos pra calcular o módulo do vetor resultante (distância entre pontos)
    sq1 = (xi-xii)*(xi-xii) # sq1 recebe o resultante do eixo X '(xi-xii)' e eleva este valor ao quadrado (multiplicando por ele mesmo)
    sq2 = (yi-yii)*(yi-yii) # sq2 é a mesma coisa, só que pro eixo Y
    return math.sqrt(sq1 + sq2) # soma os quadrados dos eixos X e Y, em seguida tira a raiz quadrada deste valor com a função sqrt (square root) e por fim retorna o valor que seria a distância entre dois pontos
    # na matemática a fórmula seria raiz(x²+y²), essa função acima é basicamente esta formula


# MENOR PONTO INICIAL EH O PRIMEIRO VALOR DA LISTA
menorPonto = 0 # essa variável futuramente irá apontar para o número da casa com a menor coordenada da lista

# CRIA ARRAY FINAL COM AS COORDENADAS
coordFinal = list() # cria o vetor 'finalArray' no formato de lista, resultado final será inserido nele aos poucos
coordFinal.append(pontoIni) # primeiro valor deste será a coordenada da tua casa '(pontoIni)'
nomeFinal = list()
nomeFinal.append(name[0])


# Essa funçao aqui é a braba. Ela irá se repetir até que todos os valores estejam organizados
def getDistList(pontoIni):

    # INICIALIZA AS VARIAVEIS GLOBAIS DENTRO DA FUNCAO
    global menorPonto

    if (len(coordenadas) > 0): # inicia uma estrutura de condição, sendo a condição o vetor 'coordenadas' ter um tamanho maior que 0. Meio que a cada repetição desta funçao, uma coordenada será retirada deste vetor, reduzindo seu tamanho e isto irá se repetir até que ele fique vazio
        menorDist = distance(pontoIni[0], coordenadas[0][0], pontoIni[1], coordenadas[0][1]) # variavel 'menorDist' receberá um valor que será passado pela função de calcular distância vista anteriormente, ele passa pra esta função quatro parâmetros (valores) o primeiro sendo o eixo X da coordenada da tua casa, segundo é eixo X da primeira coordenada da lista, terceiro e quarto são iguais ao primeiro e segundo, porém para o eixo Y
        menorPonto = 0 # aqui só está inicializando a variavel com um valor, usamos 0 pq ele corresponde à primeira casa do vetor (em python vetores começam na casa 0), que seria a coordenada usada na linha de cima

        for d in range (len(coordenadas)): # estrutura de repetição, à cada ciclo a variavel 'd' receberá um valor diferente, ele que será utilizado como índice para apontar para uma casa do vetor 'coordenadas', começando pela casa 0 até a última

            # CHAMA FUNCAO PRA COMPRAR DISTANCIAS
            actualDist = distance(pontoIni[0], coordenadas[d][0], pontoIni[1], coordenadas[d][1]) # irá calcular a distância entre o ponto atual, que muda a cada repetição (primeira casa, segunda, terceira, depende da variável 'd' supracitada), e o último ponto (que fica armazenado na variavel 'pontoIni')

            if (actualDist < menorDist): # outra condicional, desta vez checa se a distância que acabara de ser calculada é menor que a que calculados um pouco antes
                menorDist = actualDist # se acontecer da distância que calculamos agora ser menor que 'menorDist', então atualizaremos o valor da 'menorDist' para o da 'actualDist'
                menorPonto = d # e armazenamos no 'menorPonto' o endereço dessa coordenada na lista, para futuramente sabermos como pegar o valor da coordenada de menor distância
        
        # resumo destas últimas etapas: nós comparamos todos os pontos da lista de coordenadas com o ponto atual (sendo o primeiro tua casa), após acharmos a menor distância, pegamos a localização dessa coordenada na lista

        pontoIni = coordenadas[menorPonto] # a variavel 'pontoIni' que marca o ponto atual (primeira repetição seria o da tua casa) irá ser atualizada para o ponto com a menor distância ('menorPonto' está indicando qual casa da lista que contém tal valor)

        coordFinal.append(coordenadas[menorPonto]) # o vetor 'finalArray' irá receber o valor desse ponto
        nomeFinal.append(name[menorPonto+1])

        coordenadas.remove(coordenadas[menorPonto]) # removemos este ponto da lista de coordenadas
        name.remove(name[menorPonto+1])
        # CHAMA FUNCAO PRA NOVA COMPARACAO
        getDistList(coordFinal[len(coordFinal)-1]) # esta função irá chamar a si mesma (recursividade) para fazer a análise novamente e descobrir o próximo ponto de menor distância, passando como parâmetro o valor da última coordenada do vetor 'finalArray'
    
    finalArray = coordFinal + nomeFinal

    return finalArray # depois que determinarmos a ordem de todos os pontos, a função retornará o valor do 'finalArray'

finalCoords = getDistList(pontoIni) # criamos o vetor 'finalCoords' que irá chamar a função acima e receberá o valor do 'finalArray'


# print(finalCoords) # print feio puta merda Renatão



# print bonitão
print('Coordenadas organizadas de maneira à formar a menor distância entre elas:')
for x in range (int(len(finalCoords)/2)):
        print(finalCoords[int(x+len(finalCoords)/2)], '  ', finalCoords[x])