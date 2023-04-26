def define_posicoes(linha,coluna,orientacao,tamanho):
    lista=[]
    for e in range (tamanho):
        if orientacao=='vertical':
            lista.append([linha+e,coluna])
        elif orientacao=='horizontal':
            lista.append([linha,coluna+e])
    return lista
def preenche_frota(frota,nome,linha,coluna,orientacao,tamanho):
    if nome not in frota.keys():
        frota[nome]=[]
    frota[nome].append(define_posicoes(linha,coluna,orientacao,tamanho))
    return frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
def posiciona_frota(info_navios):
    tabuleiro = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for posicoes in info_navios.values():
        for lista in posicoes:
          for i in lista:
            tabuleiro[i[0]][i[1]]=1
    return tabuleiro
def afundados(frota,tabuleiro):
    x=0
    for nome in frota.keys():
        for lugares in frota[nome]:
            y=0
            for lugar in lugares:
                if tabuleiro[lugar[0]][lugar[1]]=='X':
                    y+=1
            if y==len(lugares):
                x+=1
    return x
def posicao_valida (infos,linha,coluna,orientacao,tamanho):
    pos_nav = define_posicoes(linha,coluna,orientacao,tamanho)
    for i in pos_nav:
        if i[0] > 9 or i[1]>9:
            return False
        for posicoes in infos.values():
            for f in posicoes:
                for e in f:
                    if i[0] == e[0] and i[1] == e[1]:
                        return False
    return True

navios = ["porta-aviões","navio-tanque","navio-tanque","contratorpedeiro","contratorpedeiro","contratorpedeiro","submarino","submarino","submarino","submarino"]
tamanhos = {"porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1}
frota = {"porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": []}

for nome in navios:
    print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanhos[nome]}')
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if nome != 'submarino':
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'
    if nome == 'submarino':
        orientacao = 0
    p = posicao_valida (frota,linha,coluna,orientacao,tamanhos[nome])
    while p == False:
        print('Esta posição não está válida!')
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanhos[nome]}')
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if nome != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        if nome == 'submarino':
            orientacao = 0
        p = posicao_valida (frota,linha,coluna,orientacao,tamanhos[nome])
    d = define_posicoes(linha,coluna,orientacao,tamanhos[nome])
    frota_preenchida = preenche_frota(frota,nome,linha,coluna,orientacao,tamanhos[nome])

print(frota_preenchida)
        
    
        


