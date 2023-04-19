def define_posicoes(linha,coluna,orientacao,tamanho):
    lista=[]
    for e in range (tamanho):
        if orientacao=='vertical':
            lista.append([linha+e,coluna])
        elif orientacao=='horizontal':
            lista.append([linha,coluna+e])
    return lista
print(define_posicoes(2,4,'vertical',3))