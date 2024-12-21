# This is the Python script for your project

def eh_tabuleiro(arg):
    """
    eh tabuleiro: universal → booleano
    A função recebe um argumento de qualquer tipo e devolve True se o seu argumento \n
    corresponde a um tabuleiro e False caso contário. Um tabuleiro \n
    corresponde a um tuplo de tuplos como descrito, em que 2 ≤ m, n ≤ 100
    """

    if not isinstance(arg,tuple):
        return False
    
    num_linhas=len(arg)

    if not 2<=num_linhas<=100:
        return False

    for linha in arg:
        if not isinstance(linha,tuple): 
            return False

    num_colunas=len(arg[0])

    if not 2<=num_colunas<=100:
        return False

    for linha in arg:
        if len(linha)!=num_colunas:
            return False
        
        for valor in linha:
            if not type(valor)==int or valor not in [-1,0,1]:
                return False

    return True

def eh_posicao(arg):
    """
    eh posicao: universal → booleano \n
    Recebe um argumento de qualquer tipo e devolve True se o seu argumento \n
    corresponde a uma posição dum tabuleiro e False caso contrário. \n
    As posições no tabuleiro são definidas por um número inteiro
    """

    if type(arg)==int and arg>0 and arg<10000:
    #As posições são definidas por um número inteiro positivo
        return True
    return False 

def obtem_dimensao(tab):
    """
     obtem valor: tabuleiro x posicao → inteiro \n
    A função recebe um tabuleiro e devolve um tuplo formado pelo número de \n
    linhas m e colunas n do tabuleiro.
    """
    
    if eh_tabuleiro:
        m=len(tab)
        n=len(tab[0])
        dimensao=(m,n)
    return dimensao

def obtem_valor(tab,pos):
    """
     obtem valor: tabuleiro x posicao → inteiro \n
    A função recebe um tabuleiro e uma posiçãoo do tabuleiro, e devolve o valor \n
    contido nessa posição.
    """

    linha=identifica_linha(tab,pos)  
    coluna=identifica_coluna(tab,pos)
    return tab[linha][coluna]

def obtem_coluna(tab,pos): 
    """
    obtem coluna: tabuleiro x posicao → tuplo \n
    A função recebe um tabuleiro e uma posiçãoao do tabuleiro, e devolve um \n
    tuplo com todas as posições que formam a coluna em que esta contida a \n
    posição, ordenadas de menor a maior
    """   

    numero_linhas=obtem_dimensao(tab)[0]
    numero_colunas=obtem_dimensao(tab)[1]
    coluna_pos=identifica_coluna(tab,pos)

    valores_da_coluna=()

    #As posições começam no 1, enquanto as colunas/linhas no 0
    for linha in range(numero_linhas):
        posicao=(linha*numero_colunas)+coluna_pos+1
        valores_da_coluna+=(posicao,)
    
    return valores_da_coluna

def obtem_linha(tab,pos):
    """
    obtem linha: tabuleiro x posicao → tuplo \n
    A função recebe um tabuleiro e uma posição do tabuleiro, e devolve um tuplo \n
    com todas as posições que formam a linha em que esta contida a posição, \n
    ordenadas de menor a maior.
    """
    	
    numero_colunas=obtem_dimensao(tab)[1]
    linha_pos=identifica_linha(tab,pos)

    valores_da_linha=()
    #Variável que armazaena os valores da linha
    
    for linha in range(numero_colunas):
        #Calculo da posição
        posicao=(linha_pos*numero_colunas)+linha+1
        #adiciona esse valor a lista
        valores_da_linha+=(posicao,)
    
    return valores_da_linha

def obtem_diagonais(tab,pos):
    """
    obtem diagonais: tabuleiro x posicao → tuplo \n
    A função recebe um tabuleiro e uma posição do tabuleiro, e devolve o \n
    tuplo formado por dois tuplos de posições correspondentes `a diagonal (descendente da \n
    esquerda para a direita ) e antidiagonal (ascendente da esquerda para a direita) que \n
    passam pela posição, respetivamente.
    """

    linha_pos=identifica_linha(tab,pos)
    coluna_pos=identifica_coluna(tab,pos)
    numero_linhas=obtem_dimensao(tab)[0]
    numero_colunas=obtem_dimensao(tab)[1]

    j=coluna_pos-linha_pos

    
    #VALORES DA DIAGONAL:
    diagonal=()
    if j>=0:
    #se a coluna de pos for maior ou igual à sua linha, então primeiro valor 
    #da diagonal encontra-se na linha 0 
    
        posicao_inicial=j+1
        diagonal+=(posicao_inicial,)
        m,n = 1,j+1 #Seguinte valor da diagonal
    
    else:
    #se a coluna de pos for menor à sua linha, então então primeiro valor 
    #da diagonal encontra-se na coluna 0
    
    
        i=-j #Ao calcular j, como linha_pos>coluna_pos, j dará um valor <0. Ao inverso desse valor atribuimos o valor da linha
        posicao_inicial=(i*numero_colunas)+1
        diagonal+=(posicao_inicial,)
        m,n = i+1,1 #seguinte valor da diagonal

    while m<numero_linhas and n<numero_colunas:
    #Incrementa 1 no valor da linha/coluna da posição inicial da diagonal para chegar ao próximo valor da diagonal
        posicoes_rest=(m*numero_colunas)+n+1
        diagonal+=(posicoes_rest,)
        m+=1
        n+=1
    

    
    #VALORES DA ANTIDIAGONAL:
    antidiagonal=()

    i_adiag=numero_linhas-1 #posição da antidiagonal que se encontra na última linha do tabuleiro
    j_adiag= coluna_pos-(i_adiag-linha_pos) #valor da coluna da posição inicial - valor da distância da posição à última linha

    if j_adiag>=0:
    #se a o valor da linha de pos for maior ou igual ao da sua coluna, 
    #então o primeiro valor da antidiagonal encontra-se na última linha do tabuleiro

        posicao_inicial_a=(i_adiag*numero_colunas)+j_adiag+1
        antidiagonal+=(posicao_inicial_a,)
        m,n=i_adiag-1,j_adiag+1 
        #subir uma linha (encontrar o valor acima da posição inicial da antidiagonal que se encontra num valor de linha menor)
        #e incrementar 1 ao número da coluna da posição inicial da antidiagonal
    
    else:
    #se a o valor da linha de pos for menor ao da sua coluna, 
    #então o último valor da antidiagonal encontra-se na coluna 0 do tabuleiro
  
        posicao_inicial_a=(-j_adiag*numero_colunas)+1 #O número da coluna é 0
        #a linha do último valor da antidiagonal é -j (j_adiag<0)
        antidiagonal+=(posicao_inicial_a,)
        m,n=-j_adiag-1,1 
        #próximo valor da antidiagonal pertence à coluna 1 e a uma linha abaixo do último valor da antidiagonal
    
    while m>=0 and n<numero_colunas:
    #Retira 1 valor à linha do primeiro valor da antidiagonal e aumenta 1 valor à coluna do mesmo
        posicoes_rest_a=(m*numero_colunas)+n+1
        antidiagonal+=(posicoes_rest_a,)
        m=m-1
        n=n+1

    return(diagonal,antidiagonal)

def tabuleiro_para_str(tab):
    """
    tabuleiro para str: tabuleiro → cad. caratere
    recebe um tabuleiro e devolve a cadeia de caracteres que o representa\n
    (a representação “para os nossos olhos”), de onde:\n
        (1) Os símbolos "X"/"O" representam as bolas brancas ou pretas, dependendo\n
        do símbolo escolhido pelo utilizador. O símbolo "+" representa uma posição vazia no tabuleiro\n
        (2) Cada símbolo no tabuleiro é separado horizontalmente por "---" \n
        e verticalmente por " | ".
    """
    
    numero_colunas=obtem_dimensao(tab)[1]
    numero_linhas=obtem_dimensao(tab)[0]
    rep_tab=''

    for i_linha in range(len(tab)):
    #Cria o tabuleiro
        for i_coluna in range(len(tab[0])):
        #Cria uma linha
            valor_col=tab[i_linha][i_coluna]

            if valor_col==1:
                rep_tab+='X'
            elif valor_col==0:
                rep_tab+='+'
            elif valor_col==-1:
                rep_tab+='O'

            
            
            if i_coluna<numero_colunas-1:
            #Adiciona-se o tracejado depois do símbolo ((O/X/+) até à penúltima linha
            #Evita que se adicione tracejado fora do tabuleiro
            
                rep_tab+='---'
        
        if i_linha<numero_linhas-1:
        #A cada criação de 1 linha, adiciona-se as linhas verticais em baixo
            rep_tab+='\n'+'|   '*(numero_colunas-1)+'|\n'
    
    return rep_tab

def eh_posicao_valida(tab,pos): 
    """
    eh posicao valida: tabuleiro x   posicao → booleano \n
    A função recebe um tabuleiro e uma posição, e devolve True se a \n
    posição corresponde a uma posição do tabuleiro, e False caso contrário. Se algum dos \n
    argumentos dados for inválido, a função deve gerar um erro com a mensagem \n
    'eh_posicao_valida: argumentos invalidos'.
    """
    if not eh_tabuleiro(tab) or type(pos)!=int:
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    
    numero_total_posicoes=obtem_dimensao(tab)[0]*obtem_dimensao(tab)[1]

    if 1<=pos<=numero_total_posicoes:
        return True
    else:
        return False

def eh_posicao_livre(tab,pos):
    """
    eh posicao livre: tabuleiro x posicao → booleano \n
    Recebe um tabuleiro e uma posição do tabuleiro, e devolve True \n
    se a posição corresponde a uma posição livre (não ocupada por pedras), e False caso \n
    contrário. Se algum dos argumentos dado for inválido, a funçãoao deve gerar um erro com \n
    a mensagem 'eh_posicao_livre: argumentos invalidos'. 
    """

    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')

    linha_pos=identifica_linha(tab,pos)
    coluna_pos= identifica_coluna(tab,pos)
    valor=tab[linha_pos][coluna_pos]

    #A única forma da posição estar livre é se o valor na coluna for igual a 0
    if valor==0:
        return True
    else: 
        return False

def obtem_posicoes_livres(tab):
    """
    obtem posicoes livres: tabuleiro → tuplo \n
    Recebe um tabuleiro e devolve o tuplo com todas as posições \n
    livres do tabuleiro, ordenadas de menor a maior. Se o argumento dado for inválido, a \n
    função deve gerar um erro com a mensagem 'obtem_posicoes_livres: argumento invalido'.
    """

    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')

    pos_livres=()
    numero_colunas=obtem_dimensao(tab)[1]

    for i_linha in range(len(tab)):
        for i_coluna in range(len(tab[i_linha])):

            if tab[i_linha][i_coluna]==0:
                pos=(i_linha*numero_colunas)+i_coluna+1
                pos_livres+=(pos,)

    return pos_livres

def obtem_posicoes_jogador(tab,jog):
    """
    obtem posicoes jogador: tabuleiro x inteiro → tuplo \n
    Recebe um tabuleiro e um inteiro identificando um jogador \n
    (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas) e \n
    devolve o tuplo com todas as posições do tabuleiro ocupadas por pedras do jogador, \n
    ordenadas de menor a maior. Se algum dos argumentos dados for inválidos, a função deve \n
    gerar um erro com a mensagem 'obtem_posicoes_jogador: argumentos invalidos'.
    """

    if not eh_tabuleiro(tab) or type(jog)!=int or jog not in [-1,1]:
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')

    numero_colunas=obtem_dimensao(tab)[1]
    pos_jogador=()

    for i_linha in range(len(tab)):
        for i_coluna in range(len(tab[i_linha])):
            
            if tab[i_linha][i_coluna]==jog:
                pos=(i_linha*numero_colunas)+i_coluna+1
                pos_jogador+=(pos,)

    return pos_jogador

def obtem_posicoes_adjacentes(tab,pos):
    """
    obtem posicoes adjacentes: tabuleiro x posicao → tuplo \n
    Recebe um tabuleiro e uma posição do tabuleiro, e \n
    devolve o tuplo formado pelas posições do tabuleiro adjacentes (horizontal, vertical e \n
    diagonal), ordenadas de menor a maior. Se algum dos argumentos dado for inválido, a \n
    função deve gerar um erro com a mensagem 'obtem_posicoes_adjacentes: argumentos invalidos'.
    """

    if not eh_tabuleiro(tab) or not eh_posicao(pos) or not eh_posicao_valida(tab,pos):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')

    numero_colunas=obtem_dimensao(tab)[1]
    numero_linhas=obtem_dimensao(tab)[0]
    posicoes_adj=()
    total_posicoes=numero_colunas*numero_linhas

    for valor in range(1,total_posicoes+1):
        if valor!=pos and f_chebychev(tab,valor,pos)==1:
        #valor!=pos para que o valor de pos não apareça no tuplo retornado
            posicoes_adj+=(valor,)

    return posicoes_adj

def ordena_posicoes_tabuleiro(tab,tup):
    """
    ordena posicoes tabuleiro: tabuleiro x tuplo → tuplo \n
    recebe um tabuleiro e um tuplo de posições do tabuleiro (potencialmente vazio), e \n
    devolve o tuplo com as posições em ordem ascendente de distância à posição central do tabuleiro. \n
    Posições com igual distância à posição central, são ordenadas de menor a maior de acordo com a \n
    posição que ocupam no tabuleiro. Se algum dos argumentos dado for inválido, a função deve gerar \n
    um erro com a mensagem 'ordena_posicoes_tabuleiro: argumentos invalidos'.
    """

    if not eh_tabuleiro(tab) or not isinstance(tup,tuple):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')

    numero_linhas=obtem_dimensao(tab)[0]
    numero_colunas=obtem_dimensao(tab)[1]
    c=(numero_linhas//2)*numero_colunas+numero_colunas//2+1 #posicao central do tabuleiro

    
    def ordenacao_criterios(x): #x representa um único elemento do tuplo
        """
        A função percorre todos os elementos do tuplo para criar uma chave de ordenação \n
        para cada valor, ou seja, transforma cada valor dentro do tuplo noutro valor \n
        (com base nos critéior dados) e compara cada um desses novos valores e \n
        ordena os valores do tuplo fornecido de acordo com a sua chave de ordenação. \n
        o critério2 só se aplica se o critério1 for igual.
        """
        if not eh_posicao_valida(tab,x):
            raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')

        crit1=f_chebychev(tab,x,c)
        crit2=identifica_linha(tab,x)
        crit3=identifica_coluna(tab,x)
        return(crit1,crit2,crit3)
    
    return tuple(sorted(tup,key=ordenacao_criterios))

def marca_posicao(tab,pos,jog):
    """
    marca posicao: tabuleiro x posicao x inteiro → tabuleiro \n
    Recebe um tabuleiro, uma posição livre do tabuleiro e um \n
    inteiro identificando um jogador (1 para o jogador com pedras pretas ou -1 para o \n
    jogador com pedras brancas), e devolve um novo tabuleiro com uma nova pedra do \n
    jogador indicado nessa posição. Se algum dos argumentos dados for inválidos, a função \n
    deve gerar um erro com a mensagem 'marca_posicao: argumentos invalidos'.
    """
    
    if not eh_tabuleiro(tab) or not eh_posicao_valida(tab,pos) or pos not in obtem_posicoes_livres(tab) or type(jog)!=int or jog not in [-1,1]:
        raise ValueError('marca_posicao: argumentos invalidos')
    
    linha_pos=identifica_linha(tab,pos)
    coluna_pos=identifica_coluna(tab,pos)

    #Estratégia: converter todo o tabuleiro (incuindo as linhas do mesmo) a listas
    #e trabalhar com as listas. No fim, converter tudo a tuplos de novo.
    l_tab=[]
    for linha in tab:
        l_tab.append(list(linha))

    #Mudar a posição vazia livre pelo o identificador do jogador
    l_tab[linha_pos][coluna_pos]=jog
    
    novo_tab=[]
    for linha in l_tab:
        novo_tab.append(tuple(linha))

    return tuple(novo_tab)

def verifica_k_linhas(tab,pos,jog,k):
    """
    verifica k linhas: tabuleiro x posicao x inteiro x inteiro → booleano \n
    recebe um tabuleiro, uma posição do tabuleiro, um valor inteiro identificando \n
    um jogador (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas), \n
    e um valor inteiro positivo k, e devolve True se existe pelo menos uma linha (horizontal, \n
    vertical ou diagonal) que contenha a posição com k ou mais pedras consecutivas do jogador \n
    indicado, e False caso contrário. Se algum dos argumentos dado for inválido, \n
    a função deve gerar um erro com a mensagem 'verifica_k_linhas: argumentos invalidos'.
    """
    
    if not eh_tabuleiro(tab) or not eh_posicao_valida(tab,pos) or type(jog)!=int or jog not in [-1,1] or type(k)!=int or k<=0:
        raise ValueError('verifica_k_linhas: argumentos invalidos')

    vlrs_linhas=obtem_linha(tab,pos)
    vlrs_colunas=obtem_coluna(tab,pos)
    vlrs_diagonais=obtem_diagonais(tab,pos)[0]
    vlrs_antidiagonais=obtem_diagonais(tab,pos)[1]

    linhas=(vlrs_linhas,vlrs_colunas,vlrs_diagonais,vlrs_antidiagonais)
    
    for linha in linhas:
        contador=0
        lista_valores=[]
        for x in linha:
            if obtem_valor(tab,x)==jog: 
                contador+=1
                lista_valores.append(x)
            else: #se x!=jog
                contador=0
                lista_valores.clear()

            if contador>=k and pos in lista_valores:
                return True
    return False

def eh_fim_jogo(tab,k):
    """
    eh fim jogo: tabuleiro x inteiro → booleano \n
    recebe um tabuleiro e um valor inteiro positivo k, e devolve um \n
    booleano a indicar se o jogo terminou (True) ou não (False). Um jogo pode terminar \n
    caso um dos jogadores tenha k pedras consecutivas, ou caso já não existam mais posições \n
    livres para marcar. Se algum dos argumentos dado for inválido, a função deve gerar um \n
    erro com a mensagem 'eh_fim_jogo: argumentos invalidos'.
    """

    if not eh_tabuleiro(tab) or type(k)!=int or k<0:
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    
    n_linhas=obtem_dimensao(tab)[0]
    n_colunas=obtem_dimensao(tab)[1]
    
    for pos in range(1,n_linhas*n_colunas+1):
        #Verifica se há k consecutivas para jog=1 ou jog=-1, logo se há vencedores ou não
        if verifica_k_linhas(tab,pos,1,k) or verifica_k_linhas(tab,pos,-1,k):
            return True

    #Verifica se o tabuleiro está cheio ou não
    for linha in tab:
        if 0 in linha:
            return False
    
    #Retorna True se não há vencedores, mas se o tabuleiro não tem posições livres
    return True

def escolhe_posicao_manual(tab):
    """
    escolhe posicao manual: tabuleiro → posicao \n
    Recebe um tabuleiro e devolve uma posição introduzida manualmente pelo jogador. A função \n
    deve apresentar a mensagem 'Turno do jogador. Escolha uma posicao livre: ' , repetindo a \n
    mensagem até o jogador introduzir uma posição livre. Se o argumento dado for inválido, \n
    a função deve gerar um erro com a mensagem 'escolhe_posicao_manual: argumento invalido'.
    """

    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
   
    while True: 
        pos_manual=input('Turno do jogador. Escolha uma posicao livre: ')
        #solicitação da posição ao utilizador

        if not pos_manual.isdigit():
            continue

        pos_manual=int(pos_manual)
        
        if eh_posicao(pos_manual) and obtem_valor(tab,pos_manual)==0:
        #Se a posição inserida for válida e se a posição estiver vazia devolve o 
        #número, se não, volta a pedir um número ao utilizador até esta indicar um número com a posição vazia
            return pos_manual

def escolhe_posicao_auto(tab,jog,k,lvl):
    """
    escolhe posicao auto: tabuleiro x inteiro x nteiro x cad. carateres → posicao \n
    Recebe um tabuleiro (em que o jogo não terminou ainda), um inteiro identificando um jogador \n
    (1 para o jogador com pedras pretas ou -1 para o jogador com pedras brancas), um inteiro positivo \n
    correspondendo ao valor k de um jogo m, n, k, e a cadeia de carateres correspondente à estratégia, \n
    e devolve a posição escolhida automaticamente de acordo com a estratégia selecionada. As estratégias \n
    devem ser identificadas pelas cadeias de cararateres 'facil', 'normal' ou 'dificil'. Sempre que houver\n
    mais do que uma posição que cumpra um dos critérios definidos nas estratégias anteriores, deve \n
    escolher a posição mais próxima da posição central do tabuleiro Se algum dos argumentos dados for \n
    inválidos, a função deve gerar um erro com a mensagem 'escolhe_posicao_auto: argumentos invalidos'.
    """
    
    if not eh_tabuleiro(tab) or jog not in [-1,1] or eh_fim_jogo(tab,k) or not isinstance(lvl,str) or lvl not in ['facil','normal','dificil']:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    if k<=0:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    
    if lvl=='facil':
        return e_facil(tab,jog)
    
    if lvl=='normal':
        return e_normal(tab,jog,k)
        
    if lvl=='dificil':
        return e_dificil(tab,jog,k)
   
def jogo_mnk(cfg,jog,lvl):
    """
    jogo mnk: tuplo x inteiro x cad. carateres → inteiro\n
    É a função principal que permite jogar um jogo completo m, n, k de um jogador contra o computador. \n
    A função recebe um tuplo de três valores inteiros correspondentes aos valores de configuração \n
    do jogo m, n e k; um inteiro identificando a cor das pedras do jogador humano (1 para as pedras pretas \n
    ou -1 para as pedras brancas); e uma cadeia de caracteres identificando a estratégia de jogo utilizada \n
    pela méquina. O jogo começaa sempre com o jogador com pedras pretas a marcar uma posição\n
    livre e termina quando um dos jogadores vence ou se não existirem posições livres no tabuleiro.\n
    A função mostra o resultado do jogo (VITORIA, DERROTA ou EMPATE) e devolve um inteiro identificando o \n
    jogador vencedor (1 para preto ou -1 para branco), ou 0 em caso de empate. A função deve verificar a \n
    validade dos seus argumentos, gerando um erro com a mensagem 'jogo_mnk: argumentos invalidos'.
    """
        
    if not isinstance(cfg,tuple) or len(cfg)!=3 or type(cfg[0])!=int or type(cfg[1])!=int or type(cfg[2])!=int or not 2<=cfg[0]<=100 or not 2<=cfg[1]<=100 or not cfg[2]>0 or type(jog)!=int or jog not in [-1,1] or not isinstance(lvl, str) or lvl not in ['facil','normal','dificil']:
        raise ValueError('jogo_mnk: argumentos invalidos')

    m,n,k=cfg

    def tabuleiro_vazio(m,n):
        """
        A função define um tabuleiro vazio com as dimensões que o utilizador fornece em cgf
        para que o jogo possa começar
        """
        tabuleiro_vazio=[]
        for linha in range(m):
            linha_nova=[]
            for coluna in range(n):
                linha_nova.append(0)
            tabuleiro_vazio.append(tuple(linha_nova))
        return tuple(tabuleiro_vazio)

    tabuleiro=tabuleiro_vazio(m,n)
    print('Bem-vindo ao JOGO MNK.')
    print("O jogador joga com 'X'." if jog==1 else "O jogador joga com 'O'.")
    print(tabuleiro_para_str(tabuleiro))

    jogador_atual=1
    
    while not eh_fim_jogo(tabuleiro,k):

        if jogador_atual==jog:
        #Jogo começa sempre com o jogador de pedras pretas (1) a marcar numa posição livre
            pos_manual=escolhe_posicao_manual(tabuleiro)
            tabuleiro=marca_posicao(tabuleiro,pos_manual,jog)
            print(tabuleiro_para_str(tabuleiro))
            if verifica_k_linhas(tabuleiro,pos_manual,jog,k):
                print('VITORIA')
                return jog
            
        else:
            print('Turno do computador ('+lvl+'):')
            pos_auto=escolhe_posicao_auto(tabuleiro,-jog,k,lvl)
            tabuleiro=marca_posicao(tabuleiro,pos_auto,-jog)
            print(tabuleiro_para_str(tabuleiro))
            if verifica_k_linhas(tabuleiro,pos_auto,-jog,k):
                print('DERROTA')
                return -jog

        if obtem_posicoes_livres(tabuleiro)==0:
        #Se nenhuma dos jogadores (tanto o utilizador como a máquina) tiverem feito 
        #k em linha, o jogo termina e o tabuleiro está cheio
            print('EMPATE')
            return 0
            
        jogador_atual=-jogador_atual #Alternar o jogador
    
    

#Funções auxiliares:
def identifica_linha(tab,pos):
    """
    A função recebe uma posição e indica o valor da linha em que esta se encontra
    """

    numero_colunas=obtem_dimensao(tab)[1]
    linha=(pos-1)//numero_colunas #formula para saber qual a linha da posição
    return linha

def identifica_coluna(tab,pos):
    """
    A função recebe uma posição e indica o valor da coluna esta em que se encontra
    """

    numero_colunas=obtem_dimensao(tab)[1]
    coluna=(pos-1)%numero_colunas #formula para saber qual é a coluna da posição
    return coluna

def f_chebychev(tab,pos1,pos2):
    """
    A função define a distância entre quaisquer dois pontos
    """
    linha_pos1=identifica_linha(tab,pos1)
    coluna_pos1=identifica_coluna(tab,pos1)
    linha_pos2=identifica_linha(tab,pos2)
    coluna_pos2=identifica_coluna(tab,pos2)

    #formula da distancia entre quaisquer dois pontos
    distancia=max(abs(linha_pos1-linha_pos2),abs(coluna_pos1-coluna_pos2)) 
    return distancia

def lista_tabuleiro(tab):
    """
    Esta função irá transformar o tabuleiro numa lista para que este possa ser alterável
    """
    l_tab=[]
    for linha in tab:
        l_tab.append(list(linha))
    return l_tab

def e_facil(tab,jog):
    """
    Esta função serve para definir a estratégia fácil de jogo. Recebe um tabuleiro e uma posição que indica\n
    o jogador humano.
    """
    posicoes_livres=obtem_posicoes_livres(tab)
    lista_valores=[]
    for p in posicoes_livres: 
    #Para cada valor nas posições livres (p):

        p_adjacentes=obtem_posicoes_adjacentes(tab,p)
        for adj in p_adjacentes:
        #Verifica-se se a posição adjacente (adj) é válida
                    
            if obtem_valor(tab,adj)==jog: 
            #Se adj tiver uma pedra do jogador atual (jog), então é possível jogar uma pedra
            #própria nesta posição adjacente livre
                lista_valores.append(p)
                break #quebra volta ao incio do loop
                    

    tup_valores=tuple(lista_valores)
    if len(tup_valores)==0: 
    #quer dizer que não há nenhuma posição livre em que a adjacente seja uma peça própria e,
    #nesse caso, joga na posição livre mais perto do centro
        tup_valores=obtem_posicoes_livres(tab)
        #neste caso, como podemos jogar numa qualquer posição livre, o tup_valores passa a ser 
        #um tuplo com todas as posições livres do tabuleiro
    tup_valores_ordenados=ordena_posicoes_tabuleiro(tab,tup_valores) #jogará na posição mais próxima do meio 
    return tup_valores_ordenados[0]
    

def e_normal(tab,jog,k):
    """
    Esta função serve para definir a estratégia normal de jogo. Recebe um tabuleiro, uma posição que indica\n
    o jogador humano e um valor de k (para fazer k peças consecutivas).
    """
                       
    def verifica_linhas(tab, pos, jog, L):
        """
        Função auxiliar que verifica que, se ao jogar uma peça, é possível criar \n
        L peças seguidas do mesmo jogador
        """
        vlrs_linhas=obtem_linha(tab,pos)
        vlrs_colunas=obtem_coluna(tab,pos)
        vlrs_diagonais=obtem_diagonais(tab,pos)[0]
        vlrs_antidiagonais=obtem_diagonais(tab,pos)[1]

        #indica dos os valores das linhas(horizontal,vertical,diagonais)
        linhas=(vlrs_linhas,vlrs_colunas,vlrs_diagonais,vlrs_antidiagonais)

        for linha in linhas:
            contador=0
            for valor in linha:
                if valor==jog: #se o valor for igual ao do jogador
                    contador+=1 #incrementa-se um no contador de forma a ver qual é o maior número de peças do jogador seguidas
                else:
                    contador=0 #se deixar de haver peças seguidas na linha, o contador reinicia
                if contador>=L: #verificar se o jogador tem pelo menos L peças consecutivas e caso isso aconteça, retorna True, se não, retorna False
                    return True
        return False

    n_linhas=obtem_dimensao(tab)[0]
    n_colunas=obtem_dimensao(tab)[1]

    pos_possiveis_vitoria=[] 
    pos_de_bloqueio=[]

    for L in range(k,0,-1):
    #o valor de k vai diminuindo de 1 em 1 até encontrar o L, neste caso, seria o maior k possível

        for pos in range(1,n_linhas*n_colunas+1):
        #Verifica todas as posições no tabuleiro
            linha_pos=identifica_linha(tab,pos)
            coluna_pos=identifica_coluna(tab,pos)

            if tab[linha_pos][coluna_pos]==0: #Se a posição estiver livre
                tabuleiro_novo=lista_tabuleiro(tab) #cópia do tabuleiro para simular um jogo

                #simular uma jogada do jogador, substituindo o valor da pos pelo identificador do jogador
                tabuleiro_novo[linha_pos][coluna_pos]=jog
                #Verifica se o jogador tem
                if verifica_linhas(tabuleiro_novo,pos,jog,L):
        
                    pos_possiveis_vitoria.append(pos)

                #simular uma jogada da máquina
                tabuleiro_novo[linha_pos][coluna_pos]=-jog
                if verifica_linhas(tabuleiro_novo,pos,-jog,L):
                    pos_de_bloqueio.append(pos)

    #caso não haja seja colocar L peças consecutivas próprias ou impedir o adversário de colocar L peças consecutivas
    #jogar na primeira posição livre mais próxima do centro
    if len(tuple(pos_possiveis_vitoria))==0 and len(tuple(pos_de_bloqueio))==0:
        posicoes_livres=obtem_posicoes_livres(tab) 
        posicoes_livres_ordenadas=ordena_posicoes_tabuleiro(tab,posicoes_livres)
        return posicoes_livres_ordenadas[0]

    if pos_possiveis_vitoria:
        return ordena_posicoes_tabuleiro(tab,tuple(pos_possiveis_vitoria))[0]

    if pos_de_bloqueio:
        return ordena_posicoes_tabuleiro(tab,tuple(pos_de_bloqueio))[0]
            
    return None

def simula_jogo_n(tab,jog,pos_normal,k):
    """
    Esta função recebe um tabuleiro, um número que identifica o jogador, uma posição (pos_normal)\n
    e um k (que indica quantas peças em linha é preciso ter para vencer o jogo)
    """
    tabuleiro_novo=marca_posicao(tab,pos_normal,jog)
    
    #como o jogador identificado pelo número jog acabou de jogar,
    #agora joga o adversário
    prox_jog=-jog

    #Enquanto ainda há posições livres no tabuleiro:
    while not eh_fim_jogo(tabuleiro_novo,k):
        
        #O próximo jogador irá escolher a próxima posição com base na estratégia normal
        pos_normal=e_normal(tabuleiro_novo,prox_jog,k)
        tabuleiro_novo=marca_posicao(tabuleiro_novo,pos_normal,prox_jog)
            
        if verifica_k_linhas(tabuleiro_novo,pos_normal,prox_jog,k):
        #Se o jogar tiver atingido o número de k peças em linha para ganhar
            if prox_jog==jog:
                return 2 #retorna 2 e o jogar vence
            else:
                #Se o adversário tiver k peças para ganhar
                return 0 #retorn 0 e o jogador perde
        #Turno do próxio jogador
        prox_jog=-prox_jog
    #Se não existirem k peças em linha para nenhum jogador ganhar
    #Quer dier que o jogo está empatado
    return 1

def e_dificil(tab,jog,k):
    """
    Esta função serve para definir a estratégia dificil de jogo. Recebe um tabuleiro, uma posição que indica\n
    o jogador humano e um valor de k (para fazer k peças consecutivas).
    """

    n_linhas=obtem_dimensao(tab)[0]
    n_colunas=obtem_dimensao(tab)[1]
    pos_livres=obtem_posicoes_livres(tab)
    pos_possiveis_vitoria=[]
    #Armazena as posições em que é possível colocar uma peça e ganhar
    pos_de_bloqueio=[]
    #Armazena as posições possíveis de bloquear o adversário de ganhar
            
    for pos in pos_livres:
        linha_pos=identifica_linha(tab,pos)
        coluna_pos=identifica_coluna(tab,pos)
                
        #Verifica se aposição está livre
        if 0<=linha_pos<n_linhas and 0<=coluna_pos<n_colunas and tab[linha_pos][coluna_pos]==0:
            #Converte o tabuleiro numa lista, para que este possa ser alterado
            tabuleiro_novo=lista_tabuleiro(tab)

            #substitui no tabuleiro, a posição do jogador
            tabuleiro_novo[linha_pos][coluna_pos]=jog
            #Verifica se o jogador consegue obter k peças em linha
            if verifica_k_linhas(tuple(tuple(linha) for linha in tabuleiro_novo),pos,jog,k):
                    #Se isso for possível, armazena esse valor a uma lista de valores em que é possível colocar outra peça e fazer o jogador ganhar
                    pos_possiveis_vitoria.append(pos)

            #substitui no tabuleiro, a posição do adversário      
            tabuleiro_novo[linha_pos][coluna_pos]=-jog
            #Verifica se o adversário consegue obter k peças em linha  
            if verifica_k_linhas(tuple(tuple(linha) for linha in tabuleiro_novo),pos,-jog,k):
                    #Se for possível, adicionamos esse valor a uma lista de valores em que é possível colocar uma peça e impedir o adversário de ganhar
                    pos_de_bloqueio.append(pos)

    if pos_possiveis_vitoria:
        #Se houver várias posições possíveis, devolve a primeira posição livre mais próxima do centro
        return ordena_posicoes_tabuleiro(tab,tuple(pos_possiveis_vitoria))[0]
    if pos_de_bloqueio:
        #Se houver várias posições possíveis, devolve a primeira posição livre mais próxima do centro
        return ordena_posicoes_tabuleiro(tab,tuple(pos_de_bloqueio))[0]

    melhor_res=0
    melhor_pos=[]
    #verifica todas as posições livres no tabuleiro
    for livre in obtem_posicoes_livres(tab):
        #simula-se um uma jogada e devolve-se um valor (2:vitoria,1:empate,0:derrota)
        res=simula_jogo_n(tab,jog,livre,k)
        if res>=melhor_res:
            #caso o resultado for seja o maior  encontrado até agora
            if res>melhor_res:
                melhor_res=res #substitui-se esse valor no melhor_res (melhor resultado obtido ate agora)
                melhor_pos.clear() #reinicia a lista de melhores posições porque um melhor resultado foi encontrado
            
            melhor_pos.append(livre) #adiciona-se esse valor a lista de melhores posições
    
        
    return ordena_posicoes_tabuleiro(tab,tuple(melhor_pos))[0]


t=((1,0,0,-1),(1,-1,-1,1),(0,0,1,-1))
#print(obtem_coluna(t,6))
print(obtem_diagonais(t,6))
#print(obtem_posicoes_livres(t))


        


        
   


