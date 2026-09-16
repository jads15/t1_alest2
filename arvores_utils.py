from anytree import Node
def processar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, "r") as f: 
        for linha in f:                   
            for palavra in linha.split():
                yield int(palavra)         
gerador_arvore = processar_arquivo("/home/jo-o-antonio/Downloads/anytree/casos-cohen/casom7.txt")

def LerValores(j,G):
    if j == 0:
        return []
    else:
        return [next(G)]+LerValores(j-1,G)

def processarFilhos(i,P,G):
    if i == 0:
        return 0
    else:
        construirNodo(G,P)
        processarFilhos(i-1,P,G)

def construirNodo(G,P  =None):
    f = next(G)
    n = next(G)
    N = Node("Nodo", parent= P)
    processarFilhos(f,N,G)
    N.valores = LerValores(n,G)
    return N
def somaArvore(N):
    return sum(N.valores) + auxSoma(N.children)

def auxSoma(C):
    if  not  C:
        return 0
    else:
     return somaArvore(C[0])+auxSoma(C[1:])

def altura(N):
  if not N.children:
      return 0 
  else:
     return 1+ auxAltura(N.children) 
def auxAltura(C):
    if  not C:
        return 0
    else:
        return max(altura(C[0]), auxAltura(C[1:]))


def quantidadeNos(N):
    return 1+ AuxNos(N.children)

def AuxNos(C):
    if not C:
        return 0
    else:
        return quantidadeNos(C[0])+AuxNos(C[1:])
