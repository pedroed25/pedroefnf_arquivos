def define_posicoes(linha,coluna,orientacao,tamanho):
    lista=[]
    for e in range (tamanho):
        if orientacao=='vertical':
            lista.append([linha+e,coluna])
        elif orientacao=='horizontal':
            lista.append([linha,coluna+e])
    return lista